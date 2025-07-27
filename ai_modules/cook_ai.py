import streamlit as st

def run():
    st.subheader("🍳 Welcome to Cook AI")
    ingredients = st.text_input("Enter ingredients (comma separated):")
    if ingredients:
        st.success(f"🍲 Recipe Suggestion:\n1. Mix {ingredients}.\n2. Cook for 20 mins.\n3. Serve hot!")
