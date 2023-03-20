import streamlit as st
import pandas as pd

# Linechart dengan dataframe yang dibuat manual
st.header("Data Pangan dari Tahun pertahun")

df = pd.DataFrame({
  'year': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
  'sales': [46.7, 50.6, 51.3, 54.8, 62.6, 59.5, 59.2, 60.2]
}, index=[1,2,3,4,5,6,7,8])

st.write('Tabel:')
st.dataframe(df, width=400)
st.markdown('#')

st.write('Barchart:')
st.bar_chart(df, x='year')