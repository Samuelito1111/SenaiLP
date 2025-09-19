import os
os.system("cls")

nota = float(input("Informe a nota"))

# Se nota menor que zero ou maior que 10.
# OR -> Fora do intervalo
if nota < 0 or nota > 10:
    print("Nota inválida")
else:
    print(f"Nota: {nota}")