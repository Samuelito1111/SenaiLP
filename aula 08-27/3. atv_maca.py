import os
os.system("cls")

quantiMaca = int(input("Informe a Quantidade de Maçãs que você deseja: "))

if quantiMaca >= 12:
    macaPreco = 1
else:
    macaPreco = 1.30

valorFinal = quantiMaca * macaPreco
print(f"O valor total foi de R${valorFinal}")
