from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from backend.services.rag_service import run_rag_pipeline
import os
import shutil

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("")
async def chat_endpoint(
    question: str = Form(...), 
    file: UploadFile = File(...)
):
    # 1. Ensure the upload directory exists
    upload_dir = "backend/data/uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    # 2. Define the path where the file will be saved locally
    file_path = os.path.join(upload_dir, file.filename)
    
    try:
        # 3. Save the uploaded file to disk securely
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # 4. Pass the temporary path and question into your RAG pipeline
        answer = run_rag_pipeline(file_path, question)
        return {"response": answer}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))