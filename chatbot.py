from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# load env (optional, not required now)
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("💬 Generative AI Chatbot")

# ⚠️ Direct API key (TEMPORARY)
GROQ_API_KEY = "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"

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    groq_api_key=GROQ_API_KEY
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    try:
        response = llm.invoke(
            input=[
                {"role": "system", "content": "You are a helpful assistant"},
                *st.session_state.chat_history
            ]
        )
        assistant_response = response.content

    except Exception as e:
        assistant_response = f"❌ Error: {str(e)}"

    # Save response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    # Display response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
