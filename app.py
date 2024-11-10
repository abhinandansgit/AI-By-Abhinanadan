
import os
import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stoggle import stoggle
from PIL import Image
import streamlit_lottie as stl
import random

# Set up Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDumCbUhY9MLOcYLbkCn7kiuD5a01Hz6V0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Page Configuration
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

# CSS styling for animations and colors
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
    .main-title {
        font-size: 2.5em;
        color: #FFD700;
        text-shadow: 1px 1px 4px #000;
        animation: pulse 2s infinite;
    }
    .section-title {
        font-size: 1.7em;
        color: #00E0FF;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;'>AI by Abhinandan 🤖</h1>", unsafe_allow_html=True)
st.subheader("Your Friendly AI Chatbot")
st.write("Feel free to ask me anything or explore some fun features below!")
# Prompt Input Area with Placeholder
prompt = st.text_input("Enter your prompt below 👇", placeholder="E.g., 'Caption for Instagram', 'What’s the speciality of India?'")

# Interactive buttons with random background color change on click
def generate_random_color():
    colors = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#1A535C", "#FF6347"]
    return random.choice(colors)

# Define Chatbot Responses and Fun Buttons with color variations
if st.button("Describe Lamborghini Urus", key="urus", help="Get details about Lamborghini Urus"):
    chat = model.start_chat(history=[])
    response1 = chat.send_message("describe Lamborghini Urus.")
    st.write(f"**Response:** {response1.text}")   

if st.button("Create a story of lazy Programmer Abhinandan", key="story", help="A fun story about Abhinandan"):
    chat = model.start_chat(history=[])
    response2 = chat.send_message("Create a story of lazy Programmer Abhinandan")
    st.write(f"**Response:** {response2.text}")  

if st.button("Wish a Thanks to Abhinandan 😊", key="thanks", help="Thank Abhinandan for this chatbot"):
    chat = model.start_chat(history=[])
    thanks = chat.send_message("write a formal one-line thanks to Abhinandan for this AI model")
    st.write(f"You: {thanks.text}")
    st.write("Abhinandan: You're welcome! Follow me on Instagram @abhinandan_ap_")

if st.button("Generate AI Response 🚀", key="generate", help="Get a response based on your input prompt"):
    if not prompt:
        st.warning("Please enter a prompt to proceed.")
    else:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt, stream=False)
        st.write(f"**Response:** {response.text}")

# Add Fun Extras Section with animations
st.subheader("🎉 Some Extra Fun 🎉", anchor="extra")

# Fun Animations for jokes and facts
def display_animated_text(text):
    st.markdown(
        f"""
        <div style="font-size: 1.2em; color: {generate_random_color()}; animation: pulse 2s infinite;">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

# Joke Generator Button
if st.button("Tell me a Joke", key="joke", help="Get a joke to lighten up"):
    chat = model.start_chat(history=[])
    joke_response = chat.send_message("Tell me a funny joke.")
    display_animated_text(f"**Joke:** {joke_response.text}")

# Fact Generator with Toggle Button
with st.expander("Toggle to reveal an interesting fact 🌍"):
    chat = model.start_chat(history=[])
    fact_response = chat.send_message("Tell me an interesting fact.")
    display_animated_text(f"**Fact:** {fact_response.text}")

# Quote of the Day with color-changing text
if st.button("Get an Inspirational Quote 💡", key="quote", help="Find inspiration with a quote"):
    chat = model.start_chat(history=[])
    quote_response = chat.send_message("Share an inspirational quote.")
    display_animated_text(f"**Quote:** {quote_response.text}")

# Easter Egg Toggle Section
st.subheader("🐰 About the Developer")
stoggle("Toggle to reveal a secret about Abhinandan", ("Abhinandan is a lazy programmer 😁", "So he codes only in Python 🐍"))

# Additional Style and Footer with animation
add_vertical_space(3)
st.markdown("-")
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

# Optional: Add interactive elements with color effects and random animations
st.markdown(
    """
    <style>
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)
