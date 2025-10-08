import os
import time
os.system("cls")

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def somar(n1, n2):
    soma = n1 + n2
    return soma

def subtrair(n1, n2):
    subtrai = n1 - n2
    return subtrai

def multiplicar(n1, n2):
    multiplica = n1 * n2
    return multiplica

def dividir(n1, n2):
    divide = n1 / n2 if n2 != 0 else 'Divisão por zero'
    return divide

def mostrar_resultado(posicao1, posicao2, posicao3, posicao4):
    print(f'Soma: {posicao1}')
    print(f'Subtração: {posicao2}')
    print(f'Multiplicação: {posicao3}')
    print(f'Divisão: {posicao4}')

primeiro_numero = int(input('Informe o 1° número: '))
segundo_numero = int(input('Informe o 2° número: '))

soma = somar(primeiro_numero, segundo_numero)
subtrai = subtrair(primeiro_numero, segundo_numero)
multiplica = multiplicar(primeiro_numero, segundo_numero)
divide = dividir(primeiro_numero, segundo_numero)

mostrar_resultado(soma, subtrai, multiplica, divide)