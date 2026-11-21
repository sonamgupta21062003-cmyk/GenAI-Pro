
import hashlib

from backend.core.pdf_loader import load_pdf
from backend.core.chunking import split_documents
from backend.core.embeddings import get_embedding_model
from backend.core.vectorstore import create_vectorstore
from backend.core.llm import get_llm


def run_rag_pipeline(file_path: str, user_question: str):

    # 1. Generate a unique ID based on PDF content
    with open(file_path, "rb") as pdf:
        file_hash = hashlib.sha256(pdf.read()).hexdigest()

    # 2. Load the PDF
    docs = load_pdf(file_path)

    if not docs:
        raise ValueError("No readable content found in the PDF.")

    # 3. Split into chunks
    chunks = split_documents(docs)

    if not chunks:
        raise ValueError("No text chunks were generated.")

    # 4. Load embedding model
    embedding_model = get_embedding_model()

    # 5. Create or load the correct FAISS index
    vectorstore = create_vectorstore(
        chunks,
        embedding_model,
        file_id=file_hash
    )

    # 6. Retrieve relevant document chunks
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    relevant_docs = retriever.invoke(user_question)

    if not relevant_docs:
        return "I could not find relevant information in the uploaded document."

    context = "\n\n".join(
        doc.page_content for doc in relevant_docs
    )

    # 7. Generate grounded answer
    llm = get_llm()

    prompt = f"""
You are an expert HR assistant.

Answer the user's question using only the document context below.
If the answer is not available in the context, clearly say so.
Do not invent information.

Context:
{context}

Question:
{user_question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content
