import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder





    
df = pd.DataFrame( ['3180 E 6th Ave,Durango,CO,81301',
                            '1364 Reese St, Silverton,CO,81433',
                           '81 Ball Ln,Durango,CO,81301'])
print("hello")
print(df)

st.dataframe(df)