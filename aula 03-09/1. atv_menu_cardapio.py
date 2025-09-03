import os
os.system("cls")

print("""
================ MENU =================
| Código |       Prato      |   Valor |
|   1    |      Picanha     | R$24,00 |
|   2    |      lasanha     | R$20,00 |
|   3    |    Strogonoff    | R$18,00 |
|   4    |  Bife Acebolado  | R$15,00 |
|   5    |    Pão com Ovo   | R$5,00  |
=======================================
""")


while True:
    opcao = int(input("\nInforme qual o código do prato que você deseja: "))

    if opcao in [1, 2, 3, 4, 5]:
        break
    print("Operação inválida! Por favor, escolha novamente.")

match opcao:
    case 1:
        codigo = "1"
        nome = "Picanha"
        valor = "R$24,00"
    case 2:
        codigo = "2"
        nome = "lasanha"
        valor = "R$20,00"
    case 3:
        codigo = "3"
        nome = "Strogonoff"
        valor = "R$18,00"
    case 4:
        codigo = "4"
        nome = "Bife Acebolado"
        valor = "R$15,00"
    case 5:
        codigo = "5"
        nome = "Pão com Ovo"
        valor = "R$5,00"

print("\nO prato escolhido foi: ")
print(f"Código: {codigo} | Nome: {nome} | Valor: {valor}")
print(" ")