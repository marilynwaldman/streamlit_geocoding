import os
import pathlib
import requests
import zipfile
import pandas as pd
import geopandas as gpd
import streamlit as st
# from : https://github.com/giswqs/streamlit-geospatial/blob/master/apps/housing.py

STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / "static"
# We create a downloads directory within the streamlit static asset directory
# and we write output files to it
DOWNLOADS_PATH = STREAMLIT_STATIC_PATH / "downloads"
if not DOWNLOADS_PATH.is_dir():
    DOWNLOADS_PATH.mkdir()

@st.cache(allow_output_mutation=True)
def get_geom_data(category):

    prefix = (
        "https://raw.githubusercontent.com/giswqs/streamlit-geospatial/master/data/"
    )
    links = {
        "national": prefix + "us_nation.geojson",
        "state": prefix + "us_states.geojson",
        "county": prefix + "us_counties.geojson",
        "metro": prefix + "us_metro_areas.geojson",
        "zip": "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_zcta510_500k.zip",
    }

    if category.lower() == "zip":
        r = requests.get(links[category])
        out_zip = os.path.join(DOWNLOADS_PATH, "cb_2018_us_zcta510_500k.zip")
        with open(out_zip, "wb") as code:
            code.write(r.content)
        zip_ref = zipfile.ZipFile(out_zip, "r")
        zip_ref.extractall(DOWNLOADS_PATH)
        gdf = gpd.read_file(out_zip.replace("zip", "shp"))
    else:
        gdf = gpd.read_file(links[category])
    return gdf

@st.cache(allow_output_mutation=True)
def get_some_data(): 
    # Data source: https://www.realtor.com/research/data/
    link_prefix = "https://econdata.s3-us-west-2.amazonaws.com/Reports/"
    url = link_prefix + "Core/RDC_Inventory_Core_Metrics_Zip.csv"
    df = pd.read_csv(url)
    return df
     

gdf = get_geom_data("zip") 
df = get_some_data()
print(df)
st.dataframe(df) 
print(type(gdf)) 
print(gdf) 