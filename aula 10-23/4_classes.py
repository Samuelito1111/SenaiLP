import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class DadosPessoa:
    nome: str
    email: str
    endereco: str
        
    def dados_entrega(self):        
        print('\n=== Dados Entrega ===')
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        
    def dados_email_marketing(self):
        print('\n=== Dados E-mail ===')
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        
        
print('=== Coletar dados ===')
pessoa1 = DadosPessoa(nome= input('Digite seu nome: '), 
                      email= input('Digite seu email'),
                      endereco= input('Digite sua endereço: ')), 

os.system("cls")

print('\n=== Exibir dados ===')
pessoa1.dados_entrega()
pessoa1.dados_email_marketing()