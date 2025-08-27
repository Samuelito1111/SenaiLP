import os
os.system("cls")

idade = int(input("Informe sua idade: "))

print(" ")
print("=== Resultado ===")
print(" ")

if idade < 16:
    resultado = print("NÃO pode votar!!")
elif idade <= 17:
    resultado = print("Voto OPCIONAL!!")
elif idade >= 65:
    resultado = print("NÃO é OBRIGADO pode votar!!")
else:
    resultado = print("OBRIGADO a votar!!")