import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="📊",
    layout="wide"
)

COLOR_PALETTE = [
    "#4F46E5",
    "#06B6D4",
    "#10B981",
    "#F59E0B"
]

st.title("📊 Customer Analytics")

st.markdown("""
Explore customer demographics, service usage and churn behaviour through
interactive visualizations.
""")

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "processed" / "telco_customer_churn_clean.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["gender"].unique()),
    default=sorted(df["gender"].unique())
)

contract_filter = st.sidebar.multiselect(
    "Contract",
    options=sorted(df["Contract"].unique()),
    default=sorted(df["Contract"].unique())
)

internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=sorted(df["InternetService"].unique()),
    default=sorted(df["InternetService"].unique())
)

senior_filter = st.sidebar.multiselect(
    "Senior Citizen",
    options=sorted(df["SeniorCitizen"].unique()),
    default=sorted(df["SeniorCitizen"].unique())
)

filtered_df = df[
    (df["gender"].isin(gender_filter))
    & (df["Contract"].isin(contract_filter))
    & (df["InternetService"].isin(internet_filter))
    & (df["SeniorCitizen"].isin(senior_filter))
]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

st.subheader("Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        "Total Customers",
        f"{len(filtered_df):,}"
    )

with kpi2:
    churn_rate = (
        filtered_df["Churn"]
        .value_counts(normalize=True)
        .get("Yes", 0)
        * 100
    )

    st.metric(
        "Churn Rate",
        f"{churn_rate:.1f}%"
    )

with kpi3:
    st.metric(
        "Average Monthly Charges",
        f"${filtered_df['MonthlyCharges'].mean():.2f}"
    )

with kpi4:
    st.metric(
        "Average Tenure",
        f"{filtered_df['tenure'].mean():.1f} Months"
    )

st.divider()

st.subheader("Customer Overview")

left, right = st.columns(2)

with left:

    churn = (
        filtered_df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn.columns = [
        "Churn",
        "Customers"
    ]

    fig = px.pie(
        churn,
        values="Customers",
        names="Churn",
        hole=0.45,
        title="Customer Churn Distribution",
        color="Churn",
        color_discrete_map={
            "No": "#10B981",
            "Yes": "#EF4444"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="label+percent+value"
    )

    fig.update_layout(
        legend_title="Churn Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with right:

    contract = (
        filtered_df["Contract"]
        .value_counts()
        .reset_index()
    )

    contract.columns = [
        "Contract",
        "Customers"
    ]

    fig = px.bar(
        contract,
        x="Contract",
        y="Customers",
        color="Contract",
        title="Contract Distribution",
        color_discrete_sequence=COLOR_PALETTE
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Contract Type",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.divider()

st.subheader("Customer Services")

left, right = st.columns(2)

with left:

    internet = (
        filtered_df["InternetService"]
        .value_counts()
        .reset_index()
    )

    internet.columns = [
        "Internet Service",
        "Customers"
    ]

    fig = px.bar(
        internet,
        x="Internet Service",
        y="Customers",
        color="Internet Service",
        title="Internet Service Distribution",
        color_discrete_sequence=COLOR_PALETTE
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Internet Service",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with right:

    payment = (
        filtered_df["PaymentMethod"]
        .value_counts()
        .reset_index()
    )

    payment.columns = [
        "Payment Method",
        "Customers"
    ]

    payment_order = [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    payment["Payment Method"] = pd.Categorical(
        payment["Payment Method"],
        categories=payment_order,
        ordered=True
    )

    payment = payment.sort_values("Payment Method")

    fig = px.bar(
        payment,
        x="Payment Method",
        y="Customers",
        color="Payment Method",
        title="Payment Method Distribution",
        color_discrete_sequence=COLOR_PALETTE
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Payment Method",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

st.divider()

st.subheader("Monthly Charges Analysis")

fig = px.box(
    filtered_df,
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    title="Monthly Charges by Churn Status",
    color_discrete_map={
        "No": "#10B981",
        "Yes": "#EF4444"
    },
    points="outliers"
)

fig.update_layout(
    showlegend=False,
    xaxis_title="Churn Status",
    yaxis_title="Monthly Charges ($)"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.divider()

st.caption(
    "Dashboard built with Streamlit and Plotly • Dataset: Telco Customer Churn"
)