from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    """
    Loads PDF and returns raw documents (pages).
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents