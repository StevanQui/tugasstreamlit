import streamlit as st
import pandas as pd
import numpy as np

# Checkbox Widget
np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2018', '2019', '2020', '2021', '2022'],
  'Produk1': np.random.randint(100, 1000, 5),
  'Produk2': np.random.randint(100, 1000, 5),
  'Produk3': np.random.randint(100, 1000, 5)
  }, index=[1,2,3,4,5])

st.subheader('Table:')
st.dataframe(df)

show = st.checkbox('Show Bar_chart')
if show:
  st.markdown('#')
  st.subheader('barchart:')
  st.bar_chart(df.set_index('Tahun'))