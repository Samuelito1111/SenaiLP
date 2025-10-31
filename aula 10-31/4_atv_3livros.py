import os
from dataclasses import dataclass
os.system("cls")

QUANTIDADE_LIVROS = 3
listaLivros = []

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

print(f'Solicitando dados de {QUANTIDADE_LIVROS} livros: ')
for i in range(QUANTIDADE_LIVROS):
    livros = Livro(
        nome= input('Digite seu nome: '),
        autor= input('Digite seu e-mail: '),
        categoria= input('Digite seu categoria: '),
        preco= float(input('Digite sua idade: '))
    )
    listaLivros.append(livros)

print(f'\nExibindo dados de {QUANTIDADE_LIVROS} livros: ')

arquivo = "dados_livros.txt"

with open(arquivo, 'a') as arquivoslivros:
    for livros in listaLivros:
        arquivoslivros.write(f'{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preco}')
        print('Salvo com sucesso!')