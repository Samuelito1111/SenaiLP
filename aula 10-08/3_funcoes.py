import os
import time
os.system("cls")

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def calcular_media(n1, n2):
    calcular = (n1 + n2)/2
    return calcular

def mostrar_resultado(media):
    print(f'Resultado: {media}')
    
    if media >= 7:
        print(f'Aprovado')
    else:
        print(f'Reprovado')

limpa_tela()

nota1 = int(input('Informe a 1°nota: '))
nota2 = int(input('Informe a 2°nota: '))

media = calcular_media(nota1, nota2)

mostrar_resultado(media)