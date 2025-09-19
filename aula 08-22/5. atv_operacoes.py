import os
os.system("cls")

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

soma = n1 + n2
media = soma/2
produto = n1*n2

# maiorNumero = n1 if n1 > n2 else n2
# menorNumero = n1 if n1 < n2 else n2

maiorNumero = max(n1, n2)
menorNumero = min(n1, n2)

print(" ")
print(" ")
print("=== Resultado ===")
print(" ")
print(f"A SOMA dos números é = {soma}")
print(f"A MÉDIA dos números é = {media}")
print(f"O PRODUTO dos números é = {produto}")
print(f"O MAIOR número é = {maiorNumero}")
print(f"O MENOR número é = {menorNumero}")