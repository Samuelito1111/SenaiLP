import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write('''
Escrever um programa de computador que solicite do
usuário 5 números inteiros e,
ao final, apresente a soma de todos os números lidos.
''')

soma = 0

for i in range(1, 6):
    numero = st.number_input(f"Informe o {i}° número: ", step=1, min_value=0)
    soma += numero

if st.button("Iniciar"):
    st.success(f"A soma dos números é: {soma}")
else:
    st.info("Informe um número")