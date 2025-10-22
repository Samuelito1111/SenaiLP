from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome: str
    tipo: str
    peso: float

pessoa1 = Pessoa(nome="Sam", idade=19, cpf="123.456.789-00")
pessoa2 = Pessoa(nome="Bre", idade=19, cpf="987.654.321-00")

pet1 = Pet(nome="Bolt", tipo="Cachorro", peso=12.5)
pet2 = Pet(nome="Manda Chuva", tipo="Gato", peso=4.3)



print(f'Dados das pessoas:')
print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}\n')
print(f'Nome: {pessoa2.nome}\nIdade: {pessoa2.idade}\nCPF: {pessoa2.cpf}\n')

print(f'Dados dos pets:')
print(f'Nome: {pet1.nome}\nTipo: {pet1.tipo}\nPeso: {pet1.peso} kg\n')
print(f'Nome: {pet2.nome}\nTipo: {pet2.tipo}\nPeso: {pet2.peso} kg\n')