from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]="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"
##LangsmithTracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="ls__98c78c80ac03401cac5607f16594cb75"
os.environ["LANGCHAIN_PROJECT"]="ChatbotOpenAI"

#### Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the queries."),
        ("user","Question={question}")
    ]
)

#### streamlit framework

st.title('LangChain Demo with OPENAI API')
input_text=st.text_input("Search the topic you want")


# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
