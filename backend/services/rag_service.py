# RAG Pipeline
#PDF → Text → Chunking → Embeddings → Vector DB → LLM → Answer
from backend.core.pdf_loader import load_pdf
from backend.core.chunking import split_documents
from backend.core.embeddings import get_embedding_model
from backend.core.vectorstore import create_vectorstore
from backend.core.llm import get_llm
import os

def run_rag_pipeline(file_path: str, user_question: str):
    """
    Executes the complete RAG loop on demand when a user asks a question.
    """
    # Create a unique ID using the name of the file (e.g., 'resume.pdf')
    file_id = os.path.basename(file_path)
    # 1. Load the PDF documents dynamically
    docs = load_pdf(file_path)
    
    # 2. Break them into manageable chunks
    chunks = split_documents(docs)
    
    # 3. Initialize your embedding model 
    embedding_model = get_embedding_model()
    
    # 4. Generate vectors and store them in FAISS
    vectorstore = create_vectorstore(chunks, embedding_model,file_id=file_id)
    
    # 5. Retrieve relevant chunks based on user query
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # FIXED: Changed from retriever.get_relevant_documents to retriever.invoke
    relevant_docs = retriever.invoke(user_question)
    
    # Combine retrieved text context
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    
    # 6. Initialize your LLM model (Gemini-1.5-flash)
    llm = get_llm()
    
    # Construct your engineering prompt
    prompt = f"""
    You are an expert HR assistant. Answer the user's question using only the context provided below.
    If you do not know the answer based on the context, say that you cannot find it.
    
    Context:
    {context}
    
    Question: {user_question}
    Answer:
    """
    
    # 7. Query the model and return response text
    # (Since ChatGoogleGenerativeAI follows LangChain's interface, use invoke)
    response = llm.invoke(prompt)
    return response.content