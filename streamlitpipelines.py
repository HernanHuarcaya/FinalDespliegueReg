import streamlit as st
import pandas as pd
from joblib import load
import numpy as np

regressor = load('Modelopipeline.joblib')

# Valores iniciales
defaults = {
    "edad": 18, "sexo": 1, "estado_civil": 1, "nivel_educativo":1,
    "horas_trabajadas": 24, "categoria_ocupacional": 522,
    "actividad_empresa": 5629, "dominio": 1
}

st.title("Modelo de Regresión - Trabajo final")
st.markdown("##### Grupo: 2")
st.markdown("##### ---------------------------------------------------------------------------")
st.markdown("##### Debe seleccionar las opciones relacionadas a la persona, para generar la predicción de su ingreso neto.")
st.sidebar.header("Campos a Evaluar")

# Edad
edad = st.sidebar.number_input("Edad (Min=18, Max=110)", min_value=18, max_value=110, value=defaults["edad"])

# Sexo
sexo_map = {"Masculino": 1, "Femenino": 2}
sexo = sexo_map[st.sidebar.selectbox("Sexo", list(sexo_map.keys()))]

# Estado civil
ec_map = {"Conviviente": 1, "Casado(a)": 2, "Viudo(a)": 3, "Divorciado(a)": 4, "Separado(a)": 5, "Soltero(a)": 6}
estado_civil = ec_map[st.sidebar.selectbox("Estado civil", list(ec_map.keys()))]

# Nivel educativo
ec_map = {"Sin nivel": 1, "Educacion iniciañ": 2, "primaria incompleta": 3, "primaria completa": 4, "secundaria incompleta": 5, "secundaria completa": 6}
nivel_educativo = ec_map[st.sidebar.selectbox("Nivel educativo", list(ec_map.keys()))]

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
        'nivel_educativo': [nivel_educativo],
        'horas_trabajadas': [horas_trabajadas],
        'categoria_ocupacional': [categoria_ocupacional],
        'actividad_empresa': [actividad_empresa],
        'dominio': [dominio]
    })
    st.write("DataFrame de Entradas:")
    st.write(obs)

    target = regressor.predict(obs)      
    ingreso_mensual = target[0] / 12  
    st.markdown(f'<p style="font-size: 40px; color: green;">El ingreso neto anual proyectado es de: S/ {target[0]:,.2f}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 40px; color: green;">El ingreso neto mensual proyectado es de: S/ {ingreso_mensual:,.2f}</p>', unsafe_allow_html=True)

# Resetear
if st.sidebar.button("Resetear"):
    st.session_state.clear()
    st.rerun()
