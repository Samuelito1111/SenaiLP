import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_ALUNOS = 2
listaAlunos = []

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: str

print(f'Solicitando dados de {QUANTIDADE_ALUNOS} alunos: ')
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input('Digite seu nome: '),
        idade= int(input('Digite sua idade: ')),
        email= input('Digite seu e-mail: '),
        telefone= input('Digite seu telefone: ')
    )
    listaAlunos.append(aluno)

print(f'\nExibindo dados de {QUANTIDADE_ALUNOS} alunos: ')

arquivo = "dados_alunos.txt"

with open(arquivo, 'a') as arquivosAlunos:
    for aluno in listaAlunos:
        arquivosAlunos.write(f'{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}')
        print('Salvo com sucesso!')