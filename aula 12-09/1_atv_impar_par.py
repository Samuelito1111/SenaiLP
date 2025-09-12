import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write('''
Escreva um algoritmo que solicite ao usuário 5 valores
inteiros e ao final mostre:

a.quantos números são pares; 

b.quantos números são ímpares;
''')

for i in range(1, 6):
    numero = st.number_input(f"Informe o {i}° número: ", step=1, min_value=0)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if set.button("Verificar"):
    st.info(f"Quantidade de pares: {pares}")
    st.info(f"Quantidade de impares: {impares}")