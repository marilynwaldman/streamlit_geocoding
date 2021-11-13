import streamlit as st
row1_col1, row1_col2 = st.columns([3, 1.5])
width = 800
height = 600
layers = None

with row1_col1:
    st.write('hi')

with row1_col2:
    st.write('bye')        


