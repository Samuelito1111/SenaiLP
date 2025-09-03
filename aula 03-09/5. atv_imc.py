import os
os.system("cls")

nome = input("Informe seu nome: ")
altura = float(input("Informe sua Altura: "))

while True:
    sexo = input("Informe o seu sexo biológico (M-Masculino ou F-Feminino): ").upper()

    if sexo in ["M","F"]:
        break
    print("\nOperação inválida! Por favor, escolha novamente.")

match sexo:
    case "M":
        pesoIdeal = (72.7 * altura)-58
        print(f"""\n
Nome: {nome}
Altura: {altura}
Peso Ideal: {pesoIdeal}
""")
    case "F":
        pesoIdeal = (62.1 * altura)-44.7
        print(f"""\n
Nome: {nome}
Altura: {altura}
Peso Ideal: {pesoIdeal:.2f}
""")