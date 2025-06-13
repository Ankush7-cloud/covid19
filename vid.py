import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("country_wise_latest.csv")

st.set_page_config(layout="wide")
st.title("🌐 COVID-19 Country-wise Dashboard")

# Sidebar: Country selection
country_list = df["Country/Region"].dropna().unique()
selected_country = st.sidebar.selectbox("Select a Country", sorted(country_list))

# Filter for selected country
country_data = df[df["Country/Region"] == selected_country]

# Show raw data
st.subheader(f"📋 Raw Data for {selected_country}")
st.dataframe(country_data)

# Bar Chart - Summary
st.subheader("📊 Summary: Confirmed, Deaths, Recovered, Active")
cols = ["Confirmed", "Deaths", "Recovered", "Active"]
chart_data = country_data[cols].T.rename(columns={country_data.index[0]: selected_country})
st.bar_chart(chart_data)

# Line Chart - Simulated Trend
st.subheader("📈 Simulated Trend (Static Data)")
st.line_chart(chart_data)

# Pie Chart replacement using streamlit's area chart (optional)
st.subheader("📐 Area Chart as Pie Alternative")
st.area_chart(chart_data)

st.markdown("---")
st.caption("Data Source: Kaggle COVID-19 dataset")
