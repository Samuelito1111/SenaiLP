import os
os.system("cls")

QUANTIDADE_NUMEROS = 5

numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'\nInforme o {i+1}° número: '))
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

print('\n== Resultado ==\n')

for i in range(QUANTIDADE_NUMEROS):
    print(f'{i+1}ª número: {numeros[i]}')

print(' ')

print(f"O MAIOR número é: {maiorNumero}")
print(f"O MENOR número é: {menorNumero}")   