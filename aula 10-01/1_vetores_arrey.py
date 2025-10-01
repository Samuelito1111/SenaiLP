import os
os.system("cls")

QUANTIDADE_NOTAS = 3

notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

media = sum(notas)/len(notas)

for i in range(QUANTIDADE_NOTAS):
    print(f'\n{i+1}ª Nota: {notas[i]}')

print(f'\nMédia: {media}')