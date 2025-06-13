import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("country_wise_latest.csv")

st.set_page_config(layout="wide")
st.title("🦠 COVID-19 Dashboard")

# Country selection
country_list = df["Country/Region"].dropna().unique()
selected_country = st.selectbox("🌍 Select a Country", sorted(country_list))

# Filter for selected country
country_data = df[df["Country/Region"] == selected_country]
cols = ["Confirmed", "Deaths", "Recovered", "Active"]
chart_data = country_data[cols].T.rename(columns={country_data.index[0]: selected_country})

# Buttons to control chart display
st.subheader("📊 Choose Chart to Display:")
col1, col2, col3 = st.columns(3)

show_bar = col1.button("Show Bar Chart")
show_line = col2.button("Show Line Chart")
show_pie = col3.button("Show Pie Chart")

# Display chart based on button click
if show_bar:
    st.subheader(f"📊 Bar Chart for {selected_country}")
    st.bar_chart(chart_data)

elif show_line:
    st.subheader(f"📈 Line Chart for {selected_country}")
    st.line_chart(chart_data)

elif show_pie:
    st.subheader(f"🥧 Pie-like Area Chart for {selected_country}")
    st.area_chart(chart_data)

# Optional: Show data
with st.expander("🔍 View Raw Data"):
    st.dataframe(country_data)

st.caption("Data Source: Kaggle | COVID-19 Country Wise Latest")
