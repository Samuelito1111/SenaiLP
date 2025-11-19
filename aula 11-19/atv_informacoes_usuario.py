import os
os.system("cls")
from dataclasses import dataclass
import datetime

@dataclass
class Funcionario:
    nome: str
    data: datetime
    rg: str
    cpf: str

    def exibir_dados(self):
        data_formatada = self.data.strftime('%d/%m/%Y')
        print(f'Nome: {self.nome} \nData de Nascimento: {self.data_formatada} \nRG: {self.rg} \nCPF: {self.cpf}')

lista_de_funcionarios = []
QUANTIDADE_DE_FUNCIONARIOS = 2

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcionario = Funcionario(
        nome= input("Digite seu nome: "),
        data_texto = input("Digite a data de nascimento (dd/mm/aaaa): "),
        rg= input("Digite seu RG: "),
        cpf= input("Digite seu CPF: ")
    )
    lista_de_funcionarios.append(funcionario)
    print() # Pular uma linha.

nome_do_arquivo = "dados_funcionarios.csv"
with open(nome_do_arquivo, "a", encoding="uft-8") as arquivo_funcionarios:
    for funcionario in lista_de_funcionarios:
        arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.idade}, {funcionario.peso}, {funcionario.altura}, {funcionario.cpf} \n")
    print("Dados salvos com sucesso.")

print("\nExibindo todos os funcionarios: ")
lista = []
try:
    data_convertida = datetime.strptime(data_texto, "%d/%m/%Y")
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, data = funcionario.strip().split(",")
            dados_funcionario = Funcionario(nome=nome, idade=int(idade))
            lista.append(dados_funcionario)
    for funcionario in lista:
        funcionario.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")