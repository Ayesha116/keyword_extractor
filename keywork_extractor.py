#import essential libraries
from openai import OpenAI
import streamlit as st

#declaring openai variable
client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

#set page title
st.title('Keyword Extractor using openai')

#Api call inside a funtion to perform keyword extraction
def keyword_extractor(text):
    messages = [{'role':'system', "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."},
                {'role':"user", "content":f'{text}'}]
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=100
    )
    response_text = response.choices[0].message.content
    return response_text

#takig user input and perform operation on text
user_text = st.text_input('Input text')
button_clicked = st.button('submit')

#display output
if button_clicked:
    st.write(keyword_extractor(user_text))


