import streamlit as st
import pandas as pd
from pathlib import Path
import joblib

st.set_page_config(
    page_title="Customer Analytics & Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset & Model
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "telco_customer_churn_clean.csv"
)

joblib.load(
    BASE_DIR / "models" / "best_random_forest.pkl"
)

accuracy = 0.7903

total_customers = len(df)
churn_rate = (df["Churn"] == "Yes").mean() * 100

# -----------------------------
# Header
# -----------------------------
st.title("📊 Customer Analytics & Churn Prediction")

st.markdown(
    """
An interactive machine learning dashboard that predicts customer churn,
compares multiple classification models, and deploys an optimized
Random Forest model for inference.
"""
)

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "📉 Churn Rate",
        f"{churn_rate:.1f}%"
    )

with col3:
    st.metric(
    "🤖 Deployed Model Accuracy",
    f"{accuracy*100:.2f}%"
)

st.divider()

# -----------------------------
# Main Content
# -----------------------------
left, right = st.columns([1, 1])

with left:

    st.subheader("📌 Project Overview")

    st.write("""
The dashboard combines exploratory data analysis, machine learning model
comparison, hyperparameter optimization, customer-level churn prediction,
and business insights to help identify high-risk customers and support
retention strategies.
""")

with right:

    st.subheader("🚀 Dashboard Pages")

    st.markdown("""
- 📊 **Analytics** – Explore customer demographics and churn trends.

- 🤖 **Prediction** – Predict churn for individual customers.

- 📈 **Model Performance** – Compare machine learning models.

- 💡 **Business Insights** – View KPIs, charts, and business recommendations.
""")

st.divider()

st.caption("👈 Use the sidebar to navigate through the dashboard.")