import streamlit as st

def run():
    st.subheader("💬 Chatbot AI")
    user_input = st.text_input("You:")
    if user_input:
        st.success(f"🤖 Bot: You said '{user_input}', cool!")
