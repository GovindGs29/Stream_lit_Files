
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Load data
data = pd.read_csv('data.csv')

# Streamlit App Title
st.title("Stream Lit: Data Visualization App")

# Display the DataFrame
st.write("### DataFrame:")
st.write(data)

# Altair Chart
st.write("### Altair Chart:")
alt_chart = alt.Chart(data).mark_bar().encode(
    x='column1',
    y='column2'
)
st.altair_chart(alt_chart, use_container_width=True)

# Plotly Express Chart
st.write("### Plotly Express Chart:")
fig = px.scatter(data, x='column1', y='column2')
st.plotly_chart(fig)
