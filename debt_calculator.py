import pandas as pd
import calendar

def calculate_new_duration(debt, extra_savings_per_month):
    total_remaining = debt["monthly_payment"] * debt["remaining_months"]
    additional_payment = extra_savings_per_month
    return round(total_remaining / (debt["monthly_payment"] + additional_payment), 2)

def generate_financial_insight(debts, savings_per_month, duration_months):
    data = []
    total_savings = 0
    remaining_debts = {
        debt_id: debt["monthly_payment"] * debt["remaining_months"]
        for debt_id, debt in debts.items()
    }

    for month in range(1, duration_months + 1):
        total_savings += savings_per_month
        payments = {}

        for debt_id, remaining in remaining_debts.items():
            payment = min(debts[debt_id]["monthly_payment"], remaining)
            remaining_debts[debt_id] -= payment
            payments[debt_id] = payment

        year = 2025 + (month - 1) // 12
        month_name = calendar.month_abbr[(month - 1) % 12 + 1]
        formatted_month = f"{month_name}-{str(year)[-2:]}"

        data.append({
            "Month": formatted_month,
            "Total Savings": total_savings,
            **{f"Remaining Debt {debt_id}": remaining for debt_id, remaining in remaining_debts.items()},
            **{f"Payment to Debt {debt_id}": payment for debt_id, payment in payments.items()},
        })

    return pd.DataFrame(data)
