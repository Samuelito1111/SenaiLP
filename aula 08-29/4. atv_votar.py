import os
os.system("cls")

idade = int(input("Informe sua idade: "))

if idade >= 18 and idade <= 65:
    print("É obrigado a votar")
elif idade >= 16 or idade > 65:
    print("Não é obrigado a votar")
else:
    print("Não pode votar")
