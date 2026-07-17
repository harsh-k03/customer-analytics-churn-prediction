import streamlit as st

st.set_page_config(
    page_title="Customer Analytics & Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Analytics & Churn Prediction")

st.markdown("""
Welcome to the **Customer Analytics & Churn Prediction Dashboard**.

This application analyzes customer behavior, predicts churn risk using a machine learning model, and provides business insights to support customer retention strategies.

### Navigate using the sidebar to explore:

- 📊 Customer Analytics
- 🤖 Churn Prediction
- 📈 Model Performance
- 💡 Business Insights
""")

st.info("Select a page from the sidebar to begin.")