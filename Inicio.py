import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from user_input import user_input
from streamlit_extras.stylable_container import stylable_container
from PIL import Image

logoFesa = Image.open("img/logo-fesa.png")

st.set_page_config(page_title="Riesgo de Incendio",
                   page_icon="🔥")

if 'data' not in st.session_state:
    st.session_state.data = pd.read_csv("data_11.csv")

st.title("🔥 Predicción de riesgo de incendio en Cochabamba 🔥")

with stylable_container(
    key="intro",
    css_styles="""
    {
        padding: 2rem;
    }
    """
):
    st.markdown("Este prototipo tiene como objetivo predecir el riesgo de incendio en el departamento de Cochabamba, Bolivia. Para ello, se emplea un modelo de Machine Learning basado en el algoritmo de Gradient Boosting. A continuación, se presenta un formulario para ingresar los datos necesarios para realizar la predicción.")

col1, col2 = st.columns(2)

data = st.session_state.data

# Limpiar los nombres de las columnas
data.columns = data.columns.str.strip()


with col1:
    st.subheader("Ingresar datos climáticos")
    with st.container(height=440):
        dataframe = user_input()

# Entrenar el modelo al cargar la página
if 'model' not in st.session_state:
    # Split the data into features (X) and target (y)
    X = data.drop(['Incendio'], axis=1)
    y = data['Incendio']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create the model
    gb_clf = GradientBoostingClassifier(
        n_estimators=20, learning_rate=0.5, max_features=2, max_depth=2, random_state=0)
    gb_clf.fit(X_train, y_train)

    # Save the model and test data in session state
    st.session_state.model = gb_clf
    st.session_state.X_test = X_test
    st.session_state.y_test = y_test
    st.session_state.predictions = gb_clf.predict(X_test)

    # Calculate feature importances
    feature_importances = pd.Series(
        gb_clf.feature_importances_, index=X.columns)
    st.session_state.feature_importances = feature_importances

# Botón para ejecutar el modelo
if "predict" not in st.session_state:
    st.session_state.predict = False


def predict_callback():
    st.session_state.predict = True


with col2:
    # RESULT
    st.subheader("Predicción del Modelo")

    # Result
    if st.session_state.get('predict', False):
        # Predictions
        model = st.session_state.model
        prediction = model.predict(dataframe.to_numpy())
        with st.container(key="resultados", height=200):
            st.write("Resultado de la predicción: " + str(prediction[0]))

            if int(prediction) == 1:
                st.write(
                    "Existe una :red[**alta**] probabilidad de riesgo de incendio", )
            else:
                st.write(
                    "Existe una :green[**baja**] probabilidad de riesgo de incendio")

        # Reset predict state
        st.session_state.predict = False
    else:
        with st.container(height=200):
            st.write("Esperando datos para realizar la predicción.")

    # button with callback
    st.button("Predecir", on_click=predict_callback, type="secondary")

footer = """<style>

.footer {
display: flex;
justify-content: space-between;
padding: 10px;
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #F0F2F6;
color: black;
text-align: center;
font-size: 12px;
}
</style>
<div class="footer">
    <div></div>
    <div>
        <div><b>Desarrollado por:</b></div>
        <div>Equipo Ganador Olimpiadas STEM+ 2024 <img src="https://fesa.edu.bo/wp-content/uploads/2024/04/STEM-logo-color-3.png" width="50px"></div>
        <div>TecnoBanda, Colegio San Agustín</div>
    </div>
    <div>
    <div><b>Con el Apoyo de:</b></div>
        <a href="https://fesa.edu.bo/"><img src="https://fesa.edu.bo/wp-content/uploads/2024/05/Logo-FESA.png" width="50px" alt="Logo" style="margin-right: 10px;"></a>
        <a href="https://labtecnosocial.org/"><img src="https://labtecnosocial.org/wp-content/uploads/2021/07/cropped-logo-claro-300x149.png" width="70px" alt="Logo"></a>
    </div>
    <div></div>

</div>
"""
st.markdown(footer, unsafe_allow_html=True)
