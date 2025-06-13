import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load raw COVID-19 data
df = pd.read_csv("country_wise_latest.csv")

# Streamlit Title
st.title("COVID-19 Dashboard")

# Sidebar Country Selection
country = st.sidebar.selectbox("Select a Country", df["Country/Region"].unique())

# Filter data by country
country_data = df[df["Country/Region"] == country]

# Display raw data
st.subheader("Raw Data")
st.dataframe(country_data)

# Line Chart - Confirmed cases over time
st.subheader("Confirmed Cases Over Time (Line Chart)")
line_chart_data = country_data.groupby("New cases")["Confirmed"].sum()
st.line_chart(line_chart_data)

# Bar Chart - Deaths, Recovered, Confirmed on the latest day
st.subheader("Latest Day Summary (Bar Chart)")
latest_date = country_data["New cases"].max()
latest_stats = country_data[country_data["New cases"] == latest_date]

if not latest_stats.empty:
    totals = latest_stats[["Confirmed", "Deaths", "Recovered"]].sum()
    st.bar_chart(totals)

    # Pie Chart
    st.subheader("Proportions (Pie Chart)")
    fig, ax = plt.subplots()
    ax.pie(totals, labels=totals.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
else:
    st.warning("No data available for the latest date.")
