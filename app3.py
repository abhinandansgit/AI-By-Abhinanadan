import os
import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

# Secure API key storage (e.g., environment variable or secrets manager)
api_key = os.getenv("AIzaSyDumCbUhY9MLOcYLbkCn7kiuD5a01Hz6V0")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

st.title("AI by Abhinandan")

st.header("Ask me anything:")

prompt = st.text_input("")

if st.button("Generate Response"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            try:
                chat = model.start_chat(history=[])
                response = chat.send_message(prompt, stream=False)
                translated_response = GoogleTranslator(source='auto', target='hi').translate(response.text)
                st.write(translated_response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")