import os
os.system("cls")

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

operacao = input("Informe qual operação deseja executar (+-*/): ")

match operacao:
    case "+":
        soma = n1 + n2
        print(f"A soma dos números é: {soma}")
    case "-":
        subtra = n1 - n2
        print(f"A subtração dos números é: {subtra}")
    case "*":
        produto = n1 * n2
        print(f"O produto dos números é: {produto}")
    case "/":
        divisao = n1 + n2
        print(f"A divisão dos números é: {divisao}")
    case _:
        print("Operação inválida")
print("Fim")