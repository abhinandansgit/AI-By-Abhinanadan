import os
import streamlit as st
import google.generativeai as genai
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stoggle import stoggle
from PIL import Image

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

# Main Title and Header
st.title("AI by Abhinandan 🤖")
st.subheader("Your Friendly AI Chatbot")
st.write("Feel free to ask me anything or explore some fun features below!")

# Add an introductory GIF for visual appeal
intro_image = Image.open("ap\loding_animation.gif")
st.image(intro_image, caption="Let's chat and have some fun!", use_column_width=True)

# Prompt Input Area with Placeholder
prompt = st.text_input("Enter your prompt below 👇", placeholder="E.g., 'Tell me a joke', 'What’s the weather?'")

# Define Chatbot Responses and Fun Buttons
st.button("Ask About Today's Weather 🌤️")    
st.button("Get a Robot Poem 🤖💔")
if st.button("Say Thanks to Abhinandan 🙏"):
    st.write("You're welcome! Follow me on Instagram @abhinandan_ap_")

if st.button("Generate AI Response 🚀"):
    if not prompt:
        st.warning("Please enter a prompt to proceed.")
    else:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt, stream=False)
        st.write(f"**Response:** {response.text}")

# Add Fun Extras Section with Toggle Info
st.subheader("🎉 Extra Fun Features 🎉")

# Joke Generator Button
if st.button("Tell me a Joke"):
    joke_response = chat.send_message("Tell me a funny joke.")
    st.write(f"**Joke:** {joke_response.text}")

# Fact Generator with Toggle Button
with st.expander("Toggle to reveal an interesting fact 🌍"):
    fact_response = chat.send_message("Tell me an interesting fact.")
    st.write(f"**Fact:** {fact_response.text}")

# Quote of the Day
if st.button("Get an Inspirational Quote 💡"):
    quote_response = chat.send_message("Share an inspirational quote.")
    st.write(f"**Quote:** {quote_response.text}")

# Easter Egg Toggle Section
st.subheader("🐰 Easter Egg!")
stoggle("Toggle to reveal a secret message", "Congrats, you've found the Easter Egg! 🎉")

# Sidebar for Quick Navigation and More Options
st.sidebar.title("🔍 Explore More")
st.sidebar.button("Motivational Quotes")
st.sidebar.button("Fun Facts")
st.sidebar.write("Need help? Visit the [Support Page](https://www.instagram.com/abhinandan_ap_/#)")

# Additional Style and Footer
add_vertical_space(3)
st.write("---")
st.write("👨‍💻 Made by Abhinandan | Connect on [Instagram](https://www.instagram.com/abhinandan_ap_)")

# Optional: Add background image or color scheme
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .stButton > button {
        border-radius: 5px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
