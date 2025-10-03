import os
os.system("cls")

def par_impar(numero):
    os.system("cls")
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')

numero = int(input('Informe um número: '))
par_impar(numero)