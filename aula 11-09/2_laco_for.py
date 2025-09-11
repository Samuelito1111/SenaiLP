# Escrever um algoritmo que mostre os números ímpares entre 1 e 20

import streamlit as st
import time

st.title("Laço de repetição: For")

st.write("Escrever um algoritmo que mostre os números ímpares entre 1 e 20")
st.write("Clique no botão para iniciar.")

if st.button("Iniciar"):
    for i in range(1, 21, 2):
        st.info(i)
        time.sleep(1)
    st.header("Fim")