import pandas as pd

co2df = pd.read_csv("./data/co2-data.csv")
temp_df = pd.read_csv('./data/land_temp.csv')
sea_level_df = pd.read_csv('./data/sealevel.csv')
temp_df.drop(0,inplace=True)

#co2 data
def total_co2_emissions(year,co2df=co2df):

    world_co2df = co2df.loc[co2df['country']=='World'].copy()
    world_co2df.reset_index(drop=True, inplace=True)
    final_worldco2_df = world_co2df.loc[world_co2df['year']>=1970].copy()
    final_worldco2_df.reset_index(drop=True, inplace=True)

    if year <=2021:
        co2_value = final_worldco2_df.loc[final_worldco2_df['year']==year]['co2']
        if len(co2_value.values)>0:
            val= co2_value.values[0]/1000
            helper = f'{val :.2f}'
            return float(helper)
        else:
            return 'NaN'
    else:
        return 'NaN'

#temperature rise
def temperature_rise(year,temp_df=temp_df):

    temp_df['Year'] = temp_df['Year'].apply(lambda x: int(x))
    temp_df['Month'] = temp_df['Month'].apply(lambda x: int(x))
    temp_df['Monthly'] = temp_df['Monthly'].apply(lambda x: float(x))
    
    new_temp_df = temp_df.loc[temp_df['Month']==10].copy()[['Year','Monthly']]
    final_temp_df = new_temp_df.loc[new_temp_df['Year']>=1970].copy()
    final_temp_df.reset_index(drop=True,inplace=True)

    if year<=2021 and year>=1970:
        temp = final_temp_df.loc[final_temp_df['Year']==year]['Monthly'].values
        if len(temp) >0:
            value= f'{temp[0] :.2f}'
            return float(value)
        else:
            return 'NaN'
    else:
        return 'NaN'

#sea level rise
def sea_level_rise(year,sea_df = sea_level_df):
    
    years = sea_df['Year'].unique()
    new_sea_level = pd.DataFrame(data=None)

    for year2 in years:
        helper_df = sea_df.loc[sea_df['Year']==year2].copy()
        helper_df.reset_index(drop=True,inplace=True)
        new_sea_level = pd.concat([new_sea_level, helper_df.iloc[:1]],axis=0)

    new_sea_level.reset_index(drop=True,inplace=True)

    if year<=2021 and year>=1993:

        sea_level = new_sea_level.loc[new_sea_level['Year']==year]['GMSL_noGIA'].values

        if len(sea_level)>0:

            sl_inches = sea_level[0] * 0.0393701
            helper = f'{sl_inches :.2f}'
            return float(helper)

        else:
            return 'NaN'
    else:
        return 'NaN'
