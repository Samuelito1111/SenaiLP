# Escreva um algoritmo que solicite do usuário um número e 
# mostre a tabuada de multiplicação do número informado

import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write("Escrever um algoritmo que mostre os números ímpares entre 1 e 20")

numero = st.number_input("Digite um número: ", step=1)

st.write("Clique no botão para iniciar.")
if st.button("Calcular"):
    for i in range(1, 11):
        produto = numero * i
        st.info(f"{numero} x {i} = {produto}")
        time.sleep(1)
    st.header("Fim")