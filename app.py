import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPEN_AI_KEY']

def chatbot(query):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=1000
    )
    return response.choices[0].text

st.title('Chatbot')
st.write('Type a message and press Enter to chat with the bot!')
msg = st.text_input('You', value='', key='msg_input')
if msg:
    bot_response = chatbot(msg)
    st.text_area('Bot', value=bot_response, height=200, key='bot_response')

