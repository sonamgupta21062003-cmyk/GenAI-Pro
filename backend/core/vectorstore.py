import os
from langchain_community.vectorstores import FAISS

# Define a central directory where vectors will be stored permanently
DB_DIR = "backend/data/vector_db"

def create_vectorstore(chunks, embedding_model, file_id: str):
    """
    Saves or loads a FAISS vector index locally to prevent re-embedding.
    """
    # Create a unique path for this specific file
    store_path = os.path.join(DB_DIR, file_id)
    
    # Check if this PDF has already been processed and saved
    if os.path.exists(store_path):
        print(f"--> Found existing vector database at {store_path}. Loading instantly...")
        return FAISS.load_local(store_path, embedding_model, allow_dangerous_deserialization=True)
    
    # If it's a new file, create the vector store from scratch
    print(f"--> Creating a fresh vector store at {store_path}...")
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    
    # Save it to disk so we have it next time
    os.makedirs(DB_DIR, exist_ok=True)
    vectorstore.save_local(store_path)
    
    return vectorstore