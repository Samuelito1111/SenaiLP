import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write('''
Escrever um algoritmo que solicite ao usuário um
número e faça a contagem regressiva a partir do
número informado até o número 1, aguardando um
segundo para exibir cada número''')

numero = st.number_input("Digite um número: ", step=1, min_value=0)

st.write("Clique no botão para iniciar.")
if st.button("Iniciar"):
    for i in range(numero, 0, -1):
        st.warning(i)
        time.sleep(1)
    st.balloons()
    st.header("Fim")
else:
    st.info("Informe um número")