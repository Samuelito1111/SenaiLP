import os
os.system("cls")

soma = 0
quantidadeNotas = 0

while True:
    nota = int(input('Informe uma nota: '))
    if nota < 0:
        break
    quantidadeNotas += 1
    soma += nota
    
media = soma/quantidadeNotas

print(f'\nMédia: {media}')