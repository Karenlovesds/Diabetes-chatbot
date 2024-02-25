import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyMuPDFLoader
import os
from openai_api_key import openai_api_key  # Import your OpenAI API key
from diabetes_management_samples import get_samples # Import your good samples (input and output pairs)


# 1. Setting the OpenAI API key in the environment for use by the application
os.environ['OPENAI_API_KEY'] = openai_api_key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# 2. Initializing the embeddings and language models with the OpenAI API key
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# 3. Defining persistent storage directories and collection names for document processing
persist_directory = 'pdf_persist'
collection_name = 'pdf_collection'

# 4. Loading the question answering chain
chain = load_qa_chain(llm, chain_type="refine")

# 5. Placeholder for the vectorstore, will be initialized after loading documents
vectorstore = None

# 6. Import sample questions and answers related to diabetes management guidelines
samples = get_samples()

# 7. Modifying sample inputs to include "Based on medical research," prefix and a note on consulting a physician
samples_modified = []

for sample in samples:
    input_text = sample["inputs"]
    # Split the input_text into question and answer
    question, answer = input_text.split("\n\nAnswer: ")
    # Prepend "Based on medical research, " to the question
    modified_question = "Based on medical research, " + question
    # Append a note to the end of each answer
    modified_answer = answer + "\n\nNote: Always consult a physician before making medical decisions."
    # Combine the modified question and answer
    modified_input = modified_question + "\n\nAnswer: " + modified_answer
    samples_modified.append({
        "inputs": modified_input
    })

# 8. Streamlit app definition
def main():
    # Configuring the Streamlit page
    st.set_page_config(page_title="PDF QA ChatBot", page_icon=":robot:")
    st.header("Diabetes ChatBot")

    # Initializing session state variables for conversation history
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.title("PDF Chatbot")

    # File uploader for PDF documents
    with st.container():
        uploaded_files = st.file_uploader("Upload your PDF files", type="pdf", accept_multiple_files=True)
        if not uploaded_files:
            vectorstore = None
            st.write("Please upload your PDF files")
        else:
            paths = []
            docs = []
            for file in uploaded_files:
                path = os.path.join('.', file.name)
                paths.append(path)
                with open(path, 'wb') as f:
                    f.write(file.getbuffer())
                    doc = PyMuPDFLoader(path)
                    docs.extend(doc.load())

            # Splitting and processing the documents
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            split_docs = text_splitter.split_documents(docs)
            vectorstore = Chroma.from_documents(split_docs, embeddings, collection_name=collection_name, persist_directory=persist_directory)
            vectorstore.persist()
            st.write("Done")

    # Answering questions based on the uploaded and processed documents
    with st.container():
        question = st.text_input("Question")
        if vectorstore is not None and question is not None and question != "":
            docs = vectorstore.similarity_search(question, 5)
            answer = chain.run(input_documents=docs, question=question)
            st.write(answer)

if __name__ == "__main__":
    main()
