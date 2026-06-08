import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("Dashboard")

if st.sidebar.button("Logout"):
    del st.session_state["token"]
    st.switch_page("app.py")

# Month Filter
month = st.selectbox(
    "Select Month",
    ["January", "February", "March", "April"]
)

st.write("Selected Month:", month)

# Month Mapping
month_num = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# Fetch Summary Data from FastAPI
try:
    response = requests.get(
        f"http://127.0.0.1:8000/summary?month={month_num[month]}"
    )

    if response.status_code == 200:
        data = response.json()

        total_income = data.get("total_income", 0)
        total_expense = data.get("total_expense", 0)
        savings = data.get("savings", 0)

    else:
        total_income = 0
        total_expense = 0
        savings = 0

except Exception:
    total_income = 0
    total_expense = 0
    savings = 0

# Summary Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Income", f"₹{total_income}")

with col2:
    st.metric("Total Expenses", f"₹{total_expense}")

with col3:
    st.metric("Savings", f"₹{savings}")

# Expense Pie Chart
st.subheader("Expense Distribution")

expense_data = {
    "category": ["Food", "Transport", "Bills", "Shopping"],
    "amount": [10000, 5000, 7000, 3000]
}

expense_df = pd.DataFrame(expense_data)

fig1 = px.pie(
    expense_df,
    names="category",
    values="amount",
    title="Expenses by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# Income vs Expense Bar Chart
st.subheader("Income vs Expense")

summary_data = {
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "income": [50000, 55000, 60000, 58000],
    "expense": [25000, 30000, 28000, 32000]
}

summary_df = pd.DataFrame(summary_data)

fig2 = px.bar(
    summary_df,
    x="month",
    y=["income", "expense"],
    barmode="group",
    title="Monthly Income vs Expense"
)

st.plotly_chart(fig2, use_container_width=True)