import numpy as np
import pandas as pd
import geopandas as gpd
import streamlit as st
import folium as fl
import streamlit_folium as sf
import branca.colormap as cm


MESSAGE_SIZE_LIMIT = 150*int(1e6) #150 MB

st.title('Current Weather Warnings')

#Read in weather info

weatherdf = gpd.read_file('current_all/current_all.shp')
#weatherdf = gpd.read_file('current_warnings/current_warnings.shp')

weatherdf = weatherdf.drop(columns=['PHENOM','SIG','WFO','EVENT','ONSET','ENDS','CAP_ID','MSG_TYPE','VTEC'])

st.write(weatherdf.head())

#Assign an integer value to each unique warning
#so they will plot in different colors later

wxwarnings = {}
k = 0
for w in weatherdf['PROD_TYPE'].unique():
    wxwarnings[w]=k
#    print(w,k)
    k += 10

st.write(wxwarnings)

#Get min and max values of wxwarning id codes
all_values = wxwarnings.values()

max_wxwarnings = max(all_values)
min_wxwarnings = min(all_values)

st.write('wxwarnings:',min_wxwarnings,max_wxwarnings)

# Now create an column PROD_ID which duplicates PROD_TYPE
weatherdf["PROD_ID"]=weatherdf['PROD_TYPE']

# and fill with values from the dictionary wxwarnings
weatherdf['PROD_ID'].replace(wxwarnings,inplace=True)

st.write(weatherdf.head())

#verify no missing/Nan
missing = weatherdf.isnull().sum().sum()
st.write('Number of missing values:',missing)

#explicitly create an index column with each entry having a unique value for indexing
weatherdf['UNIQUE_ID']=weatherdf.index

st.write(weatherdf.head(10))

# write weatherdf to a geoJson file
weatherdf.to_file("weatherdf.geojson", driver='GeoJSON')

st.write('wrote GeoJSON file')

# Use branca.colormap instead of choropleth


#create a b/w map of CONUS
mbr = fl.Map(location=[30.0,-95.0],zoom_start=4,tiles="Stamen Toner")

colormap = cm.linear.YlGnBu_09.scale(min_wxwarnings,max_wxwarnings)

colormap

#Add weather data to map with mouseover (this will take a few minutes), include tooltip

fl.GeoJson(weatherdf,
               style_function = lambda x: {"weight":0.5, 
                            'color':'red',
                            'fillColor':colormap(x['properties']['PROD_ID']), 
                            'fillOpacity':0.5
               },
           
               highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.25, 
                                'weight': 0.1
               },
               
               tooltip=fl.GeoJsonTooltip(
                   fields=['PROD_TYPE','ISSUANCE','EXPIRATION'], 
                   aliases=['Hazard', 'Starts','Expires'],
                   labels=True,
                   localize=True
               ),
              ).add_to(mbr)

sf.folium_static(mbr)

mbr.save('wxwarning.html')

st.write('Done')
