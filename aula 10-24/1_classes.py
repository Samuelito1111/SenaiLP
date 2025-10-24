import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_CLIENTES = 3

@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str

    def mostrar_dados_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')

lista_clientes = []


for i in range(QUANTIDADE_CLIENTES):
    print(f"\nInforme os dados da {i + 1}° pessoa:")
    dados_clientes = Cliente(nome= input('Digite seu nome: '),
                             endereco= input("Infomre seu endereço: "),
                             telefone= input('Digite seu telefone: '))
    lista_clientes.append(dados_clientes)
    os.system("cls")

for um_cliente in lista_clientes:
    um_cliente.mostrar_dados_cliente()