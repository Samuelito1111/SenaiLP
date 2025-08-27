import os
os.system("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(" ")
print("=== Boletim ===")
print(" ")

if media >= 7:
    resultado = "Aprovado(a)"
elif media >= 4:
    resultado = "Recuperação"
else:
    resultado = "Nem tenta, véi"

print(f"Média do(a) aluno(a) = {media}")
print(f"Situação do(a) aluno(a) = {resultado}")