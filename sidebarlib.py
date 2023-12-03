import streamlit as st
import pandas as pd


def user_input():
  
    on = st.sidebar.toggle("Datos default para dia con incendio", value=False)
    st.write("")
    if on:
        column_1 = st.sidebar.number_input(("**Cloud Cover High [high cld lay]**"), value=87.38)
        column_2 = st.sidebar.number_input(("**Direct Shortwave Radiation**"), value=5922)
        column_3 = st.sidebar.number_input(("**FAO Reference Evapotranspiration [2 m]**"), value=6.29)
        column_4 = st.sidebar.number_input(("**Relative Humidity [2 m]**"), value=78.22)
        column_5 = st.sidebar.number_input(("**Relative Humidity [2 m]_1**"), value=20.71)
        column_6 = st.sidebar.number_input(("**Relative Humidity [2 m]_2**"), value=48.08)
        column_7 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]**"), value=0.17)
        column_8 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]_10**"), value=0.17)
        column_9 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]_9**"), value=0.17)
        column_10 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]**"), value=0.15)
        column_11 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]_7**"), value=0.15)
        column_12 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]_8**"), value=0.15)
        column_13 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]**"), value=21.41)
        column_14 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]_3**"), value=21.36)
        column_15 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]_4**"), value=21.38)
        column_16 = st.sidebar.number_input(("**Temperature**"), value=48.76)
        column_17 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]**"), value=31.44)
        column_18 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]_1**"), value=31.44)
        column_19 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]_2**"), value=11.76)
        column_20 = st.sidebar.number_input(("**Temperature_5**"), value=11.76)
        column_21 = st.sidebar.number_input(("**Temperature_6**"), value=26.32)
        column_22 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]**"), value=32.22)
        column_23 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]_1**"), value=3.75)
        column_24 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]_2**"), value=15.04)
    else:
        column_1 = st.sidebar.number_input(("**Cloud Cover High [high cld lay]**"), value=56.083332)
        column_2 = st.sidebar.number_input(("**Direct Shortwave Radiation**"), value=4145)
        column_3 = st.sidebar.number_input(("**FAO Reference Evapotranspiration [2 m]**"), value=3.8626044)
        column_4 = st.sidebar.number_input(("**Relative Humidity [2 m]**"), value=79.176346)
        column_5 = st.sidebar.number_input(("**Relative Humidity [2 m]_1**"), value=22.599285)
        column_6 = st.sidebar.number_input(("**Relative Humidity [2 m]_2**"), value=53.568966)
        column_7 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]**"), value=0.272)
        column_8 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]_10**"), value=0.27166668)
        column_9 = st.sidebar.number_input(("**Soil Moisture [28-100 cm down]_9**"), value=0.271)
        column_10 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]**"), value=0.21)
        column_11 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]_7**"), value=0.209)
        column_12 = st.sidebar.number_input(("**Soil Moisture [7-28 cm down]_8**"), value=0.20966671)
        column_13 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]**"), value=17.17)
        column_14 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]_3**"), value=17.16)
        column_15 = st.sidebar.number_input(("**Soil Temperature [100-255 cm down]_4**"), value=17.165834)
        column_16 = st.sidebar.number_input(("**Temperature**"), value=34.45)
        column_17 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]**"), value=25.449104)
        column_18 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]_1**"), value=9.179106)
        column_19 = st.sidebar.number_input(("**Temperature [2 m elevation corrected]_2**"), value=16.546602)
        column_20 = st.sidebar.number_input(("**Temperature_5**"), value=3.81)
        column_21 = st.sidebar.number_input(("**Temperature_6**"), value=14.822918)
        column_22 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]**"), value=22.088408)
        column_23 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]_1**"), value=2.0883007)
        column_24 = st.sidebar.number_input(("**Vapor Pressure Deficit [2 m]_2**"), value=9.108302)
    
    
    data = {
        "Cloud Cover High [high cld lay]": column_1, 
        "Direct Shortwave Radiation": column_2, 
        "FAO Reference Evapotranspiration [2 m]": column_3, 
        "Relative Humidity [2 m]": column_4, 
        "Relative Humidity [2 m]_1": column_5, 
        "Relative Humidity [2 m]_2": column_6, 
        "Soil Moisture [28-100 cm down]": column_7, 
        "Soil Moisture [28-100 cm down]_10": column_8,
        "Soil Moisture [28-100 cm down]_9": column_9,
        "Soil Moisture [7-28 cm down]": column_10, 
        "Soil Moisture [7-28 cm down]_7": column_11,
        "Soil Moisture [7-28 cm down]_8": column_12, 
        "Soil Temperature [100-255 cm down]": column_13,
        "Soil Temperature [100-255 cm down]_3": column_14, 
        "Soil Temperature [100-255 cm down]_4": column_15, 
        "Temperature": column_16, 
        "Temperature [2 m elevation corrected]": column_17,
        "Temperature [2 m elevation corrected]_1": column_18, 
        "Temperature [2 m elevation corrected]_2": column_19,
        "Temperature_5": column_20,
        "Temperature_6": column_21, 
        "Vapor Pressure Deficit [2 m]": column_22,
        "Vapor Pressure Deficit [2 m]_1": column_23, 
        "Vapor Pressure Deficit [2 m]_2": column_24,
        }
    
    data_table = pd.DataFrame(data, index=[0])
    return data_table