import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
from st_aggrid.shared import JsCode

#@st.cache()
def get_data():
    
    df3 = pd.DataFrame({'street': ['3180 E 6th Ave',
                            '1364 Reese St',
                           '81 Ball Ln',
                           '7405 Dellwood Rd NE',
                           '4945 Twin Lakes Rd'],
                        'city' : ['Durango',
                           'Silverton',
                           'Durango,CO',
                           'Albuquerque',
                           'Boulder'],
                        'zip' : ['81310', '81433', '81301', '87110', '980301'] 
                          })
    #
    # colnames=["Name","Street_address","City","State","ZIPcode","full_address"]                        
    #df3.to_csv("./myaddresses.csv",index=False)
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
    cellsytle_jscode = JsCode(
         """
    function(params) {
         if (params.value.includes('Silverton')) {
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

    cellsytle_jszipcode = JsCode(
         """

    function(params) {

        if(/^([0-9]{5}|[a-zA-Z][a-zA-Z ]{0,49})$/.test(params.value)){
            return {
                 'color': 'black',
                 'backgroundColor': 'white'
             }
        }
        else {
             return {
                 'color': 'black',
                 'backgroundColor': 'lightgrey'
             }
        } 
         
    };
     """
    )
    
    gb = GridOptionsBuilder.from_dataframe(df)
    
    gb.configure_pagination()
    
   
    for col in df.columns:
        gb.configure_column(col, editable=True)
    gb.configure_column("city", cellStyle=cellsytle_jscode)  
    gb.configure_column("zip", cellStyle=cellsytle_jszipcode)  
    gridOptions = gb.build()
    with st.form('example form') as f:
         grid_return = AgGrid(df,
             key='grid1',
             gridOptions=gridOptions,
             editable=True,
             height=height, 
             fit_columns_on_grid_load=True,
             allow_unsafe_jscode=True
         )
         button = st.form_submit_button()
    #st.text("Grid  Return")
    #print("before ************")
    #print(df)
    #grid_return['data'].to_csv("./myaddresses.csv")
    if button:
         print(grid_return['data'])
         print(grid_return['data'].dtypes)
         grid_return['data'].to_csv("./myaddresses.csv",index=False)
         st.write(grid_return['data'])


    st.sidebar.markdown("example controls:")
    use_fixed_key = st.sidebar.checkbox("Use fixed key in AgGrid call", value=True)


