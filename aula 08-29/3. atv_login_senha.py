import os
os.system("cls")

loginSalvo = "Sam"
senhaSalvo = "123"

login = input("Informe seu número de mátricula: ")
senha = input("Informe sua senha numerica: ")

if login == loginSalvo and senha == senhaSalvo:
    print(f"Bem vindo {loginSalvo}")
else:
    print("Login ou senha inválidos")