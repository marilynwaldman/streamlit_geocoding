# test download file on streaamlit cloud

import time 
import base64

import streamlit as st
import pandas as pd 

def getfile():
    df  = pd.DataFrame()  
    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        df = pd.read_csv(file, low_memory=False)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
        st.write(df.head())
        st.write(df.shape)

    return df





def main():
    import pandas as pd

    st.set_option('deprecation.showfileUploaderEncoding', False)

    df = getfile()
    st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv',file_name='addres.csv')
    

        
    
if __name__ == "__main__":
    main()



