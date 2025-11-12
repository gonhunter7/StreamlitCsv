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

st.header("Registro de Avistamientos de Felinos")
st.markdown("Registro de leopardos, panteras y pumas avistados en Argentina desde 1937 hasta el 2012")
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.write(f'Tiene {filas} filas y {columnas} columnas')

nombres_ubic = felinos['genus'].unique()
cant_ubic = len(nombres_ubic)

with st.expander("¿Cuántas especies tiene el Registro de Avistamientos?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles Son las especies en el registro?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas del registro de felinos?"):
    st.write(felinos.columns)
