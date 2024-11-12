from PIL import Image
import io
import streamlit as st

image = Image.open("Rocket.gif")
resized_image = image.resize((100, 100))

image_bytes = io.BytesIO()
resized_image.save(image_bytes, format='GIF')

st.markdown('<div class="header">', unsafe_allow_html=True)

st.image(image_bytes, format='GIF')
st.markdown('</div>', unsafe_allow_html=True)

st.write("Feel free to ask me anything or explore some fun features below!")
