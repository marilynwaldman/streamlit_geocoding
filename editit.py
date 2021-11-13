import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
@st.cache()
def get_data():
    
    df = pd.DataFrame({'street1': ['3180 E 6th Ave',
                            '1364 Reese St',
                           '81 Ball Ln',
                           '7405 Dellwood Rd NE',
                           '4945 Twin Lakes Rd'],
                        'city' : ['Durango',
                           'Silverton',
                           'Durango,CO',
                           'Albuquerque',
                           'Boulder']})
    #colnames=["Name","Street_address","City","State","ZIPcode","full_address"]                        
    df.to_csv("./myaddresses.csv")
    df = pd.read_csv('./myaddresses.csv',header=0) 
    #print(list(df.columns))                        
    return df

if __name__ == "__main__":
    reload_data = False
    df = get_data()
    #st.set_page_config(page_title="Netflix Shows", layout="wide") 
    st.title("Netlix shows analysis")

    height = st.sidebar.slider('Height', min_value=100, max_value=800, value=400)

    st.subheader("Editable Grids")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_column("Name", editable=True)
    for col in df.columns:
        gb.configure_column(col, editable=True)
    gridOptions = gb.build()

    grid_return = AgGrid(df,
        key='grid1',
        gridOptions=gridOptions,
        editable=True,
        height=height, 
        fit_columns_on_grid_load=True
    )
    st.text("Grid  Return")
    #print("before ************")
    #print(df)

    st.write(grid_return['data'])


    st.sidebar.markdown("example controls:")
    use_fixed_key = st.sidebar.checkbox("Use fixed key in AgGrid call", value=True)


