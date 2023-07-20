#Para executar streamlit run App.py

import streamlit as st
import pandas as pd
import numpy as np

st.header("Título") # Quer colocar em Negrito? Add "# Text"

st.caption('Adcione sua legenda, adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda, Adcione sua legenda ')

opcao = st.sidebar.selectbox(
    "Selecione uma opção:",
    ("","Opção 1","Opção 2", "Opção 3")
)

if opcao == "Opção 1":
    df = pd.DataFrame(
     np.random.randn(10, 4),
     columns=['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4',])

    st.table(df)

elif opcao == "Opção 2":
    df = pd.DataFrame(
     np.random.randn(10, 4),
     columns=['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4',])

    st.bar_chart(df)

if opcao == "Opção 3":
    df = pd.DataFrame(
        np.random.randn(10, 4),
        columns=['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4',])
    st.line_chart(df)





