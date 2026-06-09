# Debe direccionar VS Code a la carpeta con los archivos:
# 1.- Archivo
# 2.- Abrir carpeta. Debe dar click en la carpeta que contiene los archivos de interés
#3.- A la izquierda, en el explorador deberá poder visualizar todos los archivos
#------------------------------------------------------------------------------------------------

# CÓDIGO STREAMLIT
# Ir a:   Ver/Terminal
# Crea un ambiente virtual (puedes usar otro nombre en lugar de 'venv'): coloca este código
#   python -m venv venv

#---------------------------------------------------------------------------------------
# Luego de crear el ambiente virtual, lo activas
#   .\venv\Scripts\activate   # En Windows
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# Cuando vuelva a iniciar sesión, debe volver a activar el ambiente virtual, ya no lo debe crear.
# En este caso debes abrir la carpeta con los archivos del caso.
#---------------------------------------------------------------------------------------------


# Instala la versión específica de scikit-learn
#   pip install scikit-learn==1.2.2
# Instala otras dependencias, incluyendo Streamlit
#  pip install streamlit pandas joblib
#-------------------------------------------------------------------------------------------------
# Desde la segunda vez: hacer:
# Si da error, debes ir a PowerShell de Window y:
#      Get-ExecutionPolicy                           Si es Restricted; ejecuta
#      Set-ExecutionPolicy RemoteSigned              Colocar Sí
# En consola de VSC:  .\venv\Scripts\activate



import streamlit as st
import pandas as pd
from joblib import load
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
#import pyautogui

# Cargar el modelo de regresión
regressor = load('Modelopipeline.joblib')

# Cargar el encoder
#with open('encoderpipeline.pickle', 'rb') as f:
#    encoder = pickle.load(f)

# Inicializar variables
sexo = "1"
estado_civil= "1"
horas_trabajadas= 24
categoria_ocupacional="522"
actividad_empresa="5629"
dominio= "1"

# Streamlit app
st.title("Modelo de Regresión")
st.markdown("##### Debe seleccionar las opciones, de lo contrario la predicción será incorrecta.")

# Sidebar para la entrada del usuario
st.sidebar.header("Campos a Evaluar el ingreso de la Persona")

# Entrada del usuario para RD_Spend
edad = st.sidebar.number_input("**Edad (Min=18, Max=110)**", min_value=18.0, value=float(edad))

st.sidebar.markdown("<h1 style='font-size: 24px;'>Sexo</h1>", unsafe_allow_html=True)
sexo = st.sidebar.selectbox("sexo", ["Masculino", "Femenino"], index=["1", "2"].index(sexo))

st.sidebar.markdown("<h1 style='font-size: 24px;'>Estado civil</h1>", unsafe_allow_html=True)
estado_civil = st.sidebar.selectbox("estado_civil", ["Soltero", "Casado"], index=["1", "2"].index(estado_civil))

horas_trabajadas = st.sidebar.number_input("**Horas trabajadas por semana (Min=24, Max=48)**", min_value=24.0, value=float(horas_trabajadas))

st.sidebar.markdown("<h1 style='font-size: 24px;'>Categoria ocupacional</h1>", unsafe_allow_html=True)
categoria_ocupacional = st.sidebar.selectbox("categoria_ocupacional", ["barmanes y trabajadores asimilados", "explotadores forestales, trabajadores forestales clasificados y afines"], index=["522", "615"].index(categoria_ocupacional))

st.sidebar.markdown("<h1 style='font-size: 24px;'>Actividad empresa</h1>", unsafe_allow_html=True)
actividad_empresa = st.sidebar.selectbox("actividad_empresa", ["Actividad 01", "Actividad 02"], index=["5629", "150"].index(actividad_empresa))

st.sidebar.markdown("<h1 style='font-size: 24px;'>Dominio</h1>", unsafe_allow_html=True)
dominio = st.sidebar.selectbox("dominio", ["Costa Norte", "Costa Centro","Costa Sur","Sierra Norte","Sierra Centro"], index=["1","2","3","4","5"].index(dominio))

# Función para resetear las entradas
def reset_inputs():
    global edad, sexo, estado_civil, horas_trabajadas, categoria_ocupacional, actividad_empresa, dominio
    edad = 18
    horas_trabajadas = 24
    sexo = "Masculino"
    estado_civil = "Soltero"
    categoria_ocupacional = "barmanes y trabajadores asimilados"
    actividad_empresa = "Actividad 01"
    dominio = "Costa Norte"

# Botón para predecir
if st.sidebar.button("Predecir"):
    # Validar las entradas
    if all(isinstance(val, (int, float)) and val >= 0 for val in [edad, sexo, estado_civil, horas_trabajadas, categoria_ocupacional, actividad_empresa, dominio]):
        # Crear un DataFrame con las entradas del usuario
        obs = pd.DataFrame({
            'Edad': [edad],
            'Sexo': [sexo],
            'Estado civil': [estado_civil],
            'Horas trabajadas por semana': [horas_trabajadas],
            'Categoria ocupacional': [categoria_ocupacional],
            'Actividad empresa': [actividad_empresa],
            'Dominio': [dominio]
        })

        # Mostrar el DataFrame de entradas para depuración
        st.write("DataFrame de Entradas:")
        st.write(obs)

        #----------------------Pipeline-------------------------
        # Predecir usando el modelo
        target = regressor.predict(obs)

        # Mostrar la predicción con un tamaño de fuente grande usando markdown
        st.markdown(f'<p style="font-size: 40px; color: green;">La predicción del Ingreso será: ${target[0]:,.2f}</p>', unsafe_allow_html=True)

    else:
        st.warning("Rellene todos los espacios en blanco")

# Colocar el botón "Resetear" debajo del botón "Predecir"
if st.sidebar.button("Resetear"):
    # Resetear inputs
    reset_inputs()




#	edad	sexo	estado_civil	horas_trabajadas	categoria_ocupacional	actividad_empresa	dominio	    ingreso	    Profit_predict
#	63	    2	        5	            3	                522	                5629	            5	            14039.126953	    11612.434731
#	42	    1	        2	            2	                615	                150	                5	            5766.923340	        10687.291158
#	33	    1	        1	            4	                885	                2396	            5	            19948.009766	    13665.625699



""" Sexo:
○ Hombre
○ Mujer

Estado civil:
○ Soltero
○ Casado
○ Conviviente
○ Viudo
○ Divorciado
○ Separado

Nivel educativo:
○ Sin nivel
○ Primaria incompleta
○ Primaria completa
○ Secundaria incompleta
○ Secundaria completa
○ Superior técnica incompleta
○ Superior técnica completa
○ Universitaria incompleta
○ Universitaria completa
○ Posgrado

Horas trabajadas por semana:
_______

Categoría ocupacional:
○ Empleador
○ Independiente
○ Empleado
○ Obrero
○ TFNR
○ Trabajador del hogar

Tamaño de empresa:
○ 1 trabajador
○ 2-10 trabajadores
○ 11-50 trabajadores
○ 51+ trabajadores

Dominio:
○ Costa Norte
○ Costa Centro
○ Costa Sur
○ Sierra Norte
○ Sierra Centro
○ Sierra Sur
○ Selva
○ Lima Metropolitana """




# Cambiar los valores.
# Para asignar valores: ver los rangos de las cuantitativas ( MÍNIMO --MÁXIMO)
# eso determinan  cómo predice el modelo. 

#  streamlit run streamlitpipelines.py       en la consola
#  pip freeze > requirements.txt