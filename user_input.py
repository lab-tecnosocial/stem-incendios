import streamlit as st
import pandas as pd


def user_input():

    on = st.toggle("Datos predeterminados para día con incendio", value=False)
    st.write("")
    if on:
        column_1 = st.number_input(
            ("**Nubosidad Alta [capa alta de nubes]**"), value=87.38)
        column_2 = st.number_input(
            ("**Radiación Solar Directa**"), value=5922)
        column_3 = st.number_input(
            ("**Evapotranspiración de Referencia FAO [2 m]**"), value=6.29)
        column_4 = st.number_input(
            ("**Humedad Relativa [2 m]**"), value=78.22)
        column_5 = st.number_input(
            ("**Humedad del Suelo [28-100 cm de profundidad]**"), value=0.17)
        column_6 = st.number_input(
            ("**Humedad del Suelo [7-28 cm de profundidad]**"), value=0.15)
        column_7 = st.number_input(
            ("**Temperatura del Suelo [100-255 cm de profundidad]**"), value=21.41)
        column_8 = st.number_input(("**Temperatura**"), value=48.76)
        column_9 = st.number_input(
            ("**Temperatura [2 m corregida por elevación]**"), value=31.44)
        column_10 = st.number_input(
            ("**Déficit de Presión de Vapor [2 m]**"), value=32.22)
    else:
        column_1 = st.number_input(
            ("**Nubosidad Alta [capa alta de nubes]**"), value=56.083332)
        column_2 = st.number_input(
            ("**Radiación Solar Directa**"), value=4145)
        column_3 = st.number_input(
            ("**Evapotranspiración de Referencia FAO [2 m]**"), value=3.8626044)
        column_4 = st.number_input(
            ("**Humedad Relativa [2 m]**"), value=79.176346)
        column_5 = st.number_input(
            ("**Humedad del Suelo [28-100 cm de profundidad]**"), value=0.272)
        column_6 = st.number_input(
            ("**Humedad del Suelo [7-28 cm de profundidad]**"), value=0.21)
        column_7 = st.number_input(
            ("**Temperatura del Suelo [100-255 cm de profundidad]**"), value=15.17)
        column_8 = st.number_input(("**Temperatura**"), value=21)
        column_9 = st.number_input(
            ("**Temperatura [2 m corregida por elevación]**"), value=25.449104)
        column_10 = st.number_input(
            ("**Déficit de Presión de Vapor [2 m]**"), value=10.088408)

    data = {
        'Nubosidad Alta [capa alta de nubes]': column_1,
        'Radiación Solar Directa': column_2,
        'Evapotranspiración de Referencia FAO [2 m]': column_3,
        'Humedad Relativa [2 m]': column_4,
        'Humedad del Suelo [28-100 cm de profundidad]': column_5,
        'Humedad del Suelo [7-28 cm de profundidad]': column_6,
        'Temperatura del Suelo [100-255 cm de profundidad]': column_7,
        'Temperatura': column_8,
        'Temperatura [2 m corregida por elevación]': column_9,
        'Déficit de Presión de Vapor [2 m]': column_10
    }

    data_table = pd.DataFrame(data, index=[0])
    return data_table
