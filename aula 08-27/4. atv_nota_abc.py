import os
os.system("cls")

nome = input("Informe o nome do(a) alunoa(a): ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

if media >= 6:
    resultado = "Aprovado(a)"
else:
    resultado = "Reprovado(a)"

print(" ")
print("=== Boletim ===")
print(" ")

print(f"Nome do(a) aluno(a) = {nome}")
print(f"Média = {media}")
print(f"Conceito = {conceito}")
print(f"Situação = {resultado}")