import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Crear casillas de verificación para cada tipo de gráfico
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión (Odómetro vs Precio)')
build_scatter_year = st.checkbox('Construir gráfico de dispersión (Año del Modelo vs Precio)')

if build_histogram:
    st.write('Construcción del histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro en los Vehículos")
    # Formatear ambos ejes para mostrar números con separador de miles
    fig.update_xaxes(tickformat=",.0f")
    fig.update_yaxes(tickformat=",.0f")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construcción del gráfico de dispersión para la relación entre odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    fig_scatter.update_xaxes(tickformat=",.0f")
    fig_scatter.update_yaxes(tickformat=",.0f")
    st.plotly_chart(fig_scatter, use_container_width=True)

if build_scatter_year:
    st.write('Construcción del gráfico de dispersión para la relación entre Año del Modelo y Precio')
    fig_scatter_year_price = px.scatter(
        car_data, 
        x="model_year", 
        y="price", 
        title="Relación entre Año del Modelo y Precio",
        labels={"model_year": "Año del Modelo", "price": "Precio"}
    )
    fig_scatter_year_price.update_xaxes(tickformat=",.0f")
    fig_scatter_year_price.update_yaxes(tickformat=",.0f")
    st.plotly_chart(fig_scatter_year_price, use_container_width=True)