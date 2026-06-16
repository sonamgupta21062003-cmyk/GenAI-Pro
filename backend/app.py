from fastapi import FastAPI
from backend.routes.chat import router as chat_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="S.G.'s GenAI RAG Chatbot",
    description="PDF Q&A chatbot using RAG + Gemini",
    version="1.0"
)

# include routes
app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "RAG Chatbot API is running 🚀"}