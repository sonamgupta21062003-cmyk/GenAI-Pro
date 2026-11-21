
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    api_key = st.secrets["GOOGLE_API_KEY"]

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )
