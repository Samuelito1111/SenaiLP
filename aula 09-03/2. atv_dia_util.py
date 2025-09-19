import os
os.system("cls")

while True:
    semana = int(input("Digite o um número para o dia da semana: "))

    if semana in [1, 2, 3, 4, 5, 6, 7]:
        break
    print("Operação inválida! Por favor, escolha novamente.")

match semana:
    case 1:
        dia = "Domingo"
        utilidade = "Fim de Semana"
    case 2:
        dia = "Segunda-Feira"
        utilidade = "Dia útil"
    case 3:
        dia = "Terça"
        utilidade = "Dia útil"
    case 4:
        dia = "Quarta"
        utilidade = "Dia útil"
    case 5:
        dia = "Quinta"
        utilidade = "Dia útil"
    case 6:
        dia = "Sexta"
        utilidade = "Dia útil"
    case 7:
        dia = "Sábado"
        utilidade = "Fim de Semana"

print(f"\nO dia foi {dia}, é um {utilidade}")