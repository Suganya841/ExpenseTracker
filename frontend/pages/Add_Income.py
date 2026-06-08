import streamlit as st

st.title("Add Income")

amount = st.number_input("Amount")

source = st.text_input("Source")

date = st.date_input("Date")

if st.button("Submit"):
    st.success("Income Added")