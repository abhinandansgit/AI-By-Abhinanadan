import os
import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stoggle import stoggle
from PIL import Image
import streamlit_lottie as stl
import random


os.environ["GOOGLE_API_KEY"] = "AIzaSyDumCbUhY9MLOcYLbkCn7kiuD5a01Hz6V0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')


st.set_page_config(
    page_title="AI by Abhinandan",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://www.instagram.com/abhinandan_ap_/#",
        "Report a bug": "https://www.instagram.com/abhinandan_ap_/#",
        "About": "A fun and interactive AI chatbot by Abhinandan."
    }
)


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #8E2DE2, #4A00E0);
        color: #fff;
    }
    .stButton > button {
        border-radius: 8px;
        background-color: #FF0080;
        color: #fff;
        font-weight: bold;
        transition: 0.4s ease;
    }
    .stButton > button:hover {
        background-color: #4A00E0;
        transform: scale(1.1);
    }
    .generate-btn > button {
        background-color: #FFD700 !important;
        color: #000 !important;
        font-weight: bold;
    }
    .output-box {
        border: 1px solid #FFD700;
        padding: 15px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;'>AI by Abhinandan 🤖</h1>", unsafe_allow_html=True)
st.subheader("Your Friendly AI Chatbot")
st.write("Feel free to ask me anything or explore some fun features below!")

def get_response_with_error_handling(prompt_text):
    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt_text, stream=False)
        return response.text
    except Exception as e:
        st.warning("The content may violate certain terms. Please try a different prompt.")
        return None
col1, col2 = st.columns([4, 1])
with col1:
    prompt = st.text_input("Enter your prompt below 👇", placeholder="E.g., 'Caption for Instagram', 'What’s the specialty of India?'")
with col2:
    generate_clicked = st.button("Generate AI Response 🚀", key="generate", help="Get a response based on your input prompt", 
                                 type="primary", use_container_width=True)
if generate_clicked:
    if not prompt:
        st.warning("Please enter a prompt to proceed.")
    else:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt, stream=False)
        st.markdown("<div class='output-box'><strong>Response:</strong><br>" + response.text + "</div>", unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)
with col3:
    urus_clicked = st.button("Describe Lamborghini Urus", key="urus", help="Get details about Lamborghini Urus")
with col4:
    story_clicked = st.button("Create a Story of Lazy Programmer Abhinandan", key="story", help="A fun story about Abhinandan")
with col5:
 if st.button("Wish Thanks to Abhinandan 😊", key="thanks", help="Thank Abhinandan for this chatbot"):
        chat = model.start_chat(history=[])
        thanks = chat.send_message("Write a formal one-line thanks to Abhinandan for this AI model")
        st.write(f"You: {thanks.text}")
        st.write("Abhinandan: You're welcome! Follow me on Instagram @abhinandan_ap_")
if urus_clicked:
    chat = model.start_chat(history=[])
    response1 = chat.send_message("Describe Lamborghini Urus.")
    st.markdown(f"<div class='output-box'><strong>Response:</strong><br>{response1.text}</div>", unsafe_allow_html=True)
if story_clicked:
    chat = model.start_chat(history=[])
    response2 = chat.send_message("Create a story of lazy Programmer Abhinandan")
    st.markdown(f"<div class='output-box'><strong>Story:</strong><br>{response2.text}</div>", unsafe_allow_html=True)
st.subheader(" Some Extra Fun 😁", anchor="extra")
if st.button("Tell me a Joke", key="joke", help="Get a joke to lighten up"):
    chat = model.start_chat(history=[])
    joke_response = chat.send_message("Tell me a funny joke.")
    st.markdown(f"<div class='output-box'><strong>Joke:</strong><br>{joke_response.text}</div>", unsafe_allow_html=True)
with st.expander("Toggle to reveal an interesting fact 🌍"):
    chat = model.start_chat(history=[])
    fact_response = chat.send_message("Tell me a random interesting fact.")
    st.markdown(f"<div class='output-box'><strong>Fact:</strong><br>{fact_response.text}</div>", unsafe_allow_html=True)
if st.button("Get an Inspirational Quote 💡", key="quote", help="Find inspiration with a quote"):
    chat = model.start_chat(history=[])
    quote_response = chat.send_message("Share an inspirational quote.")
    st.markdown(f"<div class='output-box'><strong>Quote:</strong><br>{quote_response.text}</div>", unsafe_allow_html=True)
st.subheader("🐰 About the Developer")
stoggle("Toggle to reveal a secret about Abhinandan", ("Abhinandan is a lazy programmer 😁", "So he codes only in Python 🐍"))
st.write("---")
add_vertical_space(3)
st.markdown(
    """
    <div style="text-align: center; color: #FFD700; animation: pulse 2s infinite;">
        👨‍💻 Made by Abhinandan Parhi | Connect on 
        <a href="https://www.instagram.com/abhinandan_ap_" target="_blank" style="color: #FF6347;">Instagram</a>, 
        <a href="https://in.linkedin.com/in/abhinandan-parhi-ap" target="_blank" style="color: #FF6347;">LinkedIn</a>, 
        <a href="https://github.com/abhinandansgit" target="_blank" style="color: #FF6347;">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
