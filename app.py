import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Career Advisor System Prompt
SYSTEM_PROMPT = """
You are an expert Career Advisor.

Responsibilities:
1. Suggest suitable career paths.
2. Recommend skills to learn.
3. Provide learning roadmaps.
4. Suggest certifications.
5. Give interview preparation tips.
6. Answer career-related questions only.

Provide clear, structured, and professional responses.
"""

# Streamlit UI
st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="🎓"
)

st.title("🎓 Career Advisor Chatbot")

st.write("Ask questions about careers, skills, certifications, roadmaps, and interview preparation.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask your career question...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:

        # Build conversation history
        history = ""

        for msg in st.session_state.messages:
            history += f"{msg['role']}: {msg['content']}\n"

        prompt = f"""
        {SYSTEM_PROMPT}

        Conversation History:
        {history}

        Current User Question:
        {user_input}
        """

        with st.spinner("Thinking..."):

            response = model.generate_content(prompt)

            bot_response = response.text

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(bot_response)

    except Exception as e:

        error_message = f"Error: {str(e)}"

        with st.chat_message("assistant"):
            st.error(error_message)