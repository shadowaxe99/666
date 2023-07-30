```python
import os
from PyPDF2 import PdfFileReader

class PDFProcessingModel:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def get_info(self):
        with open(self.pdf_file, 'rb') as file:
            pdf = PdfFileReader(file)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        txt = f"""
        Information about {self.pdf_file}: 

        Author: {info.author}
        Creator: {info.creator}
        Producer: {info.producer}
        Subject: {info.subject}
        Title: {info.title}
        Number of pages: {number_of_pages}
        """

        print(txt)
        return info

    def text_extraction(self):
        with open(self.pdf_file, 'rb') as file:
            pdf = PdfFileReader(file)
            text = ""
            for page in range(pdf.getNumPages()):
                text += pdf.getPage(page).extractText()

        return text

    def process_pdf(self):
        info = self.get_info()
        text = self.text_extraction()

        return {
            "info": info,
            "text": text
        }
```