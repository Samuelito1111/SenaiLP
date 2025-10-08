import os
os.system("cls")

def posi_nega(numero):
    os.system("cls")
    if numero < 0:
        print(f'O número {numero} é positivo!')
    elif numero > 0:
        print(f'O número é 0!')
    else:
        print(f'O número {numero} é negativo!')

numero = int(input('Informe um número: '))
posi_nega(numero)