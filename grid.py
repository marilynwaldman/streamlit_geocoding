from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("./addresses.csv")  
gb = GridOptionsBuilder.from_dataframe(shows)

gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gridOptions = gb.build()

AgGrid(shows, gridOptions=gridOptions, enable_enterprise_modules=True)
