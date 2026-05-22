import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Cargar datos
df = pd.read_csv(r"C:\Users\GTX 1660Ti\Downloads\Proyecto_S_7\vehicles_us.csv")
df["type"] = df["type"].astype(str)

# Poner título
st.header('Estadística descriptiva de Vehículos', divider = "blue")

# Descargar dataset
st.download_button(
    label = "Descargar dataset",
    data = df.to_csv(index=False),
    file_name = "vehicles_us_limpio.csv"
)

st.divider()

# Seleccionar solo variables numéricas
opciones = df.select_dtypes(include=np.number).columns.tolist()

v = st.multiselect(
    label = "Seleccione máximo 2 variables numéricas:",
    options = opciones,
    max_selections = 2
)

# Ejecutar análisis
analisis_b = st.button(
    label = "Analizar"
)

st.divider()

# Analisis
if analisis_b:
    if len(v) == 2:
        try:
            # Filtrar filas vacías en las variables seleccionadas
            df_clean = df.dropna(subset=v)

            col1, col2 = st.columns(2)

            # Visualizar histograma de variable 1
            with col1:

                hist_plot01 = px.histogram(
                    df_clean, 
                    x = v[0], 
                    title = f"Distribución {v[0]}", 
                    color = "type", 
                    marginal = "box", 
                    width = 700, 
                    height = 400
                )
                st.plotly_chart(hist_plot01, use_container_width=True)

                c1, c2, c3 = st.columns(3)

                with c1:
                    prom1 = np.mean(df_clean[v[0]])
                    st.metric(
                        label = "Media",
                        value = "{:.1f}".format(prom1)
                    )
                with c2:
                    med1 = np.median(df_clean[v[0]])
                    st.metric(
                        label = "Mediana",
                        value = "{:.1f}".format(med1)
                    )
                with c3:
                    desv1 = np.std(df_clean[v[0]])
                    st.metric(
                        label = "Desviación",
                        value = "{:.1f}".format(desv1)
                    )

            # Visualizar histograma de variable 2
            with col2:
                hist_plot02 = px.histogram(
                    df_clean, 
                    x = v[1], 
                    title = f"Distribución {v[1]}", 
                    color = "type", 
                    marginal = "box", 
                    width = 700,
                    height = 400
                )
                st.plotly_chart(hist_plot02, use_container_width=True)

                c4, c5, c6 = st.columns(3)

                with c4:
                    prom2 = np.mean(df_clean[v[1]])
                    st.metric(
                        label = "Media",
                        value = "{:.1f}".format(prom2)
                    )
                with c5:
                    med2 = np.median(df_clean[v[1]])
                    st.metric(
                        label = "Mediana",
                        value = "{:.1f}".format(med2)
                    )
                with c6:
                    desv2 = np.std(df_clean[v[1]])
                    st.metric(
                        label = "Desviación",
                        value = "{:.1f}".format(desv2)
                    )

            # Visualizar dispersion entre variables
            disp_plot = px.scatter(
                df_clean, 
                x = v[0], 
                y = v[1], 
                color = "type", 
                title = f"Dispersión {v[1]} vs. {v[0]}", 
                width = 700, 
                height = 400
            )
            st.plotly_chart(disp_plot, use_container_width=True)

            correl = np.corrcoef(df_clean[v[0]], df_clean[v[1]])
            st.metric(
                label = "Correlación de Pearson",
                value = "{:.1%}".format(correl[0,1])
            )

        except Exception as e:
            st.error(f"Ocurrió un error al calcular: {e}")
    else:
        st.warning("Faltan variables por seleccionar (debes seleccionar exactamente 2).")








