%%writefile app.py
import streamlit as st
import pandas as pd
import sqlite3

# Load your data (replace with your actual data loading)
conn = sqlite3.connect('retail_db.sqlite')  # Assuming your database is named 'retail_db.sqlite'
df = pd.read_sql_query("SELECT * FROM retail", conn)
conn.close()

st.title("Retail Data Explorer")

# Country selection
selected_country = st.selectbox("Select a Country:", df['Country'].unique())

# Filter data by selected country
country_data = df[df['Country'] == selected_country]

# Display the filtered data
st.write(f"Data for {selected_country}:")
st.dataframe(country_data)

# Column selection for min/max
columns_to_analyze = st.multiselect("Select columns to find min/max:", df.columns[2:]) #Exclude CustomerID and Country

if columns_to_analyze:
    for col in columns_to_analyze:
        if col in country_data.columns: # Check if the column exists in the filtered data
          min_val = country_data[col].min()
          max_val = country_data[col].max()
          st.write(f"For {col} in {selected_country}:")
          st.write(f"- Minimum: {min_val}")
          st.write(f"- Maximum: {max_val}")
        else:
            st.warning(f"Column '{col}' not found in data for {selected_country}")
else:
  st.write("Select at least one column to display min/max values.")
