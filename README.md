# Chat with Multiple PDFs

This project allows you to chat with multiple PDF documents and ask questions about the content.

## Description

The code provided uses the Streamlit framework to create a user interface for interacting with PDF documents. It uses the PyPDF2 library to extract text from the PDFs and the langchain library for language processing tasks such as text splitting, embeddings, and conversational retrieval. The chat functionality is powered by the Hugging Face Hub and Google Flan T5 XXL model.

## Dependencies

- streamlit
- dotenv
- PyPDF2
- langchain
- htmlTemplates

## Installation

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Change to the project directory: `cd repository`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `streamlit run app.py`
2. Upload your PDF documents.
3. Enter your question in the text input field.
4. Click the "Process" button to process the PDFs and get a response.

## Credits

This project was created using the langchain library, which is developed by [LangChain](https://github.com/langchain).

## Acknowledgments

The Hugging Face Hub and Google Flan T5 XXL model are used for the conversational retrieval functionality.

