import streamlit as st
import time

st.title("Atividade")

st.header("Laço de repetição: For")

st.write('''
Escrever um programa de computador que solicite do usuário 3 notas e,
ao final, apresente a média e mostre para o usuário se o aluno está aprovado,
em recuperação ou reprovado. 

Considere que para aprovação, deve-se obter média maior ou igual a 7,
para ser reprovado, a média deve ser menor que 4.
''')

notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nt = st.number_input(f"Informe a {i+1}° nota: ", min_value=0, max_value=10)
    notas.append(nt)

media = sum(notas)/QUANTIDADE_NOTAS

if st.button("Ver a média"):
    st.info(f"Media: {media:.1f}")
    if media >= 7:
        st.success("Parabéns! Aprovado!")
    elif media >= 4:
        st.warning("Recuperação")
    else:
        st.error("Reprovado")
else:
    st.warning("Informe todas as notas")