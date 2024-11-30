import os
import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stoggle import stoggle
from streamlit_lottie import st_lottie
from streamlit_3d_viewer import st_3d_viewer  # For 3D elements
import random
import json


# Configure Google Generative AI
os.environ["GOOGLE_API_KEY"] = "AIzaSyCenB10p3CKKiVXqHiEiGTB5JtcNy2aDeM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Streamlit page configuration
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

# CSS for multicolor gradient and crazy styles
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #FF5F6D, #FFC371, #47C9FF, #833AB4, #C13584);
        animation: gradientBG 10s ease infinite;
        color: #fff;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(45deg, #FFC371, #FF5F6D);
        color: white;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, background 0.4s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #833AB4, #C13584);
        transform: scale(1.1);
    }
    .output-box {
        border: 2px solid #47C9FF;
        padding: 15px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        margin-top: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }
    .3d-box {
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3D Object Viewer JSON
cube_data = {
    "vertices": [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1],
    ],
    "faces": [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [0, 3, 7, 4],
        [1, 2, 6, 5],
    ],
}

# Header and interactive title
st.markdown("<h1 style='text-align: center; font-family: Comic Sans MS;'>🌈 AI by Abhinandan 🤖</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px;'>✨ Your friendly chatbot with a splash of creativity! ✨</p>", unsafe_allow_html=True)

# Input box and AI generation
col1, col2 = st.columns([4, 1])
with col1:
    prompt = st.text_input("🌟 Enter your prompt below", placeholder="E.g., 'Write a poem about stars.'")
with col2:
    generate_clicked = st.button("🚀 Generate AI Response")

if generate_clicked:
    if not prompt:
        st.warning("Please enter a prompt to proceed.")
    else:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt, stream=False)
        st.markdown(f"<div class='output-box'><strong>Response:</strong><br>{response.text}</div>", unsafe_allow_html=True)

# Additional Features
col3, col4, col5 = st.columns(3)
with col3:
    urus_clicked = st.button("🏎️ Describe Lamborghini Urus")
with col4:
    story_clicked = st.button("📖 Create a Fun Story")
with col5:
    thanks_clicked = st.button("🙏 Say Thanks to Abhinandan")

if urus_clicked:
    chat = model.start_chat(history=[])
    response1 = chat.send_message("Describe Lamborghini Urus.")
    st.markdown(f"<div class='output-box'><strong>Urus Details:</strong><br>{response1.text}</div>", unsafe_allow_html=True)

if story_clicked:
    chat = model.start_chat(history=[])
    response2 = chat.send_message("Tell a story of a lazy programmer named Abhinandan.")
    st.markdown(f"<div class='output-box'><strong>Story:</strong><br>{response2.text}</div>", unsafe_allow_html=True)

if thanks_clicked:
    chat = model.start_chat(history=[])
    thanks = chat.send_message("Write a formal thank you for Abhinandan for this chatbot.")
    st.markdown(f"<div class='output-box'><strong>Thank You:</strong><br>{thanks.text}</div>", unsafe_allow_html=True)

# Fun Elements Section
st.subheader("🎉 Fun Section")

# Joke Generator
if st.button("😂 Tell me a Joke"):
    chat = model.start_chat(history=[])
    joke_response = chat.send_message("Tell me a joke.")
    st.markdown(f"<div class='output-box'><strong>Joke:</strong><br>{joke_response.text}</div>", unsafe_allow_html=True)

# Inspirational Quote
if st.button("💡 Inspire Me"):
    chat = model.start_chat(history=[])
    quote_response = chat.send_message("Share an inspirational quote.")
    st.markdown(f"<div class='output-box'><strong>Quote:</strong><br>{quote_response.text}</div>", unsafe_allow_html=True)

# 3D Viewer
st.subheader("🌀 Explore in 3D")
st_3d_viewer(cube_data, width=700, height=400)

# Footer
st.write("---")
add_vertical_space(2)
st.markdown(
    """
    <div style="text-align: center; font-size: 16px; color: #FFD700;">
        Created with ❤️ by Abhinandan Parhi
        <br> Connect on 
        <a href="https://www.instagram.com/abhinandan_ap_" target="_blank" style="color: #FF6347;">Instagram</a>,
        <a href="https://github.com/abhinandansgit" target="_blank" style="color: #FF6347;">GitHub</a>, and
        <a href="https://linkedin.com/in/abhinandan-parhi-ap" target="_blank" style="color: #FF6347;">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
