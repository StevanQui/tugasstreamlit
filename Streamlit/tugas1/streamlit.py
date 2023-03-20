import streamlit as st
import pandas as pd

# Linechart dengan dataframe yang dibuat manual
st.header("Data Pariwisata Tahun 2022 - 2023")

df = pd.DataFrame({
  'year': ['Jan/22', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des', 'Jan/23'],
  'sales': [121.978, 105.195, 142.007, 213.381, 333.109, 452.995, 598.164, 624.256, 648.901, 678.901, 657.269, 895.121, 735.947]
}, index=[1,2,3,4,5,6,7,8,9,10,11,12,13])

st.write('Tabel:')
st.dataframe(df, width=1000)
st.markdown('#')

st.write('Linechart:')
st.line_chart(df, x='year')