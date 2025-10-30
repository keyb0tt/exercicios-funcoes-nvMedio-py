# Crie uma função maior_valor(*valores) que retorne o maior entre todos os argumentos recebidos.
import os
os.system('clear')

def maior_valor(*valores):
    if not valores:
        return None
    return max(valores)

print(f'{maior_valor(1, 5, 9, 1)=}')