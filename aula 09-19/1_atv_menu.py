import os
os.system("cls")

valorTotal = 0
while True:
    print("""
    ================ MENU =================
    | Código |       Prato      |   Valor |
    |   1    |      Picanha     | R$25,00 |
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
            valor = 25
        case 2:
            codigo = "2"
            nome = "lasanha"
            valor = 20
        case 3:
            codigo = "3"
            nome = "Strogonoff"
            valor = 18
        case 4:
            codigo = "4"
            nome = "Bife Acebolado"
            valor = 15
        case 5:
            codigo = "5"
            nome = "Pão com Ovo"
            valor = 5
    
    valorTotal += valor
    

    outroPedido = input('Deseja adicionar mais algum prato? (S/N)').upper().strip()
    
    if outroPedido == "N":
        break
    
    os.system("cls")
    
print(f'''
Valor Total da compra: {valorTotal}
''')