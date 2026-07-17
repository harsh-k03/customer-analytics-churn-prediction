import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights")

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "processed" / "telco_customer_churn_clean.csv"

df = pd.read_csv(DATA_PATH)

df["Churn_Flag"] = df["Churn"].map({"No": 0, "Yes": 1})

st.subheader("Key Business Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    churn_rate = df["Churn_Flag"].mean() * 100
    st.metric("Overall Churn Rate", f"{churn_rate:.2f}%")

with col2:
    avg_tenure = df["tenure"].mean()
    st.metric("Average Customer Tenure", f"{avg_tenure:.1f} Months")

with col3:
    avg_monthly = df["MonthlyCharges"].mean()
    st.metric("Average Monthly Charges", f"${avg_monthly:.2f}")

st.divider()

st.subheader("Churn by Contract Type")

contract = (
    df.groupby("Contract")["Churn_Flag"]
    .mean()
    .reset_index()
)

contract["Churn_Flag"] *= 100

fig = px.bar(
    contract,
    x="Contract",
    y="Churn_Flag",
    color="Contract",
    text="Churn_Flag",
    title="Churn Rate by Contract Type"
)

fig.update_traces(texttemplate="%{text:.1f}%")
fig.update_layout(
    showlegend=False,
    yaxis_title="Churn Rate (%)"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Churn by Internet Service")

internet = (
    df.groupby("InternetService")["Churn_Flag"]
    .mean()
    .reset_index()
)

internet["Churn_Flag"] *= 100

fig = px.bar(
    internet,
    x="InternetService",
    y="Churn_Flag",
    color="InternetService",
    text="Churn_Flag",
    title="Churn Rate by Internet Service"
)

fig.update_traces(texttemplate="%{text:.1f}%")
fig.update_layout(
    showlegend=False,
    yaxis_title="Churn Rate (%)"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Business Recommendations")

st.success("""
### Recommended Actions

- Convert month-to-month customers to long-term contracts.
- Target Fiber Optic customers with loyalty offers.
- Improve customer support for high-risk customers.
- Provide discounts for customers with high monthly charges.
- Launch retention campaigns for customers in their first year.
""")

st.info("""
### Key Findings

- Month-to-month customers show the highest churn.
- Fiber optic customers churn more frequently.
- Customers paying higher monthly charges are more likely to leave.
- Longer-tenure customers are significantly more loyal.
""")