import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    # Replace the text below with your actual Gemini API Key string
    api_key="AQ.Ab8RN6JHGm2zyKAN0iZjmvuIc0lcBJRsGuV9Eifiqi3OwE3m0A"
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )