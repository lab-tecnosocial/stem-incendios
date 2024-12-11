from sklearn.metrics import classification_report, confusion_matrix
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = st.session_state.data
y_test = st.session_state.y_test
predictions = st.session_state.predictions

st.title("Sobre el Modelo")

st.image("incendios.jpg")

st.subheader("Datos de entrenamiento")
st.write(data)

# CORRELATION HEATMAP
st.subheader("Mapa De Correlación")

fig, ax = plt.subplots(figsize=(15, 15))
# Create the heatmap
sns.heatmap(data.corr(), annot=True, cmap="bwr", fmt=".2f", linewidths=.5)
# Display the plot
st.pyplot(fig)

# Precision
# lr_list = [0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1]
# st.subheader("Precisión del Algoritmo (Gradient Boosting)")
# with st.expander("**Datos Extra**"):
#     for learning_rate in lr_list:
#         gb_clf0 = GradientBoostingClassifier(
#             n_estimators=20, learning_rate=learning_rate, max_features=2, max_depth=2, random_state=0)
#         gb_clf0.fit(X_train, y_train)

#         st.write("Ritmo de Aprendizaje: ", learning_rate)
#         st.write("Puntaje de Precisión (Entrenamiento): {0:.3f}".format(
#             gb_clf0.score(X_train, y_train)))
#         st.write("Puntaje de Precisión (Validación): {0:.3f}".format(
#             gb_clf0.score(X_test, y_test)))


st.write("**Matriz de Confusión:**")
st.write('''
         1 significa que si hay riesgo de alta probabilidad de incendio\n
         0 significa que no hay riesgo de alta probabilidad de incendio
         ''')
st.write(pd.DataFrame(confusion_matrix(y_test, predictions)))

st.write("**Reporte de Clasificación:**")
st.dataframe(classification_report(y_test, predictions, output_dict=True))
