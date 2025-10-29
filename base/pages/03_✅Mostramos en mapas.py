import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

def agregar_marca_aerop(row):
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['Nombre'],
        icon=folium.Icon()
    ).add_to(mapa)

tab_lagos, tab_felinos = st.tabs(["Mapa Lagos", "Mapa Felinos"])
lagos = pd.read_csv('lagos_arg.csv')

with tab_lagos:
    
    st.title("Mapa Lagos")
    
    st.markdown("Este mapa muestra los lagos de Argentina podiendo filtrar por tamaño")
    mapa = generar_mapa()

    ac1,ac2 = st.columns([0.3, 0.7])
    r_areas = ac1.checkbox("Grandes", key="lagos_grandes")
    if r_areas:
        a_larg = lagos[lagos['Sup Tamaño']=='grande']
        a_larg.apply(agregar_marca_aerop, axis=1)
    r_parques = ac1.checkbox("Medianos", key="lagos_medianos")
    if r_parques:
        a_med = lagos[lagos['Sup Tamaño']=='medio']
        a_med.apply(agregar_marca_aerop, axis=1)    
    r_monu = ac1.checkbox("Pequeños", key="lagos_pequeños")
    if r_monu:
        a_small = lagos[lagos['Sup Tamaño']=='chico']
        a_small.apply(agregar_marca_aerop, axis=1)
    with ac2:
        st_folium(mapa, key='lagos')

felinos = pd.read_csv('felinos_filtrado.csv')

def agregar_marca_aerop(row):
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['stateProvince'],
        icon=folium.Icon()
    ).add_to(mapa)


with tab_felinos:
    st.title("Mapa Felinos")

    st.markdown("Este mapa muestra los avistamientos de felinos de Argentina, podiendo filtrar por especie")
    
    mapa = generar_mapa()

    ac1, ac2 = st.columns([0.3, 0.7])

    genus_unicos = felinos['genus'].unique()[:3]

    r_genus1 = ac1.checkbox(genus_unicos[0], key="felinos_genus1")
    if r_genus1:
        felinos[felinos['genus'] == genus_unicos[0]].apply(agregar_marca_aerop, axis=1)

    r_genus2 = ac1.checkbox(genus_unicos[1], key="felinos_genus2")
    if r_genus2:
        felinos[felinos['genus'] == genus_unicos[1]].apply(agregar_marca_aerop, axis=1)

    r_genus3 = ac1.checkbox(genus_unicos[2], key="felinos_genus3")
    if r_genus3:
        felinos[felinos['genus'] == genus_unicos[2]].apply(agregar_marca_aerop, axis=1)

    with ac2:
        st_folium(mapa, key='felinos')
