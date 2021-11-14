import streamlit as st
#import numpy as np
import pandas as pd
import time 

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
from st_aggrid.shared import JsCode


@st.cache()
def get_data(file):
    df  = pd.DataFrame() 
    
    #
    # colnames=["Name","Street_address","City","State","ZIPcode","full_address"]                        
    #df3.to_csv("./myaddresses.csv",index=False) 
    df = pd.read_csv(file, low_memory=False)
    with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
    st.write(df.head())
    st.write(df.shape)
    #print(list(df.columns))                        
    return df

if __name__ == "__main__":
    reload_data = False
    df  = pd.DataFrame() 
    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        
        df = pd.read_csv(file, low_memory=False)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
            
    #st.set_page_config(page_title="Netflix Shows", layout="wide") 
    st.title("AG Grid Example")

    height = st.sidebar.slider('Height', min_value=100, max_value=800, value=200)

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
             fit_columns_on_grid_load=False,
             allow_unsafe_jscode=True
         )
         button = st.form_submit_button("Save Changes")
    
    if button:
         df = grid_return['data']
         st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv',file_name='address.csv')
         #st.write(df)




