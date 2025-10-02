import os
os.system("cls")

QUANTIDADE_NUMEROS = 6

numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Informe o {i+1}° número: '))
    numeros.append(numero)
    
for i in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print('\n== Resultado ==\n')

for i in range(QUANTIDADE_NUMEROS):
    print(f'{i+1}ª número: {numeros[i]}')

print(' ')

print(f"O número de Pares é: {pares}")
print(f"O número de Ímpares é: {impares}")   