import os
import time
os.system("cls")

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def somar(n1, n2):
    return n1 + n2

def mostrar_resultado(soma):
    print(f'Resultado: {soma}')

limpa_tela()

primeiro_numero = int(input('Informe o 1° número: '))
segundo_numero = int(input('Informe o 2° número: '))

soma = somar(primeiro_numero, segundo_numero)

mostrar_resultado(soma)