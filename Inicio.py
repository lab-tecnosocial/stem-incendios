import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from user_input import user_input
from streamlit_extras.stylable_container import stylable_container


st.set_page_config(page_title="Riesgo de Incendio",
                   page_icon="🔥")

if 'data' not in st.session_state:
    st.session_state.data = pd.read_csv("Data_clima_Clasificaction.csv")

st.header("PREDICCIÓN DE RIESGO DE INCENDIO EN EL DEPARTAMENTO DE COCHABAMBA")

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

with col1:
    st.subheader("Ingresar datos climáticos")
    with st.container(height=500):
        dataframe = user_input()

# Entrenar el modelo al cargar la página
if 'model' not in st.session_state:
    # Split the data into features (X) and target (y)
    X = data.drop('Incendio', axis=1)
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

        with st.container(height=200):
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
    st.button("Predecir", on_click=predict_callback)

for i in range(10):
    st.write("")


st.markdown("""
<style>
.big-font {
    position: absolute !important;
    font-size:13px !important;
    line-height:5px !important;
    right:100px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">INFO</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">Olimpiadas STEM+ 2023</p>',
            unsafe_allow_html=True)
st.markdown('<p class="big-font">Grupo: TecnoBanda</p>',
            unsafe_allow_html=True)
st.markdown('<p class="big-font">Colegio San Agustín</p>',
            unsafe_allow_html=True)
st.markdown('<p class="big-font">CBBA - Bolivia</p>', unsafe_allow_html=True)
