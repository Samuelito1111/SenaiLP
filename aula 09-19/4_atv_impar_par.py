import os
os.system("cls")

somaGeral = 0
somaPares = 0

quantidadeGeral = 0
quantidadePares = 0
quantidadeImpares = 0

while True:
    numero = int(input('Informe um número: '))
    if numero == 0:
        break
    
    if numero % 2 == 0:
        somaPares += numero
        somaGeral += numero
        quantidadeGeral += 1
        quantidadePares += 1
    else:
        somaGeral += numero
        quantidadeGeral += 1
        quantidadeImpares += 1

mediaGeral = somaGeral/quantidadeGeral
mediaPares = somaPares/quantidadePares

print(f'''
A quantidade de números Pares foi: {quantidadePares}
A quantidade de números Ímpares foi: {quantidadeImpares}

Média de números Pares foi: {mediaPares}
Média de números Geral foi: {mediaGeral}
''')