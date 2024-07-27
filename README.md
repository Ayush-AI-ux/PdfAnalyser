# PDF Analyser

This is a PDF Question Answering App built with Streamlit and Hugging Face's Transformers library. This app allows users to upload PDF files, read their content, and ask questions about the content.

## Features

- Upload multiple PDF files.
- Extract and read text from the uploaded PDFs.
- Ask questions about the content of the PDFs using a question-answering model.
- Get answers to questions based on the content of the PDFs.

## Requirements

- Python 3.6 or higher
- Streamlit
- PyPDF2
- Transformers
- dotenv

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ayush-AI-ux/PdfAnalyser.git
    cd PdfAnalyser
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Hugging Face API key:**

    - Create a `.env` file in the root directory of the project.
    - Add your Hugging Face API key to the `.env` file:

    ```plaintext
    HUGGINGFACE_API_KEY=your_huggingface_api_key
    ```

5. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your web browser. The default address is `http://localhost:8501`.
2. Upload one or more PDF files using the file uploader.
3. Once the PDF content is read, you can ask questions about the content in the text input field.
4. The app will display the answer to your question based on the content of the uploaded PDFs.

## File Structure

- `app.py`: The main application file containing the Streamlit code.
- `requirements.txt`: The list of dependencies required to run the app.
- `.env`: The file containing your Hugging Face API key (not included in the repository).

## Example

Here is a simple example of how the app works:

1. Upload a PDF file containing some text.
2. Enter a question about the content of the PDF.
3. The app will provide an answer based on the content of the uploaded PDF.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
