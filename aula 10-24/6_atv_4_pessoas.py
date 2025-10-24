import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_PESSOAS = 4

class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print('\n=== Exibir dados ===')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

lista_pessoas = []

for i in range(QUANTIDADE_PESSOAS):
    print(f"\nInforme os dados da {i + 1}° pessoa:")      
    dados_pessoa = Pessoa(nome= input('Digite seu nome: '), 
                        idade= int(input('Digite sua idade: ')), 
                        peso= float(input('Digite seu peso: ')), 
                        altura= float(input('Digite sua altura: ')))
    lista_pessoas.append(dados_pessoa)
    os.system("cls")

for dados_pessoa in lista_pessoas:
    dados_pessoa.mostrar_dados()

