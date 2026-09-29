import streamlit as st
st.title("LATTA's company")
st.header("Welcome to my  new  company")
st.write("hello", "LATTA")
name = st.text_input("Enter your name")  
if st.button("submit"):
    st.write(" yeahh !now you can fill your details")
gender = st.radio("select your gender",["Male","Female"])
chat = st.chat_input("enter your message")