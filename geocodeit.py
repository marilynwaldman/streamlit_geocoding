import time 
import base64

import streamlit as st
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def create_address_col(df):
    st.sidebar.title("Select Address columns")
    st.sidebar.info("You need to select address column (Street name and number), post code and City")
    
    address_name = st.sidebar.selectbox("Select Address column", df.columns.tolist())
    city = st.sidebar.selectbox("Select City Column", df.columns.tolist())
    state = st.sidebar.selectbox("Select the State Column", df.columns.tolist())
    zip_code = st.sidebar.selectbox("Select the Zip Code Column", df.columns.tolist())

    

    df["geocode_col"] =  df[address_name].astype(str) + ',' + \
                df[city].astype(str) + ',' + \
                df[state].astype(str) + ',' + \
                df[zip_code].astype(str) 
       
    return df
    
def choose_geocode_column(df):
    selection = st.selectbox("Select the column", df.columns.tolist())
    df["geocde_col"] = df[selection]
    return df

def main():
    reload_data = False
    df  = pd.DataFrame() 
    df['geocode_col'] = None
    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        
        df = pd.read_csv(file, low_memory=False)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
            st.write(df.head())
            st.write(df.shape)

    cols = df.columns.tolist()

    st.subheader("Choose Address Columns from the Sidebar")
    st.info("Example correct address: 314 S. Golden Ave, Apt 304, Boulder, CO, 80301")
    df_address = create_address_col(df)
    st.write(df_address["geocode_col"].head())
    

if __name__ == "__main__":
    main()            
            
        


