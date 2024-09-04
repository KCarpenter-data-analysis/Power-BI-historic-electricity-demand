#Creating hourly_observation table

#For cleaning open Midas Weather csv files then converting them into pandas dataframe format to be loaded into PostgreSQL database 
# station hourly_observation as csv files.

import pandas as pd
import numpy as np
import csv
import re


def get_obs_data(file_path, number_rows):
    """Skips first n rows of open Midas weather data CSV files and then all rows after that into df."""
    df = pd.read_csv(file_path, skiprows = number_rows, low_memory=False)
    return df



def cols_to_keep(df):
    """"Reduce df to only columns needed from hourly weather observations."""
    df = df.drop(df.tail(1).index) #Drop final empty row
    cols_to_keep = ['ob_time', 'src_id', 'wind_direction', 'wind_speed','air_temperature', 'dewpoint', 'wetb_temp','rltv_hum','drv_hr_sun_dur']
    df = df[cols_to_keep]
    df['ob_time'] = pd.to_datetime(df['ob_time'])
    return df



def check_values(df):
    """Prints a number of descriptions to see where data may be missing."""
    print('Null values are', df.isnull().sum())
    print(df.describe())
    print(df['ob_time'].groupby([df.ob_time.dt.month]).agg('count'))
    return



def full_date(start_year, end_year_plus_one):
    """Takes strings containing the year and the year after then creates df with a row for every hour in that year."""
    full_date_col = pd.date_range(start_year + '-01-01', end_year_plus_one +'-01-01', freq='60min')
    full_date_df = pd.DataFrame(full_date_col, columns=['ob_time'])
    full_date_df = full_date_df[:-1]
    return full_date_df
    


def add_all_dates(year, year_plus_one, df):
    """Create df with one column with datetime every hour between two dates then merges this with obs_df to make sure
    any missing time periods are included."""
    all_date_df = full_date(year, year_plus_one)
    print(all_date_df.tail())
    all_date_merge_df = all_date_df.merge(df, how = 'left', on = 'ob_time')
    return all_date_merge_df



def calc_wind_direction(df):
    """Takes a df then compiles a dictionary of wind directions then using the wind direction in degrees maps this to a new column
    in the df."""
    compass_dict = {1:'N', 2:'NNE', 3:'NE', 4:'ENE', 5:'E', 6:'ESE', 7:'SE', 8:'SSE', 9:'S', 10:'SSW', 11:'SW', 12:'WSW', 
                    13:'W', 14:'WNW', 15:'NW', 16:'NNW', 17:'N'}
    df['wind_value'] = round(df['wind_direction_degrees']/22.5) + 1
    df['wind_direction'] = df['wind_value'].map(compass_dict)
    df = df.drop(['wind_value'], axis=1)
    return df



number_rows = 280

#File path for 2018 Sutton Bonington data
file_path_2018 = 'C:/Users/katie/OneDrive/weather_data/hourly_weather_obs_sutton_bonington_2018.csv'


#Get 2018 data for Sutton Bonington
obs_sutton_2018 = get_obs_data(file_path_2018, number_rows)
obs_sutton_2018 = cols_to_keep(obs_sutton_2018)

#Check for missing data 
check_values(obs_sutton_2018)

#Get 2019 hourly weather obs data for Sutton
file_path_2019 = 'C:/Users/katie/OneDrive/weather_data/hourly_weather_obs_sutton_bonington_2019.csv'
obs_sutton_2019 = get_obs_data(file_path_2019, number_rows)
obs_sutton_2019 = cols_to_keep(obs_sutton_2019)

#Check for missing data 
check_values(obs_sutton_2019)


#Get 2020 hourly weather obs data
file_path_2020 = 'C:/Users/katie/OneDrive/weather_data/hourly_weather_obs_sutton_bonington_2020.csv'
obs_sutton_2020 = get_obs_data(file_path_2020, number_rows)
obs_sutton_2020 = cols_to_keep(obs_sutton_2020)

#Check for missing data
check_values(obs_sutton_2020)


#Get 2021 hourly weather obs data
file_path_2021 = 'C:/Users/katie/OneDrive/weather_data/hourly_weather_obs_sutton_bonington_2021.csv'
obs_sutton_2021 = get_obs_data(file_path_2021, number_rows)
obs_sutton_2021 = cols_to_keep(obs_sutton_2021)

#Check for missing data
check_values(obs_sutton_2021)


#Get 2022 hourly weather obs data
file_path_2022 = 'C:/Users/katie/OneDrive/weather_data/hourly_weather_obs_sutton_bonington_2022.csv'
obs_sutton_2022 = get_obs_data(file_path_2022, number_rows)
obs_sutton_2022 = cols_to_keep(obs_sutton_2022)

#Check for missing data
check_values(obs_sutton_2022)


#Concatenate Sutton data from 2018-2022 into one df
hourly_obs_sutton_df = pd.concat([obs_sutton_2018, obs_sutton_2019, obs_sutton_2020, obs_sutton_2021, obs_sutton_2022], ignore_index=True)
print(len(hourly_obs_sutton_df) == len(obs_sutton_2018) + len(obs_sutton_2019) + len(obs_sutton_2020) + len(obs_sutton_2021) + len(obs_sutton_2022))


#Checks for missing data
check_values(hourly_obs_sutton_df)

#Compiles df with no ob_times missing and merges with df with observations of sutton
hourly_obs_sutton_df = add_all_dates('2018', '2023', hourly_obs_sutton_df)
print(hourly_obs_sutton_df.shape)
print(hourly_obs_sutton_df.tail())


#rename columns
hourly_obs_sutton_df = hourly_obs_sutton_df.rename({'ob_time':'ob_time_id','src_id': 'station_id', 'wind_direction': 'wind_direction_degrees',
                                    'wetb_temp': 'wet_bulb_temp', 'rltv_hum': 'relative_humidity',
                                    'drv_hr_sun_dur': 'sunshine_duration'}, axis=1)

print(hourly_obs_sutton_df.head())

#Look at wind direction values
wind_directions = hourly_obs_sutton_df.wind_direction_degrees.unique()
print(wind_directions)

#Produce column with string containing direction wind is blowing
hourly_obs_sutton_df = calc_wind_direction(hourly_obs_sutton_df)
hourly_obs_sutton_df.head()

#Change station_id column to integer
hourly_obs_sutton_df['station_id'] = hourly_obs_sutton_df['station_id'].astype("Int64")


#Output to CSV file for importing into PostgreSQl
hourly_obs_sutton_df.to_csv('C:/Users/katie/OneDrive/weather_data/hourly_obs_sutton.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_NONE)


