from flask import Flask
from PyPDF2 import PdfReader
import os
# send yaml file to openai




app = Flask(__name__)

@app.route('/get_data')
def get_pdf():
    pdfs = os.listdir('data')
    pdf = PdfReader(f'data/{pdfs[0]}')
    raw_text = ''
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text