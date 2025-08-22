import os
os.system("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

print(" ")
print("=== Boletim ===")

if media >= 7:
    resultado = "Aprovado"
elif media >= 4:
    resultado = "Recuperação"
else:
    resultado = "Nem tenta, fí"

print(f"Média do aluno = {media}")
print(f"Situação do aluno = {resultado}")