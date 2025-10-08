import os
import time
os.system("cls")

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def converterMetros(numero):
    return numero * 100

numero = int(input('Informe o número:'))

resultado = converterMetros(numero)    

print(f'Valor em cm: {resultado}')