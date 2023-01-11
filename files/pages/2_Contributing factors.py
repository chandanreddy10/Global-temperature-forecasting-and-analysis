import streamlit as st
import pandas as pd
import helper_functions

st.set_page_config(page_title='Project report',layout='wide')
st.title(":violet[Contributing Factors for the temperature rise.]")

#plots container
with st.container():

    with st.container():

        countries = pd.Series(('Argentina','Australia', 'Brazil', 'Canada', 
    'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'South Korea', 'Japan', 'Mexico', 'Russia', 
    'Saudi Arabia', 'South Africa', 'Turkey', 'United Kingdom', 'United States','European Union (27)'))
        
        country = st.selectbox(label="Select a country",options=countries,index=7,help="please select a country to output its co2 emissions etc.")
        st.text(f"Selected country - {country}")
    fig1, fig2, fig3, fig4 = helper_functions.plot_charts(country)
    with st.container():
        col1,col2 = st.columns(2, gap="large")
        with col1:
            st.pyplot(fig1)
        
        with col2:
            st.pyplot(fig2)

    with st.container():
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.pyplot(fig3)
        with col2:
            st.pyplot(fig4)

#for g-20 plots
with st.container():
    
    u_parent = "./plots/contributing_factors/"
    plot = helper_functions.get_plot
    
    col1, col2  = st.columns(2,gap="large")
    with col1:
        st.text("")
        st.image(plot("g20_per_capita_co2_emission",u_parent),caption="per capita co2 emission og G20 nations.",width=650)
        st.text("")
        st.text("")
        st.text("")
        st.image(plot("g20_share_of_global_co2_emission",u_parent),caption="global share of co2 emissions",width=650)

    with col2:
        st.markdown(
            """#### Here, we have considered only G-20 countries because the they account for almost all the GDP and trade in the world.  \n"""
            """  \n"""
            """#### Plots show how each countries are contributing to the climate change which is the result of global warming. Here, we have only considered $CO_2$ emissions, as shown below $CO_2$ emissions are the main drivers of the temperature rise."""
            """  \n"""
            """#### we have plotted per capita co2, global cement co2 share, global share of co2 emissions \n"""
        )
        st.text("")
        st.text("")
        st.text("")
        st.image(plot("g20_share_of_global_cement_co2_emission",u_parent),caption="share of global cement co2 emissions.",width=640)


#for the pie charts
with st.container():
    
    col1, col2 = st.columns(2,gap="large")

    with col1:
        year = st.slider(label="pick a year to see the factors contributing to $CO_2$ emissions.",min_value=2000,max_value=2021,value=2016,help="select an year to ouput the respective percentage of factors.")
        figure = helper_functions.plot_pie(year)

        g_year = st.slider(label="pick a year to see the greenhouse gases",min_value=2004,max_value=2019,value=2016,help="select an year to ouput the respective percentage of gases emissions")
        g_figure= helper_functions.plot_gases(g_year)

        st.pyplot(g_figure)
    with col2:
        st.pyplot(figure)
        
#for factors---charts
with st.container():

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.image(plot("temp_vs_first_factors",u_parent),caption="temperature vs factors",width=650)
    
    with col2:
        st.image(plot("temp_data_vs_second_factors",u_parent),caption="temperature vs factors",width=650)

#for text----
with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """##### The above charts show the factors and temperature, it shows how temperature varies or get effected from the factors.  \n"""
            """##### Factors considered are the coal, oil, consumption, land use and others. as we can see the main contributors are coal and cement from the left side graph and all the factors from the right side."""
            """  \n"""
            """##### The values were scaled down using the min max scaling and to the prodcut added 0.2 to match the temperature, this would make our analysis easier."""
            """  \n"""
            """##### Here is the correlation of all the factors with temp."""
            """  \n"""
            """##### From the table the highest correlated values are coal, gas and cement. \n"""
            """  \n"""
            """##### Interestingly the **consumption** is less correlated to the temperature."""
        )
    with col2:
        corr = pd.read_csv("./data/correlation_data.csv")
        st.dataframe(corr)