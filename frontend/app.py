
import os
import streamlit as st
import sys
import hashlib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from backend.services.rag_service import run_rag_pipeline

st.set_page_config(
    page_title="GenAI Pro - HR Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 S.G.'s GenAI Pro - RAG Document Assistant")

# Backend URL: local during development, deployed URL in production
API_URL = st.secrets.get(
    "API_URL",
    os.getenv("API_URL", "http://127.0.0.1:8000")
).rstrip("/")

# Sidebar: PDF upload
with st.sidebar:
    st.header("Document Setup")
    uploaded_file = st.file_uploader(
        "Upload your Syllabus or Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:
        st.success(f"📂 Loaded: {uploaded_file.name}")
    else:
        st.info("Please upload a PDF document to begin chatting.")

# Persistent chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a question about the document...")

if prompt:
    if not uploaded_file:
        st.error("Please upload a PDF before asking a question!")
    else:
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            with st.spinner("Analyzing your document..."):
                file_bytes = uploaded_file.getvalue()

                file_hash = hashlib.sha256(file_bytes).hexdigest()
                upload_dir = ROOT_DIR / "backend" / "data" / "uploads"
                upload_dir.mkdir(parents=True, exist_ok=True)

                file_path = upload_dir / f"{file_hash}.pdf"

                if not file_path.exists():
                    file_path.write_bytes(file_bytes)

                answer = run_rag_pipeline(
                    str(file_path),
                    prompt
                )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            with st.chat_message("assistant"):
                st.markdown(answer)

        except Exception as e:
            st.error(f"Error: {e}")
