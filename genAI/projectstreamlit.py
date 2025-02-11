import streamlit as st
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key = "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"
)


st.title("Simple LLM chatbot")
st.write("Enter your query")

user_input = st.text_input("Your question:","")

if st.button("Get answer"):
    response = llm.invoke(user_input)
    st.write("### RESPONSE:")
    st.write(response.content)