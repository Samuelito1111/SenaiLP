import os
os.system("cls")

def saudacoes(nome, idade, altura, peso):
    os.system("cls")
    print(f'''
Olá {nome}! Seja bem-vindo(a)!
Sua idade é: {idade} anos!
Tem {altura:.2f} cm de altura!
Pesa {peso:.2f} kg!''')

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
saudacoes(nome, idade, altura, peso)