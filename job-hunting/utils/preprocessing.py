import nltk
import os
import textract # can be used for OCR too

from pypdf import PdfReader as pdf_read
from typing import Optional
from nltk.tokenize import word_tokenize

if not nltk.data.find("tokenizers/punkt"):
    nltk.download("punkt")

def extract_text_from_file(file_path: str) -> Optional[str]:
    print(file_path)
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    text = ""

    print(f"File extension: {file_extension}")

    if file_extension == ".pdf":
        with open(file_path, 'rb') as file:
            reader = pdf_read(file)

            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()

    elif file_extension in [".doc", ".docx"]:
        text = textract.process(file_path).decode("utf-8")
    elif file_extension == ".txt":
        with open(file_path) as file:
            text = file.read()
    else:
        print(f"Unsupported file type: {file_extension}")
        return None
    return text