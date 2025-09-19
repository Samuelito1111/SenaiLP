import os
os.system("cls")

while True:
    ano = int(input("\nDigite o um número para o mês do ano: "))

    if ano in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        break
    print("Operação inválida! Por favor, escolha novamente.")

match ano:
    case 1:
        mes = "Janeiro"
        num = "1"
    case 2:
        mes = "Fevereio"
        num = "2"
    case 3:
        mes = "Março"
        num = "3"
    case 4:
        mes = "Abril"
        num = "4"
    case 5:
        mes = "Maio"
        num = "5"
    case 6:
        mes = "Junho"
        num = "6"
    case 7:
        mes = "Julho"
        num = "7"
    case 8:
        mes = "Agosto"
        num = "8"
    case 9:
        mes = "Setembro"
        num = "9"
    case 10:
        mes = "Outubro"
        num = "10"
    case 11:
        mes = "Novembro"
        num = "11"
    case 12:
        mes = "Dezembro"
        num = "12"

print(f"\nO {num}° mês é {mes}")