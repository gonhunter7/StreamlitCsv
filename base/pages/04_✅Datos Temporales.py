import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

felinos = pd.read_csv('felinos_filtrado.csv')

felinos['year'] = pd.to_numeric(felinos['year']).astype('Int64')
felinos['month'] = pd.to_numeric(felinos['month']).astype('Int64')
felinos['day'] = pd.to_numeric(felinos['day']).astype('Int64')

st.title("Datos Temporales")

año_seleccionado = st.selectbox(
    "Selecciona Año",
    ["(Todos)"] + sorted([int(a) for a in felinos['year'].dropna().unique()])
)

if año_seleccionado != "(Todos)":
    felinos = felinos[felinos['year'] == int(año_seleccionado)]

mes_seleccionado = st.selectbox(
    "Selecciona Mes",
    ["(Todos)"] + sorted([int(m) for m in felinos['month'].dropna().unique()])
)

if mes_seleccionado != "(Todos)":
    felinos = felinos[felinos['month'] == int(mes_seleccionado)]

if año_seleccionado == "(Todos)":
    nivel = "year"
    titulo = "Avistamientos por Año"
    xlabel = "Año"

elif mes_seleccionado == "(Todos)":
    nivel = "month"
    titulo = f"Avistamientos por Mes en {año_seleccionado}"
    xlabel = "Mes"

else:
    nivel = "day"
    titulo = f"Avistamientos por Día en {año_seleccionado}-{mes_seleccionado:02d}"
    xlabel = "Día"

conteo = felinos[nivel].value_counts().sort_index()

fig, ax = plt.subplots()
conteo.plot(kind='bar', ax=ax)
ax.set_title(titulo)
ax.set_xlabel(xlabel)
ax.set_ylabel("Cantidad de avistamientos")

st.pyplot(fig)
