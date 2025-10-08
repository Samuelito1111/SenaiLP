import os
os.system("cls")

produto = 0

def tabuada(numero, produto):
    os.system("cls")
    print('== Tabuada ==')
    for i in range(1,11):
        produto = numero * i
        print(f'{numero} x {i} = {produto}')

numero = int(input('Informe um número: '))
tabuada(numero, produto)