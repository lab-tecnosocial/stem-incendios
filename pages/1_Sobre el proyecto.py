import streamlit as st


st.title("Sobre el Proyecto")
st.image("cerrotunari.jpg")


url = "https://www.meteoblue.com/es/tiempo/historyclimate/weatherarchive/cochabamba_bolivia_3919968"

st.write("""
        Somos un equipo denominado TecnoBanda, representando al Colegio San Agustín en las Olimpiadas STEM+ 2023 en Cochabamba, Bolivia. Nuestra meta primordial radica en la creación de una plataforma capaz de emplear inteligencia artificial para predecir y evaluar el riesgo de incendios. Este proyecto busca no solo facilitar las labores de los bomberos, sino también proporcionar una herramienta eficiente para el control y mitigación de incendios, al alcance de toda la población y sobre todo de las instituciones que requieren toda la ayuda posible para contrarrestar este problema latente en nuestra sociedad.

        El enfoque de este prototipo se centra en representar el riesgo de incendios en todo el departamento de Cochabamba. Sin embargo, su aplicabilidad se extiende para ser implementado en diferentes municipios y departamentos mediante la sustitución de la base de datos manteniendo la estructura de columnas y los códigos de programación.

        Los datos pertinentes para el departamento de Cochabamba, siguiendo el mismo formato, se encuentran disponibles en el siguiente enlace de [MeteoBlue](%s).
         
        A continuación, se encuentra un tutorial de como manejar la página web.
""" % url)
st.video("https://youtu.be/4UjXIj6seI4")
