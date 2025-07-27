import streamlit as st
from ai_modules import cook_ai, summary_ai, code_ai, chatbot_ai

st.set_page_config(layout="wide", page_title="Multi-AI App")

st.sidebar.title("🤖 Choose Your AI Assistant")
choice = st.sidebar.radio("Select Tool:", [
    "🍳 Cook AI",
    "📄 Summary AI",
    "💻 Code AI",
    "💬 Chatbot AI"
])

if choice == "🍳 Cook AI":
    cook_ai.run()
elif choice == "📄 Summary AI":
    summary_ai.run()
elif choice == "💻 Code AI":
    code_ai.run()
elif choice == "💬 Chatbot AI":
    chatbot_ai.run()
