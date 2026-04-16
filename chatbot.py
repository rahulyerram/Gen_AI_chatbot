import streamlit as st
from langchain_groq import ChatGroq

st.title("DEBUG MODE")

# 🔍 Force check secrets
st.write("Secrets:", dict(st.secrets))

# 🔴 Hard fail if not present
if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ Secrets NOT loaded at all")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]

st.success("✅ Key loaded")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    groq_api_key=api_key
)

st.write("✅ LLM initialized successfully")
