import os
import time
os.system("cls")

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def taxaDoAmor(n1):
    if n1 < 100:
        return n1 + n1 * 0.10
    else:
        return n1 + n1 * 0.10

        