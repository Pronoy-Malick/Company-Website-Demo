import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.set_page_config(layout="wide")

st.title("Contact us")

with st.form("my"):
    user_email = st.text_input("Enter Your Email Address", placeholder="Ex:- User@gmail.com")
    user_choice = st.selectbox('What Topic you want to discuss?', df["topic"])
    raw_user_message = st.text_area("Enter your Message",placeholder="Ask your questions or your thoughts.")
    user_message = f"""\
Subject: Someone with {user_email} is trying to contact you
    
Topic- {user_choice}
{raw_user_message}
From: {user_email}
"""
    submit = st.form_submit_button("Submit")

    if submit:
        send_email(user_message)
        st.info("Your Email sent sucessfully!...")

