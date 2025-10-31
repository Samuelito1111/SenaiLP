import os
os.system("cls")

# Texto que deseja salvar
texto = input('Digite seu nome: ')

# Definir nome do arquivo para salvar
nomeArquivo = 'exemplo.txt'

# Comandos para salvar
with open (nomeArquivo, 'a') as meuArquivo:
    meuArquivo.write(f'{texto}\n')
print('Salvo com sucesso!')