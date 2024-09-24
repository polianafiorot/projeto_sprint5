import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px
        
car_data = pd.read_csv(Path("./data/vehicles.csv")) # lendo os dados

st.header("Aplicativo Web Simples com Streamlit")
st.title("Análise de Carros Usados")

        
if st.button('Criar um histograma para preço de carros'): # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para preço de carros usados')
    # criar um histograma
    fig = px.histogram(car_data, x="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

     
if st.checkbox('Criar um histograma para tipo de carro'):
    st.write('Criando um histograma para tipo de carro')
    fig1 = px.histogram(car_data, x="type")
    st.plotly_chart(fig1, use_container_width=True)

if st.checkbox('Criar um gráfico de dispersão para condição do carro'):
    st.write('Criando um gráfico de dispersão para condição do carro')
    fig2 = px.scatter(car_data, x="condition", y="price")
    st.plotly_chart(fig2, use_container_width=True)




        