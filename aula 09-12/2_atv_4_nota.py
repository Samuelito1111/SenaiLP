import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write('''
Escrever um programa de computador que
solicite do usuário 4 notas e, ao final, apresente a média.
''')


soma = 0

for i in range(1, 5):
    notas = st.number_input(f"Informe a {i}° nota: ", min_value=0, max_value=10)
    soma += notas

media = soma/4

if st.button("Iniciar"):
    st.success(f"A média do aluno é: {media}")