import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder

@st.cache()
def get_data():
    
    df = pd.DataFrame({'a': ['3180 E 6th Ave,Durango,CO,81301',
                            '1364 Reese St, Silverton,CO,81433',
                           '81 Ball Ln,Durango,CO,81301',
                           '7405 Dellwood Rd NE, Albuquerque, NM,87110',
                           '4945 Twin Lakes Rd, Boulder, CO, 80301']})
    return df

if __name__ == "__main__":    
    data = get_data()
    reload_data = False
    gb = GridOptionsBuilder.from_dataframe(data)
    #make all columns editable
    gb.configure_columns(list('a'), editable=True)

    #Create a calculated column that updates when data is edited. Use agAnimateShowChangeCellRenderer to show changes   
    #gb.configure_column('row total', valueGetter='Number(data.a) + Number(data.b) + Number(data.c) + Number(data.d) + Number(data.e)', cellRenderer='agAnimateShowChangeCellRenderer', editable='false', type=['numericColumn'])
    go = gb.build()
    height=3

    st.markdown(f"Grid was called as: <br>```AgGrid(..., reload_data={reload_data})``` <br>", unsafe_allow_html=True)
    ag = AgGrid(
        data, 
        gridOptions=go, 
        fit_columns_on_grid_load=True,
        height=height 
    )    
    
    

    st.subheader("Returned Data")
    st.dataframe(ag['data'])

    st.subheader("Grid Options")
    st.write(go)