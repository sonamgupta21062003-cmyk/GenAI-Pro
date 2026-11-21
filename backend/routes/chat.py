
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from backend.services.rag_service import run_rag_pipeline
from pathlib import Path
import os
import shutil
import uuid

router = APIRouter(prefix="/chat", tags=["Chat"])

UPLOAD_DIR = Path("backend/data/uploads")


@router.post("")
async def chat_endpoint(
    question: str = Form(...),
    file: UploadFile = File(...)
):
    if not file.filename or Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / f"{uuid.uuid4().hex}.pdf"

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        answer = run_rag_pipeline(str(file_path), question)

        return {"response": answer}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"RAG processing failed: {str(e)}"
        )

    finally:
        await file.close()
