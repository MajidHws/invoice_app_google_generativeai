from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

input_prompt = """
your are an expert in understanding invoice. you will 
receive images as invoices and you will have to
answer questions based on the input image
"""

st.write("""
# My Invoice OCR
This is a simple OCR app to extract text from invoice records
""")

# add an input
input = st.text_input("Your prompt", key="input")
# add image picker 
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
#check if image is uploaded, display it

# number = st.slider("Pick a number", 0, 100)
# st.write(f"You picked {number}")


def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()
        image_parts = [{
            "mime_type": upload_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise Exception("No image uploaded")

# create a function that will take input, image and prompt then call genai.generativeModel
def get_gemini_response(input, image, prompt):
    # model = genai.GenerativeModel('gemini-pro-vision')
    # response = model.generative_content([input, image[0], prompt])
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# add a button
if st.button("Send"):
    with st.spinner('Waiting for response...'):
        # model = genai.GenerativeModel('gemini-1.5-flash')
        # response = model.generate_content("The opposite of hot is")
        image_data = input_image_setup(uploaded_image)
        response = get_gemini_response(input, image_data, input_prompt)
        st.write(f"Response: {response}")


image = ""

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded image", use_container_width=True)
    # st.write("Done!")