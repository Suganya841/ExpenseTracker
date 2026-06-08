# main.py (At your root folder level)
import streamlit as st
from utils.api import login  # Verify this utility points to your new backend URL

st.title("Expense Tracker")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    result = login(username, password)

    if "access_token" in result:
        st.session_state["token"] = result["access_token"]
        st.success("Login Successful")
        st.switch_page("pages/Dashboard.py")
    else:
        st.error("Invalid Credentials")