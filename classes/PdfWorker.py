from PyPDF2 import PdfFileReader


class PdfWorker:
    @staticmethod
    def get_pdf_text(filename: str):
        pdf = PdfFileReader(filename)
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extractText()
        return pdf_text
