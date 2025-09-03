import os
os.system("cls")

produto = input("Informe o nome do produto: ")
valor = float(input("Informe o valor do produto: "))

while True:
    pagamento = int(input("Informe o tipo de pagamento (1: à vista; 2: à prazo): "))

    if pagamento in [1, 2]:
        break
    print("\nOperação inválida! Por favor, escolha novamente.")
    
match pagamento:
    case 1:
        tipo = "À Vista"
        desconto = valor * 0.10
        valorFinal = valor - desconto

        print(f"""
Nome do Produto: {produto}
Valor: {valor}
Pagamento: {tipo}
Valor do Desconto: {desconto}
Valor Final: {valorFinal}
              """)
    case 2:
        while True:
            numParcela = int(input("Informe a quantidade de parcelas (Até 6 vezes): "))

            if pagamento in [1, 2, 3, 4, 5, 6]:
                break
            print("\nOperação inválida! Por favor, escolha novamente.")
                    
        valorParcela = valor / numParcela
        tipo = "À Prazo"

        print(f"""
Nome do Produto: {produto}
Valor: {valor}
Pagamento: {tipo}
Quantidade de Parcelas: {numParcela}
Valor por Parcela: {valorParcela:.2f}
Total à prazo: {valor}
              """)
