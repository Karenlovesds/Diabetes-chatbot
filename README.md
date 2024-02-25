# Diabetes Management Chatbot README

## Overview
This chatbot serves as a tool for facilitating access to Australian diabetes management guidelines through scientific papers. It's designed to assist users in finding answers to common questions regarding diabetes care without the need to manually search through PDF documents. The chatbot leverages the LangChain library for processing and answering queries based on the content of the uploaded PDFs.

### Features
- Support for multiple PDF uploads
- Integration with OpenAI's language model for question answering
- Persistent storage for document processing
- Customizable for non-profit use with a focus on diabetes management

## Environment Setup

### Prerequisites
- Miniconda installed on your system

### Installation Steps

1. Ensure Miniconda is installed and properly set up by running `conda --version`. If Miniconda is not installed, follow the installation guide available on the Miniconda website.
2. conda env create -f diabetes_chatbot_env.yml
3. conda activate diabetes_chatbot_env
4. cd cd path/to/your/chatbot/Scripts
5. stremlit run chatbot.py

## Application Structure: 

- **Streamlit Interface**: Provides a user-friendly web interface for interacting with the chatbot.
- **PDF Processing**: Utilizes the PyMuPDFLoader for loading and processing PDF documents.
- **Text Splitting**: Employs the RecursiveCharacterTextSplitter for handling large documents by splitting them into manageable chunks.
- **Question Answering**: Integrates OpenAI's language models for generating responses to user queries based on the document content.
- **Vector Storage**: Uses Chroma for indexing and searching document content, facilitating efficient question answering.
- **Sample Questions**: Includes pre-defined samples related to diabetes management guidelines to demonstrate the chatbot's capabilities.

### Customizing the Chatbot

The provided code snippets for handling sample questions and modifying responses can be tailored to fit specific requirements or to include additional educational content. Users are encouraged to explore the LangChain documentation for further customization options.
