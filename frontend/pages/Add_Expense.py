import streamlit as st
import httpx

st.title("Add Expense")

amount = st.number_input("Amount")

category = st.selectbox(
    "Category",
    [
        "Food",
        "Travel",
        "Shopping",
        "Bills"
    ]
)

date = st.date_input("Date")

note = st.text_input("Note")

if st.button("Submit"):

    st.success("Expense Added")