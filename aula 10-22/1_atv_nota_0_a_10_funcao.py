import os
os.system("cls")

notas = []
QUANTIDADE_NOTAS = 2

def medias(notas):
    resultado = sum(notas) / QUANTIDADE_NOTAS
    return resultado

def aprovacao(media):
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Informe a {i + 1}° nota: "))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    notas.append(nota)

media = medias(notas)

print(f"Média: {media:.2f}")
aprovacao(media)