import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Autor: 
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def mostrarDados(self):       
        os.system("cls")
        print('\nDados do Livro')
        print(f'Título: {self.titulo}')
        print(f'Ano: {self.ano}')
        print(f'Autor: {self.autor.nome}')

livro1 = Livro(titulo= input('Informe o título do livro: '),
                   ano= int(input('Informe o ano de publicação do livro: ')),
                   autor= Autor(
                       nome= input('Informe o nome do(a) Autor(a): '),
                       biografia= input('Informe a biografioa: ')))

livro1.mostrarDados()