# PDF Utility Functions
from pypdf import PdfReader


def read_pdf(file_path: str):
    """
    Read all text from a PDF file.
    """
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text