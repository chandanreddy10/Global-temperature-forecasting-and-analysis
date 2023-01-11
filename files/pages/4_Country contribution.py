import streamlit as st
import pandas as pd
import helper_functions

st.set_page_config(page_title='Project report',layout='wide')
st.title(":blue[Factors contributing by country(G-20)]")

with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        countries = pd.Series(('Argentina','Australia', 'Brazil', 'Canada', 
    'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'South Korea', 'Japan', 'Mexico', 'Russia', 
    'Saudi Arabia', 'South Africa', 'Turkey', 'United Kingdom', 'United States','European Union (27)'))
        country = st.selectbox(label="Select Country.",options=countries,index=7)
        year = st.slider(label='Select Year',min_value=2005, max_value=2021,value=2019,help='select the year to output pie plot.')

    with col2:
        figure = helper_functions.individual_pie_chart(year,country)
        st.pyplot(figure)

