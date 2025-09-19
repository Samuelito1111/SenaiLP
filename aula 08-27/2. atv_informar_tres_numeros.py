import os
os.system("cls")

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

maiorNumero = max(n1, n2, n3)
menorNumero = min(n1, n2, n3)

print(" ")
print("=== Resultado ===")
print(" ")

print(f"O primeiro número é: {n1}")
print(f"O segundo número é: {n2}")
print(f"O terceiro número é: {n3}")
print(f"O MAIOR número é: {maiorNumero}")
print(f"O MENOR número é: {menorNumero}")
