# Q&A Chatbot
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import utils

load_dotenv()
Img = utils.Image()
PageStyle = utils.PageStyle()

# Setting background and sidebar images
bg_img = Img.get_bg_img('images/bgimg.png')

# Setting up the page style
page_style = PageStyle.page_style(bg_img)
st.markdown(page_style, unsafe_allow_html=True)

# initialise the streamlit app
st.title("Q&A Chatbot")

davinci_model = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),
                model_name="text-davinci-003",
                temperature=0.6)

gpt3_turbo_model = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),
                model_name="gpt-3.5-turbo-instruct",
                temperature=0.6)

babbage_model = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),
                model_name="babbage-002",
                temperature=0.6)

text_curie_model = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"),
                model_name="text-curie-001",
                temperature=0.6)

def get_openai_response(question, model_name):
    if model_name == "babbage-002":
        try:
            response = babbage_model(question)
        except:
            response = "Rate limit exceeded. Please wait for 30 seconds and try again."
    elif model_name == "gpt-3.5-turbo":
        try:
            response = gpt3_turbo_model(question)
        except:
            response = "Rate limit exceeded. Please wait for 30 seconds and try again."
    elif model_name == "text-curie":
        try:
            response = text_curie_model(question)
        except:
            response = "Rate limit exceeded. Please wait for 30 seconds and try again."
    else:
        try:
            response = davinci_model(question)
        except:
            response = "Rate limit exceeded. Please wait for 30 seconds and try again."

    return response


input = st.text_input("Input: ", key="input")

option = st.selectbox(
    'Choose your model to ask the question:',
    ('davinci', 'gpt-3.5-turbo', 'babbage-002','text-curie'))

submit = st.button("Ask")

if submit:
    response = get_openai_response(input, option)
    st.subheader("Response: ")
    st.write(response)