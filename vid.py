import streamlit as st
import pandas as pd

# Load CSV
df = pd.read_csv("country_wise_latest.csv")

st.title("🌍 COVID-19 Dashboard (Country-Wise)")

# Sidebar: select country
country = st.sidebar.selectbox("Select a Country", df["Country/Region"].dropna().unique())

# Filter data
data = df[df["Country/Region"] == country]

st.subheader(f"📋 Data for {country}")
st.write(data)

# Bar Chart: Confirmed, Deaths, Recovered, Active
st.subheader("📊 Case Summary (Bar Chart)")
cols = ['Confirmed', 'Deaths', 'Recovered', 'Active']
case_data = data[cols].T  # Transpose for bar chart
st.bar_chart(case_data)

# Line Chart: just duplicating bar data over index (simulate time)
st.subheader("📈 Simulated Trend (Line Chart)")
st.line_chart(case_data)

# Pie Chart
st.subheader("🥧 Case Distribution (Pie Chart)")
fig, ax = plt.subplots()
ax.pie(data[cols].values.flatten(), labels=cols, autopct="%1.1f%%", startangle=90)
ax.axis('equal')
st.pyplot(fig)

st.markdown("---")
st.caption("Data Source: Kaggle | COVID-19 Country Wise Latest")
