import os
os.system("cls")

numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Informe o {i+1}° número: '))
    
    if numero < 0:
        numero = 0
        numeros.append(numero)
    else:
        numeros.append(numero)

print('\n== Resultado ==\n')

for i in range(QUANTIDADE_NUMEROS):
    print(f'{i+1}° valor: {numeros[i]}')