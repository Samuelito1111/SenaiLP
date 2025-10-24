import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str
    
@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):       
        print('Mostrar dados do cliente')
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Estado: {self.endereco.estado}')
        print(f'Cidade: {self.endereco.cidade}')
        print(f'Endereço: {self.endereco.logradouro}')
        print(f'Número: {self.endereco.numero}')

cliente1 = Cliente(nome=input('Informe seu nome: '),
                   email= input('Informe seu email: '),
                   endereco=Endereco(
                       estado= input('Informe seu Estado: '),
                       cidade= input('Informe o nome da sua cidade: '),
                       logradouro= input('Informe o somente o nome do seu endereço: '),
                       numero= int(input('Informe o número do seu endereço: '))))

cliente1.mostrar_dados()