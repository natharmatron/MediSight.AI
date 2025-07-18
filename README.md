# MediSight.AI 🩺💻

![MediSight.AI](https://img.shields.io/badge/MediSight.AI-Local--First%20AI%20Medical%20Analyzer-blue?style=for-the-badge&logo=appveyor)

Welcome to **MediSight.AI**, a local-first full-stack application designed to analyze medical PDFs using the AI model Apollo2-2B. This project emphasizes privacy and patient-friendly insights without relying on external APIs or cloud services.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Local Processing**: All data processing occurs on your device, ensuring that sensitive information remains private.
- **AI-Powered Insights**: Leverage the Apollo2-2B model to gain valuable insights from medical reports.
- **User-Friendly Interface**: A clean and intuitive chat interface allows users to interact seamlessly with the application.
- **FastAPI Backend**: The backend is built using FastAPI, providing a robust and efficient server for handling requests.
- **PDF Analysis**: Extract and analyze information from medical PDFs with ease.
- **Responsive Design**: Built with Tailwind CSS, the app is mobile-friendly and visually appealing.

## Technologies Used

This project utilizes a variety of technologies to create a smooth user experience:

- **AI & Machine Learning**: Apollo2-2B model for medical analysis
- **Backend**: FastAPI for efficient API development
- **Frontend**: Tailwind CSS for styling and responsiveness
- **PDF Processing**: Libraries for extracting data from PDF files
- **Data Handling**: PyTorch for machine learning operations
- **Transformers**: For natural language processing tasks

## Installation

To get started with MediSight.AI, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/natharmatron/MediSight.AI.git
   cd MediSight.AI
   ```

2. **Set Up the Environment**:
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the server with:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the Application**:
   Open your web browser and go to `http://localhost:8000`.

## Usage

Using MediSight.AI is straightforward:

1. **Upload a Medical PDF**: Drag and drop your PDF file into the designated area.
2. **Interact with the AI**: Use the chat interface to ask questions or request specific insights from the uploaded document.
3. **Review Insights**: The AI will provide responses based on the content of the PDF, ensuring you get the information you need.

### Example Interaction

- **User**: "What are the key findings in this report?"
- **AI**: "The report indicates elevated cholesterol levels and recommends further testing."

## Contributing

We welcome contributions to MediSight.AI! If you'd like to help, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Open a Pull Request**: Go to the original repository and click "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [natharmatron](https://github.com/natharmatron)

## Releases

To access the latest releases of MediSight.AI, visit our [Releases](https://github.com/natharmatron/MediSight.AI/releases) section. Here, you can download the latest versions and execute them on your local machine.

## Conclusion

MediSight.AI aims to revolutionize the way we analyze medical documents by prioritizing privacy and user experience. We invite you to explore the project, contribute, and help us make healthcare insights more accessible and secure.

Thank you for your interest in MediSight.AI! Your feedback and contributions are highly appreciated.