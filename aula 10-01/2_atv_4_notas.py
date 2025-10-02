import os
os.system("cls")

QUANTIDADE_NOTAS = 4

notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

media = sum(notas)/len(notas)

if media >= 7:
    resultado = 'Aprovado'
elif media >= 5:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print('\n== Resultado ==\n')

for i in range(QUANTIDADE_NOTAS):
    print(f'\n{i+1}ª Nota: {notas[i]}')

print(f'\nMédia: {media}')
print(f'\nSituação: {resultado}')
