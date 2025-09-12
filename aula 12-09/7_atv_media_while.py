import os
os.system("cls")

print("Laço de repetição: While")

print('''
Escreva um algoritmo que solicite duas notas para um aluno. 
Caso seja menor que 0 ou maior que 10, mostre a pergunta
novamente.
Calcule e mostre a média aritmética do aluno.
''')

notas = []
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nt = float(input(f"Informe a {i+1}° nota: "))
        
        if nt >= 0 and nt <= 10:
            notas.append(nt)
            break
        print("Operação inválida! Por favor, escolha novamente.\n")

media = sum(notas)/QUANTIDADE_NOTAS

print(f"Média: {media}")