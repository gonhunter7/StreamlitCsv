import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

felinos = pd.read_csv('felinos_filtrado.csv')

felinos['year'] = pd.to_numeric(felinos['year']).astype('Int64')
felinos['month'] = pd.to_numeric(felinos['month']).astype('Int64')
felinos['day'] = pd.to_numeric(felinos['day']).astype('Int64')

st.title("Felinos Avistados y registrados Cronologicamente")

st.markdown("Puede filtrar por Año y mes para ver los momentos especificos en los que se avistaron los felinos.")
st.markdown("A mas reciente sea la fecha (Mas cercana al siglo XXI), Mas felinos registrados habra. Tal como se puede ver cuando se deja el grafico en Todos. ")

año_seleccionado = st.selectbox(
    "Selecciona el Año",
    ["(Todos)"] + sorted([int(a) for a in felinos['year'].dropna().unique()])
)
# Dropna quita Valores Nulos. Sorted ordena
if año_seleccionado != "(Todos)":
    felinos = felinos[felinos['year'] == int(año_seleccionado)]

mes_seleccionado = st.selectbox(
    "Selecciona el Mes",
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

#Dependiendo que seleccione el usuario, se cambian las variables nivel, titulo y xlabel
#Para ajustar el grafico a día, mes o año. 

conteo = felinos[nivel].value_counts().sort_index()

#sort_index ordena por indice dps de contar (Util en fecha con años y meses)

fig, ax = plt.subplots()

#subplots hace el grafico con eje X y eje Y automaticamente, junto con un fig que es el div del grafico

conteo.plot(kind='bar', ax=ax)
ax.set_title(titulo)
ax.set_xlabel(xlabel)
ax.set_ylabel("Cantidad de avistamientos")

st.pyplot(fig)
