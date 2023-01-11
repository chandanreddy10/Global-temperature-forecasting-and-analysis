import streamlit as st
import metrics 
import helper_functions

st.set_page_config(page_title='Project report',layout='wide')
st.title("Project Report on :violet[Global temperature forecasting] and :blue[analysis.]")

st.header("The cost of climate change is a whopping :red[$525 billon.]")
#container for slide bar and metrics
with st.container():
    year = st.slider(label='Select Year',min_value=1993, max_value=2021,value=2019,help='select the year to output metrics.')

    col1, col2, col3 = st.columns(3,gap='large')

    with col1:
        present_value = metrics.total_co2_emissions(year)
        previous_value = metrics.total_co2_emissions(year-1)

        title ='<p style="font-family:Sans-Serif; color:#2B3467; font-size: 20px;">Global CO<sub>2</sub> emissions.</p>'
        st.markdown(title,unsafe_allow_html=True)
        st.metric(label="------",value=f"{present_value} Gt",delta=f"{present_value-previous_value :.2f} Gt")

    with col2:
        present_value = metrics.temperature_rise(year)
        previous_value = metrics.temperature_rise(year-1)

        title ='<p style="font-family:Sans-Serif; color:#2B3467; font-size: 20px;">Global temperature rise.</p>'
        st.markdown(title,unsafe_allow_html=True)
        st.metric(label="------",value=f"{present_value} °C",delta=f"{present_value-previous_value : .2f} °C")

    with col3:
        present_value = metrics.sea_level_rise(year)
        previous_value = metrics.sea_level_rise(year-1)

        title ='<p style="font-family:Sans-Serif; color:#2B3467; font-size: 20px;">Sea level rise.</p>'
        st.markdown(title,unsafe_allow_html=True)
        st.metric(label="------",value=f"{present_value} in",delta=f"{present_value-previous_value : .2f} in")

def space_func():
    st.text("")
    st.text("")
    st.text("")
    st.text("")

space_func()
#container for model forecasting
with st.container():

    col1, col2 = st.columns(2,gap="large")

    with col1:
        year = st.number_input("Enter the year to get predicted temperature.",min_value=2016,max_value=2030,value=2023)
        st.text(f"Entered year {year}")

        ftemp = helper_functions.arima_call(year)[0]
        ptemp = helper_functions.arima_call(year-1)[0]

    with col2:

        st.metric(label=f"Predicted value for {year}",value=f"{ftemp : .2f} °C",delta=f"{ftemp-ptemp :.2f} °C")

space_func()
#text container
with st.container():
        text = '<p style="font-family:Sans-Serif; color:#2B3467; font-size: 40px;text-align:center;">The Model</p>'
        st.markdown(text,unsafe_allow_html=True)

#this for the details of the model.
tab1, tab2 = st.tabs(["DATA","MODEL"])

