import streamlit as st
import requests

st.set_page_config(
    page_title="GenAI Pro - HR Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 S.G.'s GenAI Pro - RAG Document Assistant")

# 1. Add a sidebar layout for file uploading
with st.sidebar:
    st.header("Document Setup")
    uploaded_file = st.file_uploader("Upload your Syllabus or Resume (PDF)", type=["pdf"])
    if uploaded_file:
        st.success(f"📂 Loaded: {uploaded_file.name}")
    else:
        st.info("Please upload a PDF document to begin chatting.")

# Initialize session state for persistent chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation chunks
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input box
prompt = st.chat_input("Ask a question about the document...")

if prompt:
    # Stop processing if the user forgot to attach a file
    if not uploaded_file:
        st.error("⚠️ Please upload a PDF file in the sidebar before asking a question!")
    else:
        # Append and display user's message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Analyzing document and querying Gemini..."):
            try:
                # 2. FIXED: Prepare multipart/form-data payload for FastAPI
                # Read the file data into memory bytes
                file_bytes = uploaded_file.getvalue()
                
                payload_files = {
                    "file": (uploaded_file.name, file_bytes, "application/pdf")
                }
                payload_data = {
                    "question": prompt
                }

                # Send the POST request utilizing 'files' and 'data' instead of 'json'
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    data=payload_data,
                    files=payload_files
                )
                
                if response.status_code == 200:
                    # 3. FIXED: Extract using ["response"] to match your backend dictionary key
                    answer = response.json()["response"]
                    
                    # Append and display the LLM response
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    with st.chat_message("assistant"):
                        st.markdown(answer)
                else:
                    st.error(f"Backend Error ({response.status_code}): {response.text}")
                    
            except Exception as e:
                st.error(f"Failed to connect to backend server: {str(e)}")