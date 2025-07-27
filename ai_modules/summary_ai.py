import streamlit as st

def run():
    st.subheader("📄 Summary AI")
    text = st.text_area("Enter the text you want to summarize:")
    if text:
        st.success("📝 Summary:\n\nThis is a short summary of your text.")
