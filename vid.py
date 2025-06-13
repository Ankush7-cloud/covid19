import pandas as pd
# Load the dataset
df = pd.read_csv('country_wise_latest.csv')

# Data preprocessing
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df = df.rename(columns={'Country/Region': 'Country'})

# Sidebar filters
st.sidebar.header("Filter Data")
country = st.sidebar.selectbox("Select Country", df['Country'].unique())
filtered_df = df[df['Country'] == country]

st.title(f"COVID-19 Dashboard for {country}")

# --- LINE CHART: Cases Over Time ---
st.subheader("Confirmed Cases Over Time")
line_data = filtered_df.groupby('ObservationDate')['Confirmed'].sum().reset_index()
st.line_chart(line_data.rename(columns={'ObservationDate': 'index'}).set_index('index'))

# --- BAR CHART: Latest Day Summary ---
st.subheader("Latest Day Case Summary")
latest_date = filtered_df['ObservationDate'].max()
latest_data = filtered_df[filtered_df['ObservationDate'] == latest_date].groupby('Country').sum()
latest_country_data = latest_data.loc[country][['Confirmed', 'Deaths', 'Recovered']]

st.bar_chart(latest_country_data)

# --- PIE CHART: Proportions ---
st.subheader("Proportions on Latest Date")
fig, ax = plt.subplots()
ax.pie(latest_country_data, labels=latest_country_data.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures pie chart is circular
st.pyplot(fig)

# Footer
st.markdown("Data Source: Kaggle - COVID-19 Dataset")
