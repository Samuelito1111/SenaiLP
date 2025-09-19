import streamlit as st

st.title("Laço de repetição: While")

numero = st.number_input("Informe um número", step=1)

while numero != 2:
    numero = st.number_input("Informe um número", step=1)
    break

st.header("Fim")