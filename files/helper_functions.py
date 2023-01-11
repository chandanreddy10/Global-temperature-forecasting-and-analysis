import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sktime.forecasting.arima import ARIMA
import warnings
import os

#----- ARIMA starts
def arima_call(year):
    df = pd.read_csv("./data/train_and_test_data.csv")
    data = df.loc[:,('avg_temp')].copy()
    year_to_predict = year-2022

    future = __model_arima(1,1,0,data,year_to_predict)

    return future

def __model_arima(p,d,q,data,year):

    warnings.filterwarnings(action='ignore')

    #for data
    model = ARIMA((p,d,q))
    model.fit(data)

    predictions = model.predict(fh=np.arange(-68,0))
    future_model = model.predict(fh=[year])
    fvalue = future_model.values

    #for residuals model-2

    model2 = ARIMA(order=(p,d,q))
    residuals = (data- predictions)
    model2.fit(residuals)

    future_residual = model2.predict(fh=[year])
    rfvalue = future_residual.values

    forecasted = fvalue + rfvalue

    return forecasted

#-------ARIMA ends


#----- function to return plots
def get_plot(image_name,parent_id="./plots/Global_temperature/",plot_extension="png"):
    
    path = os.path.join(parent_id,image_name+"."+plot_extension)

    return path

#plotting the multiple charts for G20 countries

def plot_charts(country):
    
    df = pd.read_csv("./data/g20co2data.csv")

    temp_df = df.loc[df['country']==country].copy()
    country_df = temp_df.loc[temp_df['year']>1970].copy()

    fig1, ax = plt.subplots()
    ax.plot(country_df['year'], country_df['co2_per_capita'],"#243763",label="$CO_2$ per capita")
    ax.set(title="$CO_2$ per capita in each year", xlabel="year", ylabel="$co_2$ per capita")
    ax.legend(loc="upper left")

    fig2, ax = plt.subplots()
    ax.plot(country_df['year'], country_df['share_global_co2'],"#243763",label="share of global $CO_2$")
    ax.set(title="Share of global $CO_2$", xlabel="year", ylabel="share of global $CO_2$")
    ax.legend(loc="upper left")

    fig3,ax = plt.subplots()
    ax.plot(country_df['year'], country_df['share_global_cement_co2'],"#243763",label="share of cement $CO_2$")
    ax.set(title="Share of global cement $CO_2$ emissions", xlabel="year", ylabel="share of cement $CO_2$")
    ax.legend(loc="upper left")

    fig4,ax = plt.subplots()
    ax.plot(country_df['year'], country_df['consumption_co2_per_capita'],"#243763",label="consumption $CO_2$ per capita")
    ax.set(title="consumption $CO_2$ per capita", xlabel="year", ylabel="consumption $CO_2$ per capita")
    ax.legend(loc="upper left")

    return fig1,fig2,fig3,fig4

#-------for-page-2-pie-charts------

def plot_pie(year):

    world_df = pd.read_csv("./data/cleaned_world_co2.csv")
    columns = ('coal_co2','land_use_change_co2', 'cement_co2','consumption_co2','gas_co2','oil_co2','other_industry_co2')
    keys = ('Coal','Land use change','Cement','Consumption','Gas','Oil','Others')
    factors = world_df.loc[world_df['year']==year,columns].copy()

    total = factors.values.sum()
    fac = {}
    for value,key in zip(factors.values[0],keys):
        value = (value/total)*100
        fac.update({value:key})

    values_sorted=sorted(fac.keys(),reverse=True)

    ranked_factors = {}
    for value in values_sorted:
        key = fac.get(value)
        ranked_factors.update({key:value})

    fig, ax = plt.subplots()
    mexplode = [0.02,0.03,0.04,0.02,0.02,0.02,0.2]
    x = [value for value in ranked_factors.values()]
    labels = [label for label in ranked_factors.keys()]
    a,b,autotexts = ax.pie(x=x,labels=labels,explode=mexplode,autopct='%.1f%%',
    colors=['#243763','#850000','#285430','#5837D0','#562B08','#AC4425','#000000'])
    for autotext in autotexts:
        autotext.set_color('white')
    ax.set_title("Different factors contributing $CO_2$",loc='center')
    
    return fig

#--------for-page-2-gases-emissions

def plot_gases(year):

    gases = pd.read_csv("./data/world_gases.csv")
    world = gases.loc[gases['year']==year]
    world.drop(columns="Unnamed: 0",inplace=True)

    total = world.values[0][1] + world.values[0][2] + world.values[0][3]
    percentage = {'methane':world.values[0][1]/total, 'nitrous oxide':world.values[0][2]/total,
    'carbon dioxide':world.values[0][3]/total}

    fig, ax = plt.subplots()
    x = [value for value in percentage.values()]
    labels = [label for label in percentage.keys()]
    mexplode = [0.2, 0.3, 0.1]
    ax.pie(x=x,labels=labels,explode=mexplode,colors=['#B5D5C5','#FFEBB7','#1C315E'],autopct='%.2f%%')
    
    return fig

#-----for-individual-country-pie-chart-----

def individual_pie_chart(year,country):

    df = pd.read_csv("./data/g20_data_for_pie.csv")
    df.drop(columns="Unnamed: 0",inplace=True)

    year_df = df.loc[df['year']==year].copy()

    country = year_df.loc[df['country']==country].copy()

    temp_df = country.drop(columns=["year","country"]).copy()
    temp_df.fillna(0,inplace=True)
    total = temp_df.values.sum()
    keys = ('Coal','Land use change','Cement','Consumption','Gas','Oil','Others')

    factors = {}
    for value,key in zip(temp_df.values[0],keys):
        value = (value/total)*100
        factors.update({value:key})

    values_sorted=sorted(factors.keys(),reverse=True)

    ranked_factors = {}
    for value in values_sorted:
        key = factors.get(value)
        ranked_factors.update({key:value})

    fig, ax = plt.subplots()
    mexplode = [0.02,0.03,0.04,0.02,0.02,0.02]
    x = [value for value in ranked_factors.values()]
    labels =[label for label in ranked_factors.keys()]
    X=[]
    for val in x:
        if val <0:
            X.append(0)
        else:
            X.append(val)
    a,b,autotexts = ax.pie(x=X,explode=mexplode,labels=labels,autopct='%.1f%%',
    colors=['#243763','#850000','#285430','#5837D0','#562B08','#AC4425'])
    for autotext in autotexts:
        autotext.set_color('white')
    ax.set_title("Different factors contributing $CO_2$",loc='center')
    
    return fig 