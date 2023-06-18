import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load the Iris dataset
@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    return data

data = load_data()

# Set up the sidebar
st.sidebar.header('Iris Dataset Explorer')
selected_plot = st.sidebar.selectbox('Select a Plot', ['Histogram', 'Scatter Plot', 'Box Plot'])

# Display the selected plot
st.header('Iris Dataset Explorer')

if selected_plot == 'Histogram':
    st.subheader('Histogram')
    column = st.selectbox('Select a column', data.columns)
    fig = px.histogram(data, x=column, color='species')
    st.plotly_chart(fig, use_container_width=True)

elif selected_plot == 'Scatter Plot':
    st.subheader('Scatter Plot')
    x_column = st.selectbox('Select X-axis', data.columns[:-1])
    y_column = st.selectbox('Select Y-axis', data.columns[:-1])
    fig = px.scatter(data, x=x_column, y=y_column, color='species')
    st.plotly_chart(fig, use_container_width=True)

elif selected_plot == 'Box Plot':
    st.subheader('Box Plot')
    column = st.selectbox('Select a column', data.columns[:-1])
    fig = px.box(data, x='species', y=column)
    st.plotly_chart(fig, use_container_width=True)

# Display summary and description
st.subheader('Summary')
st.write(data.describe())

st.subheader('Description')
st.write("""
The Iris dataset contains measurements of four features (sepal length, sepal width, petal length, and petal width) of three different species of Iris flowers (setosa, versicolor, and virginica).
This dashboard allows you to explore the dataset by visualizing different plots and displaying summary statistics.
""")

# Display the dataset
st.subheader('Dataset')
st.dataframe(data)
