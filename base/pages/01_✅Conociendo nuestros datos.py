import pandas as pd
import streamlit as st

lagos = pd.read_csv('lagos_arg.csv')
felinos = pd.read_csv('felinos_filtrado.csv')

st.title("Parte 1")

st.header("Datos que encontraron (Lagos)")
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = lagos.shape
    st.write(f'Tiene {filas} filas y {columnas} columnas')
    
nombres_ubic = lagos['Sup Tamaño'].unique()
cant_ubic = len(nombres_ubic)

with st.expander("¿Cuántos son los valores únicos de la columna **Sup Tamaño**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **Sup Tamaño**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas?"):
    st.write(lagos.columns)

st.header("Datos que encontraron (Felinos)")
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.write(f'Tiene {filas} filas y {columnas} columnas')

nombres_ubic = felinos['genus'].unique()
cant_ubic = len(nombres_ubic)

with st.expander("¿Cuántos son los valores únicos de la columna **genus**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **genus**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas?"):
    st.write(felinos.columns)
