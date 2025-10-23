import os
from dataclasses import dataclass

os.system("cls")

class DadosPessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

print('\n=== Coletar dados ===')
pessoa1 = DadosPessoa(nome= input('Digite seu nome: '), 
                      email= input('Digite seu email: '), 
                      telefone= input('Digite seu telefone: '), 
                      endereco= input('Digite sua endereço: '))

os.system("cls")

print('\n=== Exibir dados ===')
print(f'Nome: {pessoa1.nome}')
print(f'Email: {pessoa1.email}')
print(f'Telefone: {pessoa1.telefone}')
print(f'Endereço: {pessoa1.endereco}')