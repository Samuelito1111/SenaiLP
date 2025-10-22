import os
os.system("cls")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar(imc,classificacao,recomendacao):
    if imc >= 40:
        classificacao = "Obesidade grau 3"
        recomendacao = "Procure ajuda médica especializada o quanto antes."
    elif imc >= 35:
        classificacao = "Obesidade grau 2"
        recomendacao = "É importante buscar acompanhamento médico e nutricional."
    elif imc >= 30:
        classificacao = "Obesidade grau 1"
        recomendacao = "Procure um profissional de saúde para orientação."
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere adotar hábitos mais saudáveis e aumentar a atividade física."
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha uma alimentação equilibrada e pratique exercícios."
    else:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um nutricionista para orientação."
    return classificacao, recomendacao

def exibir (imc, classificacao, recomendacao):
    print(f'''
Seu IMC é: {imc:.2f}
Classificação: {classificacao}
Recomendação: {recomendacao}
''')

peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros (ex: 1.75): "))

imc = calcular_imc(peso, altura)
classificacao, recomendacao = classificar(imc)

exibir(imc, classificacao, recomendacao)