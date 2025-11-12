
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

lagos = pd.read_csv('lagos_arg.csv')
felinos = pd.read_csv('felinos_filtrado.csv')

st.title("Gráfico")

st.subheader("Cantidad de Lagos por Provincia")

# Mostrar las columnas para verificar nombres
st.write("Columnas del dataset:", lagos.columns.tolist())

# Crear el gráfico de barras
if 'Ubicación' in lagos.columns:
    conteo_tipos = lagos['Ubicación'].value_counts()
    fig, ax = plt.subplots()
    conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel('Provincia')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad de Lagos por provincia')
    st.pyplot(fig)
else:
    st.error("❌ No se encontró la columna 'Ubicación' en el CSV.")

st.title("Gráfico De Felinos en Argentina")



# Crear el gráfico de barras
if 'species' in felinos.columns:
    conteo_tipos = felinos['species'].value_counts()
    fig, ax = plt.subplots()
    conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel('Especies')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad de Felinos por Sub especie')
    st.pyplot(fig)
else:
    st.error("❌ No se encontró la columna 'Ubicación' en el CSV.")
