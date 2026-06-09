import streamlit as st
import pandas as pd
from joblib import load
import numpy as np

regressor = load('Modelopipeline.joblib')

# Valores iniciales
defaults = {
    "edad": 18, "sexo": 1, "estado_civil": 1,
    "horas_trabajadas": 24, "categoria_ocupacional": 522,
    "actividad_empresa": 5629, "dominio": 1
}

st.title("Modelo de Regresión - Trabajo final")
st.markdown("##### Debe seleccionar las opciones, de lo contrario la predicción será incorrecta.")
st.sidebar.header("Campos a Evaluar")

# Edad
edad = st.sidebar.number_input("Edad (Min=18, Max=110)", min_value=18, max_value=110, value=defaults["edad"])

# Sexo
sexo_map = {"Masculino": 1, "Femenino": 2}
sexo = sexo_map[st.sidebar.selectbox("Sexo", list(sexo_map.keys()))]

# Estado civil
ec_map = {"Soltero": 1, "Casado": 2}
estado_civil = ec_map[st.sidebar.selectbox("Estado civil", list(ec_map.keys()))]

# Horas trabajadas
horas_trabajadas = st.sidebar.number_input("Horas trabajadas (Min=24, Max=48)", min_value=24, max_value=48, value=defaults["horas_trabajadas"])

# Categoría ocupacional
cat_map = {
    "Barmanes y trabajadores asimilados": 522,
    "Explotadores forestales y afines": 615
}
categoria_ocupacional = cat_map[st.sidebar.selectbox("Categoría ocupacional", list(cat_map.keys()))]

# Actividad empresa
act_map = {"Actividad 01": 5629, "Actividad 02": 150}
actividad_empresa = act_map[st.sidebar.selectbox("Actividad empresa", list(act_map.keys()))]

# Dominio
dom_map = {"Costa Norte": 1, "Costa Centro": 2, "Costa Sur": 3, "Sierra Norte": 4, "Sierra Centro": 5}
dominio = dom_map[st.sidebar.selectbox("Dominio", list(dom_map.keys()))]

# Predecir
if st.sidebar.button("Predecir"):
    obs = pd.DataFrame({
        'edad': [edad],
        'sexo': [sexo],
        'estado_civil': [estado_civil],
        'horas_trabajadas': [horas_trabajadas],
        'categoria_ocupacional': [categoria_ocupacional],
        'actividad_empresa': [actividad_empresa],
        'dominio': [dominio]
    })
    st.write("DataFrame de Entradas:")
    st.write(obs)

    target = regressor.predict(obs)
    st.markdown(f'<p style="font-size: 40px; color: green;">La predicción del Ingreso será: S/ {target[0]:,.2f}</p>', unsafe_allow_html=True)

# Resetear
if st.sidebar.button("Resetear"):
    st.session_state.clear()
    st.rerun()
