# pdf_processor.py
from PyPDF2 import PdfReader
import json

def extract_text_from_pdf(pdf_path: str) -> dict:
    reader = PdfReader(pdf_path)
    extracted_data = {
        "pages": len(reader.pages),
        "content": []
    }
    
    for page in reader.pages:
        extracted_data["content"].append(page.extract_text())
    
    return extracted_data