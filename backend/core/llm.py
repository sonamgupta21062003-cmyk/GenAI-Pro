
import os
import streamlit as st
from langchain_openai import ChatOpenAI


def get_llm():
    api_key = os.getenv("OPENAI_API_KEY")

    # Read from Streamlit Secrets if the environment variable is not set
    if not api_key:
        try:
            api_key = st.secrets["OPENAI_API_KEY"]
        except (KeyError, FileNotFoundError):
            api_key = None

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to Streamlit Secrets "
            "or your local environment."
        )

    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
        temperature=0.3,
        max_retries=2,
        timeout=60
    )
