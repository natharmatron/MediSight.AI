import pandas as pd
import numpy as np

# Create the dataset
data = [
    ['Young', 'Low', 'No'],
    ['Young', 'High', 'Yes'],
    ['Middle', 'High', 'Yes'],
    ['Young', 'Middle', 'No'],
    ['Senior', 'Low', 'No'],
    ['Middle', 'Middle', 'Yes'],
    ['Senior', 'Middle', 'No'],
    ['Middle', 'High', 'No'],
    ['Senior', 'High', 'Yes']
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Age', 'Income', 'Buys_Product'])

# Display the original dataset
print("Original Dataset:")
print(df)
print("\n")

# Function to remove duplicates with different class labels
def remove_conflicting_duplicates(dataframe):
    # Group by attribute columns and check if there are different class labels
    attribute_cols = dataframe.columns[:-1]  # All columns except the class label
    duplicates = dataframe.duplicated(subset=attribute_cols, keep=False)
    
    if duplicates.any():
        print("Found duplicates with same attributes:")
        dup_rows = dataframe[duplicates].sort_values(by=list(attribute_cols))
        print(dup_rows)
        
        # For each set of duplicates, remove them if they have different class labels
        to_remove = []
        for attrs, group in dataframe.groupby(list(attribute_cols)):
            if len(group['Buys_Product'].unique()) > 1:
                print(f"Removing conflicting tuples with attributes: {attrs}")
                to_remove.extend(group.index)
        
        return dataframe.drop(to_remove)
    
    return dataframe

# Clean the dataset
cleaned_df = remove_conflicting_duplicates(df)
print("Cleaned Dataset:")
print(cleaned_df)
print("\n")

# Calculate Gini Index for a split
def calculate_gini(groups, classes):
    total_instances = sum(len(group) for group in groups)
    gini = 0.0
    
    for group in groups:
        size = len(group)
        if size == 0:
            continue
            
        # Calculate Gini index for this group
        score = 0.0
        for class_val in classes:
            p = (group['Buys_Product'] == class_val).sum() / size
            score += p * p
        
        # Subtract from 1 to get Gini index
        gini += (1.0 - score) * (size / total_instances)
        
    return gini

# Split the dataset based on an attribute
def split_dataset(dataframe, attribute):
    attribute_values = dataframe[attribute].unique()
    groups = [dataframe[dataframe[attribute] == val] for val in attribute_values]
    return groups, attribute_values

# Find the best attribute to split on
def find_best_split(dataframe):
    class_values = dataframe['Buys_Product'].unique()
    attributes = dataframe.columns[:-1]  # All columns except the class label
    
    best_attribute = None
    best_gini = float('inf')
    best_groups = None
    best_values = None
    
    # Evaluate each attribute
    for attribute in attributes:
        groups, values = split_dataset(dataframe, attribute)
        gini = calculate_gini(groups, class_values)
        
        print(f"Attribute: {attribute}, Gini Index: {gini}")
        
        # Check if this attribute gives a better split
        if gini < best_gini:
            best_gini = gini
            best_attribute = attribute
            best_groups = groups
            best_values = values
    
    return best_attribute, best_gini, best_groups, best_values

# Find the best attribute to split on for the root node
best_attribute, best_gini, best_groups, best_values = find_best_split(cleaned_df)

print(f"\nBest attribute for root node: {best_attribute} with Gini Index: {best_gini}")
print("\nSplit details:")
for i, value in enumerate(best_values):
    group = best_groups[i]
    yes_count = (group['Buys_Product'] == 'Yes').sum()
    no_count = (group['Buys_Product'] == 'No').sum()
    print(f"  {best_attribute} = {value}: {len(group)} instances ({yes_count} Yes, {no_count} No)")

# Calculate Gini index for each value of the best attribute
print("\nGini calculation for each value of the best attribute:")
for i, value in enumerate(best_values):
    group = best_groups[i]
    total = len(group)
    if total > 0:
        yes_ratio = (group['Buys_Product'] == 'Yes').sum() / total
        no_ratio = (group['Buys_Product'] == 'No').sum() / total
        gini_value = 1 - (yes_ratio**2 + no_ratio**2)
        print(f"  {best_attribute} = {value}: Gini = {gini_value:.4f}")