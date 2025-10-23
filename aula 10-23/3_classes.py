import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class DadosPessoa:
    nome: str
    email: str
    telefone: str
    endereco: str
    
    def mostrar_dados(self):        
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')

print('=== Coletar dados ===')
pessoa1 = DadosPessoa(nome=input('Digite seu nome: '), 
                      email=input('Digite seu email: '), 
                      telefone=input('Digite seu telefone: '), 
                      endereco=input('Digite sua endereço: '))

os.system("cls")

print('\n=== Exibir dados ===')
pessoa1.mostrar_dados()