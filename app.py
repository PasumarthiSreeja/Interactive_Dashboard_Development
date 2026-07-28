import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="Interactive Dashboard", layout="wide")

st.title("📊 Interactive Sales Dashboard")

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Sidebar
st.sidebar.header("Dashboard Filters")

selected_month = st.sidebar.selectbox(
    "Select Month",
    ["All"] + list(df["Month"])
)

if selected_month != "All":
    df = df[df["Month"] == selected_month]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,}")
col2.metric("Total Profit", f"${df['Profit'].sum():,}")
col3.metric("Customers", df["Customers"].sum())

st.divider()

# Sales Chart
st.subheader("Monthly Sales")

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(df["Month"], df["Sales"])
plt.xticks(rotation=45)
st.pyplot(fig)

# Profit Chart
st.subheader("Monthly Profit")

fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.plot(df["Month"], df["Profit"], marker="o")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Dataset
st.subheader("Dataset")
st.dataframe(df)

st.success("Dashboard Loaded Successfully!")
