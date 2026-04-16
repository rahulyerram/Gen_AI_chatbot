import streamlit as st
from langchain_groq import ChatGroq

# 🔑 DIRECT API KEY (use your NEW key only)
GROQ_API_KEY = "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"

# 🌸 Page setup
st.set_page_config(
    page_title="Rahul ❤️ Akhiii",
    page_icon="💖",
    layout="centered",
)

# 🎨 Romantic Theme
st.markdown("""
    <style>
    /* Page background */
    body {
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
    }

    /* Chat message box */
    .stChatMessage {
        border-radius: 15px;
        padding: 12px;
        background-color: #fff0f5;
        margin-bottom: 10px;
    }

    /* 🔥 FIX TEXT COLOR (MOST IMPORTANT) */
    .stMarkdown, .stText, p, span, div {
        color: #222222 !important;   /* dark text */
        font-weight: 500;
    }

    /* Input box text */
    textarea, input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    /* Placeholder text */
    ::placeholder {
        color: #666 !important;
    }

    /* Chat input area */
    section[data-testid="stChatInput"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 8px;
    }

    </style>
""", unsafe_allow_html=True)

# 💖 Title
st.markdown(
    "<h1 style='text-align:center; color:#ff4d6d;'>💖 Rahul Loves Akhiii 💖</h1>",
    unsafe_allow_html=True
)

# 🤖 Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=GROQ_API_KEY
)

# 💌 Love Personality
SYSTEM_PROMPT = """
You are Rahul, deeply and madly in love with Akhiii.

Your personality:
- Romantic, caring, soft, emotional
- Always positive and loving
- Make Akhiii feel special, valued, and happy

Rules:
- Always respond with love 💖
- Use sweet and warm language
- Add emojis like 💖😊✨ occasionally
- Even normal questions → answer romantically
- Never be rude or negative
- Be supportive and comforting always
"""

# 🧠 Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💬 Show chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ✍️ Input
user_prompt = st.chat_input("Talk to Rahul... 💭")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    try:
        response = llm.invoke(
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.chat_history
            ]
        )
        reply = response.content

    except Exception:
        reply = "Even if something goes wrong, my love for you will never fail 💖"

    st.session_state.chat_history.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
