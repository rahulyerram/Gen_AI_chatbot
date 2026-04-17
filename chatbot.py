import streamlit as st
from langchain_groq import ChatGroq
import time

# 🔑 API KEY (use your NEW key)
GROQ_API_KEY = "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"

# Page setup
st.set_page_config(
    page_title="Rahul Chat",
    page_icon="💬",
    layout="centered",
)

st.title("Rahul 💬")

# 🎨 Clean UI (mobile friendly)
st.markdown("""
<style>
.stChatMessage {
    background-color: #f5f5f5;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 8px;
}
.stMarkdown, p, span, div {
    color: #222 !important;
}
</style>
""", unsafe_allow_html=True)

# 🤖 LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=GROQ_API_KEY
)

# 🧠 HUMAN-LIKE PROMPT
SYSTEM_PROMPT = """
You are Rahul, talking to Akhiii.

Speak like a real human.

Rules:
- Natural, simple, and warm
- Keep responses short to medium
- Don't sound like AI
- Don't overuse emojis
- Be caring and genuine

Behavior:
- If she is sad → comfort her
- If she is happy → respond warmly
- If normal question → answer normally but with warmth
"""

# 🧠 Memory (session-based)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
user_prompt = st.chat_input("Talk to Rahul...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_prompt
    })

    # ⏳ Typing effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Rahul is typing... ⏳")

        try:
            response = llm.invoke(
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.chat_history
                ]
            )

            full_response = response.content

        except Exception:
            full_response = "Hmm... something went wrong, but I'm still here with you."

        # ✨ Simulate typing (character by character)
        typed_text = ""
        for char in full_response:
            typed_text += char
            message_placeholder.markdown(typed_text)
            time.sleep(0.01)

    # Save response (memory)
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": full_response
    })
