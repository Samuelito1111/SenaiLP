# Escrever um algoritmo que mostra os números pares entre 100 e 120

import streamlit as st
import time

st.title("Laço de repetição: For")

st.write("Escrever um algoritmo que mostra os números pares entre 100 e 120")
st.write("Clique no botão para iniciar.")

if st.button("Iniciar"):
    for i in range(100, 121, 2):
        st.info(i)
        time.sleep(2)
    st.header("Fim")