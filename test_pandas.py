import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')

sigla = st.text_input('Digite a sigla do partido')
if sigla:
    st.dataframe(df[df['sigla']==sigla.upper()])
