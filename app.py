import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

st.title("PDF Question Answering App")

st.write("Upload a PDF file and ask questions about its content.")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    pdf_text = get_pdf_text(uploaded_files)
    
    st.write("PDF content has been successfully read.")

    question = st.text_input("Ask a question about the PDF content:")
    
    if question: 
        question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2", use_auth_token=huggingface_api_key)
        
        response = question_answerer(question=question, context=pdf_text)
        
        st.write("Answer:", response['answer'])