##----------------------------------------------TAB-1---------------------
#describing the data with statistical tests.
with tab1:

    #to display data
    with st.container():

        col1,col2 = st.columns(2,gap="large")

        with col1:
            import pandas as pd

            df = pd.read_csv("./data/cleaned_temp.csv")
            df.drop(columns="Unnamed: 0",inplace=True)

            st.dataframe(df.head(12))
        
        with col2:
            st.markdown(
        """ The global land temperature data is collected from **berkely.org** through web scraping.initially, the data was messy and filled with some relatively low null values.  \n
    The data has land temperature from the year **1750** measured relatively to the time period **1950-1980**, 
    main measure is the anamoly which is represented in monthly annualy etc. it represents how the temperature has varied from the period 1950-1980.  \n
    if there is a positive sign it means that the temperature has increased compared to the period and vice versa.
    just by observation it is clear thet land temperature was cooler in 1750 compared to 1950-1980.
        
        """)

    #to display plots  
    with st.container():
        col1, col2 = st.columns(2,gap="large")
        with col1:
            plots = helper_functions.get_plot
            st.image(plots("land_temp_between_1750_2022"),caption="temperature between 1750-2022",width=600)

        with col2:
            st.image(plots("average_temperature_over_the_year"),caption="Average temperature",width=600)

    with st.container():

        st.markdown(
        """ #### Above plots show the temperature plots. left side is the plot for temperature over the years, right side is the average temperature over the years.
        """)
    
    with st.container():

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.image(plots("Autocorrelation_of_global_temp_lags"), caption="auto-correlation",width=600)

            st.image(plots("partial_autocorrelation_of_global_temp_lags"),caption="partial auto-correlation",width=600)
            st.text("")
            st.image(plots("data_components"),caption="different data components",width=600)


        with col2:

            st.markdown(
            """The plots shown here are the **statistical measures**.  \n"""
            """  \n"""
            """**Auto correlation** measures the relationship between the data and its lags. lag mean the previous value in the data so, in simple terms we are finding the serial dependence of the data.  \n"""
            """  \n"""
            """In the plot, lag 0 has highest value meaning, when the value is plotted with itself it was increasing as the x increases. this is of course natural. but, auto correlation doesn't tell us the entire picture.
            let's say we neeed to find the correlation between 5th lag and the value, auto correlation gets influenced from the lags before. So, to overcome this problem we use **partial Auto correlation**  \n
            """
            """  \n"""
            
            """ **Partial correlation** is also a measure of the correlation of the values to its previous ones but, here the influence of the intermeidate lags is not considered.
            on any given day partial correlation is choosen over the auto correlation.  \n"""
            """  \n"""
            """ **Impact-response** curve results us with the effect that lags have on the value. as we can see from the plot after lag 10 the effect is minimum, out of all the lags lag-1 has the highest effect on the values.
            generally this is the case  \n"""
            """  \n"""
            """ Next plot is the components one. this plots splits the data into different components such as **seasonality**, **trend**, **residuals**, as we can see from the plot that there is no seasonality in the data. it has only the trend component  \n
            """
            """  \n"""
            """**quantile-quantile** plot describes whether the data is **stationary** or not. **stationarity** being, the mean and variance would remain constant throughout  \n"""
            """  \n"""

            """ There is also one more test to find whether the data is stationary or not, it is known as **Dickey-Fuller test**, it results with the bunch of values. in that important are the **test statistic**
            and the critical values for test statistic at 1%, 5% and 10% levels. if the test statistic is less than the critical value we say that the data is **non-stationary** and vice versa."""
            )
            st.image(plots("impact-response-plot"),caption="impact-responce plots",width=600)

            st.image(plots("quantile-quantile_plot"),caption="quantile quantile",width=600) 

#------------------------TAB-2---------------------------------------

with tab2:

    #text container
    with st.container():

        st.markdown(
            """##### For forecasting, we have different models. there are two types of features in time series, one is the time dependency, where the data is modelled based on the date or time and the values. the other is the serial dependency, where the data is modelled based on its lags."""
        """  \n"""
        """##### Here, we consider the serial dependency, modelling based on lags.
        """
        """  \n"""
        """##### Auto-Regressive models are the best for this purpose, we consider especially the ARIMA model."""
        """  \n"""
        """##### ARIMA stands for Auto-regressive integrated moving average, the parameters (p,q,d), p stands for the lag factor, q is the moving average part and d is the differencing. differencing in simple terms means the subtraction of the current values with the past. let's say the d was set to one, then the value would be the subtraction of present and the value before.  \n"""
        """  \n"""
        )
    with st.container():
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image(plots("AIC_score"),caption = "akaike information criterion",width=400)

        with col2:
            st.markdown(
                """##### Boosting technique was used to train the model. model-1 was trained on the data, model-2 was trained on the residuals of the model-1, with clubbing both of them we were able to get some improvised results.  \n"""
                """  \n"""
                """##### The metric which was used to measue the loss was **AIC**(alkaike information criterion) and **MAE**(Mean absolute error), the parameters were p=1, d=1, q=0, this resulted with the minimum loss model.  \n"""
                """  \n"""
                """##### From the below charts, models behaves well as the data is added to the model.
                """)
    with st.container():

        st.image(plots("ARIMA_model_on_train_vs_test"),caption="model on data without latest observations")

        st.image(plots("ARIMA_model_with_latest_data"),caption="model on data with latest observations")

with st.sidebar:
    st.write("Climate change project.")