import os
import streamlit as st
import google.generativeai as genai

# Set up API key and configure the model
os.environ["GOOGLE_API_KEY"] = "AIzaSyDumCbUhY9MLOcYLbkCn7kiuD5a01Hz6V0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

# Create the Streamlit app
st.title("AI by Abhinandan")

# Add a descriptive header
st.header("Ask me anything:")

# Create a text input for user's prompt
prompt = st.text_input("")

# Add suggestion buttons
st.button("What is the weather today?")
st.button("Write a poem about a lonely robot")
st.button("Translate 'Hello, how are you?' to Spanish")

if st.button("Generate Response"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt, stream=False)
        st.write(response.text)
