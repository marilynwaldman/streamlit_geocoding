from io import StringIO
import time 
import base64

import os
import os.path
from os import path
from pathlib import Path
import sys
import shutil
from time import sleep
from random import randint
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt


def get_fulladdress(df):
    
    df['full_address'] = df['Street address line 1 - Home'].astype('string') + ','  \
                        + df['Zip/Postal Code - Home'].astype('string')
    return df

def geo_codeit(df):
    user_agent = 'user_me_{}'.format(randint(10000,99999))
    locator = Nominatim(user_agent=user_agent)

    geocode = RateLimiter(locator.geocode, min_delay_seconds=5)
    df['location'] = df['full_address'].apply(geocode)

    df['Latitude'] = None
    df['Longitude'] = None
    df['Location_found'] = None
    
    for i in range(len(df)):
         
         location = locator.geocode(df.loc[i,'full_address'])
          
         if location is not None:
             df.loc[i,'Location_found'] = "found" 
             df.loc[i,'Latitude'] = location.latitude   
             df.loc[i,'Longitude'] = location.longitude 
     
    return df 

    






def get_dir():
    filename="voters.csv"
    split_names = filename.split(".")
    
    dir = "./"
    if len(split_names) > 1:
         print("here")
         dir = dir + split_names[0]
    else:
         dir = dir + filename
    return dir  

def process_files(indir, outdir, current_file, bad_files):
    count = 0
    for file in os.listdir(indir):

        outpath = outdir + "/" + file
        if path.exists(outpath):
            pass
        df_chunk = pd.read_csv(indir + "/" + file)
        df_chunk.to_csv(current_file + "/" + file)
        os.remove(indir + "/" + file)
        
        df_location = get_fulladdress(df_chunk)
            
        df_located = geo_codeit(df_location)
        if df_located is not None:
            df_located.to_csv(outdir + "/" + file)
        else:
            df_location.to_csv(bad_files + "/" + file)    
            
        os.remove(current_file + "/" + file)
        time.sleep(1)
        



        

    return

def main():
    dir = get_dir()
    indir = dir + "/input"
    outdir = dir + "/output"
    current_file = dir + "/current"
    bad_files = dir + "/badfiles"

    process_files(indir, outdir, current_file, bad_files)

if __name__ == "__main__":
    main()        
                          
                     