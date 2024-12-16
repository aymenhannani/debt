import streamlit as st
from debt_calculator import generate_financial_insight

st.title("Debt Calculation WebApp")

# User inputs for debts
st.sidebar.header("Debts")
num_debts = st.sidebar.number_input("Number of Debts", min_value=1, value=2, step=1)

debts = {}
for i in range(1, num_debts + 1):
    st.sidebar.subheader(f"Debt {i}")
    monthly_payment = st.sidebar.number_input(f"Monthly Payment (Debt {i})", min_value=0, value=1000, step=100)
    remaining_months = st.sidebar.number_input(f"Remaining Months (Debt {i})", min_value=1, value=12, step=1)
    debts[i] = {"monthly_payment": monthly_payment, "remaining_months": remaining_months}

# Savings inputs
savings_per_month = st.sidebar.number_input("Monthly Savings", min_value=0, value=2000, step=100)
duration_months = st.sidebar.slider("Duration to Calculate (Months)", min_value=12, max_value=60, value=36)

# Generate financial insights
financial_insight_df = generate_financial_insight(debts, savings_per_month, duration_months)

st.subheader("Debt Repayment Insights")
st.dataframe(financial_insight_df)

st.subheader("Summary")
remaining_debt_summary = financial_insight_df.iloc[-1][[col for col in financial_insight_df.columns if "Remaining Debt" in col]]
st.write("Remaining Debt at End of Period:")
st.write(remaining_debt_summary)
