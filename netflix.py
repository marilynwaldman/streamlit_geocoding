# https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("./netflix_titles.csv")

from st_aggrid.shared import JsCode

# ... 

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('nan')) {
        return {
            'color': 'white',
            'backgroundColor': 'darkred'
        }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
"""
)

# add this
gb = GridOptionsBuilder.from_dataframe(shows)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_column("country", cellStyle=cellsytle_jscode)
gb.configure_column("director", cellStyle=cellsytle_jscode)
gb.configure_pagination()
gridOptions = gb.build()


data = AgGrid(shows, 
              gridOptions=gridOptions, 
              enable_enterprise_modules=True, 
              allow_unsafe_jscode=True, 
              update_mode=GridUpdateMode.SELECTION_CHANGED)
