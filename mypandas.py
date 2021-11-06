
from io import StringIO
import time 
import base64


import streamlit as st
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt

import folium
from streamlit.type_util import is_dataframe
from streamlit_folium import folium_static

def get_fulladdress(df):

    df['full_address'] = df['Street address line 1 - Home'].astype('string') + ','  \
                        + df['Zip/Postal Code - Home']

                          
                     
    return df                 

def geo_codeit(df):
    from geopy.geocoders import Nominatim
    locator = Nominatim(user_agent="Ohmy22")

    from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(locator.geocode, min_delay_seconds=5)
    #df['location'] = df['full_address'].apply(geocode)

    df['Latitude'] = None
    df['Longitude'] = None
    df['Location_found'] = None

    found_list = []
    not_found_list = []
    
    for i in range(len(df)):
         print(i)
         location = locator.geocode(df.loc[i,'full_address'])
          
         if location is not None:
             df.loc[i,'Location_found'] = "found" 
             df.loc[i,'Latitude'] = location.latitude   
             df.loc[i,'Longitude'] = location.longitude
         if (i % 50) == 0:
               time.sleep(30)    
    df_found = df[df.Location_found.notnull()]
    df_not_found = df[df.Location_found.isnull()] 
    st.write("locations not found for ...")        
    st.dataframe(df_not_found)     
    return df_found, df_not_found

def draw_map(df_found):
    # center on Silverton
    m = folium.Map(location=[37.6300, -107.8139], tiles='cartodb positron',zoom_start=9)
    #st.write(df[0])
    for index, row in df_found.iterrows():
        loc = [row['lat'],row['long']]
        # add marker for Liberty Bell
        tooltip = row['full_address']
        folium.Marker(
             loc, popup=row['full_address'], tooltip=tooltip
        ).add_to(m)
    folium_static(m)

    return

#read csv and return a dataframe 
#column names are first row of csv
#all columns read as strings

def get_csv():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    
    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        df = pd.read_csv(file, header=0,
                 low_memory=False,
                 dtype=str)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
        st.write(df.head())
        st.write(df.shape)
        print(df.dtypes)    
        print(df.dtypes)
        df = get_fulladdress(df)
        df1 = df.head(1000)
        st.dataframe(df1['full_address'])
        df_found, df_not_found = geo_codeit(df1)
        return(df)
    


def main():
        df = get_csv()
        
        
        
    
        #draw_map(df)
    
if __name__ == "__main__":
    main()

     
