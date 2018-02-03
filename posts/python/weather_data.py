
# coding: utf-8

# Convert NOAA weahter data file ".dly" to Pandas DataFrame
# 
# Follow this instruction https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
# 
# Get data from ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily
# 
# <!-- TEASER_END -->

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import ftplib

get_ipython().magic('matplotlib notebook')


# In[2]:


# download data from FTP

def download_file_from_ftp(FTP_SERVER,FTP_PATH,FILENAME):
    with ftplib.FTP(FTP_SERVER) as ftp:
        ftp.login()
        ftp.cwd(FTP_PATH)
        with open(FILENAME, 'wb') as f:
            ftp.retrbinary('RETR ' + FILENAME, f.write)


# # Query station ID

# In[3]:


def get_station_ID(station_to_find, filename):
    for line in open(filename):
        if station_to_find in line:
            line_with_station=line
            station_ID=re.split(" ",line_with_station)[0]
            return station_ID
    return None
# warning, it is slow, download it only once
download_file_from_ftp("ftp.ncdc.noaa.gov", "/pub/data/ghcn/daily", "ghcnd-stations.txt")

station_to_find="GUANGZHOU" # USE CAPS
station_ID=get_station_ID(station_to_find, "ghcnd-stations.txt")


# # Download weather data

# In[4]:


weather_data_filename=station_ID+'.dly'

# warning, it is slow, download it only once
download_file_from_ftp("ftp.ncdc.noaa.gov", "/pub/data/ghcn/daily/all", weather_data_filename)


# # Convert .dly to pandas Dataframe

# In[7]:


def convert_dly_to_dataframe(dly_filename): 
    def build_dly_value_dict():
        dly_value_dict_base={
        "VALUE":[22,26],
        "MFLAG":[27,27],
        "QFLAG":[28,28],
        "SFLAG":[29,29]}
        dly_value_step=8
        dly_value_dict={}
        for day in range(31):
            for k,v in dly_value_dict_base.items():
                dly_value_dict[k+str(day+1)]=[v[0]+dly_value_step*day,v[1]+dly_value_step*day]
        return dly_value_dict
    
    dly_dict={
        "ID": [1,11],
        "YEAR":[12,15], 
        "MONTH": [16,17], 
        "ELEMENT":[18,21],}
    dly_dict.update(build_dly_value_dict())

    columns_value=["VALUE"+str(day+1) for day in range(31)]
    columns=["YEAR","MONTH","ELEMENT"]+columns_value

    def extract_data_from_line(string,loc,astype=str):
        return astype(string[loc[0]-1:loc[1]])

    data=[]
    for line in open(dly_filename):
        data_item=[]
        for k in columns:
            data_item.append(extract_data_from_line(line,dly_dict[k]))
        data.append(data_item)
    df=(pd.DataFrame(data,columns=columns)
         .apply(pd.to_numeric, errors='ignore')
         .replace(-9999,np.nan))
    return df

df=convert_dly_to_dataframe(weather_data_filename)
df.head()


# In[ ]:




