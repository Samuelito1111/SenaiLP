import os

def logo_senai():
    os.system("cls")
    print('''
===============
||   SENAI   || 
===============''')
    
logo_senai()
nome = input('Informe seu nome: ')

logo_senai()
idade = int(input('Informe sua idade: '))

logo_senai()
peso = float(input('Informe seu peso: '))

logo_senai()
print(f'''
Nome: {nome}
Idade: {idade}
Peso: {peso}
''')