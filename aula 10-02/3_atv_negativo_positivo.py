import os
os.system("cls")

numeros = []
QUANTIDADE_NUMEROS = 5
negativos = 0
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Informe o {i+1}° número: '))
    
    if numero < 0:
        negativos += 1
    else:
        numeros.append(numero)

print('\n== Resultado ==')

print(f'''
Quantidade de números Negativos: {negativos}
Soma dos números Positivos: {sum(numeros)}
''')