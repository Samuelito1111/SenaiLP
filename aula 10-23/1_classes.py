import os
from dataclasses import dataclass

os.system("cls")

class DadosPessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = DadosPessoa(nome= input('Digite seu nome: '), 
                      idade= int(input('Digite sua idade: ')), 
                      peso= float(input('Digite seu peso: ')), 
                      altura= float(input('Digite sua altura: ')))

print('\n=== Exibir dados ===')
print(f'Nome: {pessoa1.nome}')
print(f'Idade: {pessoa1.idade}')
print(f'Peso: {pessoa1.peso}')
print(f'Altura: {pessoa1.altura}')