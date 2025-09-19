import os
os.system("cls")

print("Laço de repetição: While")

print('''
Escreva um algoritmo que solicite ao usuário a nota de um
aluno. Caso seja menor que 0 ou maior que 10, mostre a pergunta
novamente. Mostre a nota informada pelo usuário.
''')

while True:
    nota = float(input("Infomer um número: "))
    if nota >= 0 and nota <= 10:
        break
    print("Operação inválida! Por favor, escolha novamente.\n")
print(f"Nota: {nota}")