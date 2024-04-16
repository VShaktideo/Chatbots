from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import ssl
from urllib3 import poolmanager

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

##LangsmithTracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="ls__98c78c80ac03401cac5607f16594cb75"
os.environ["LANGCHAIN_PROJECT"]="Chatbot1"

#### Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the queries."),
        ("user","Question={question}")
    ]
)

#### streamlit framework

st.title('LangChain Demo with LLAMA2')
input_text=st.text_input("Search the topic you want")



# Ollama LLAMA2
llm=Ollama(model="llama2",base_url="http://ollama-container:11434", verbose=True)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
