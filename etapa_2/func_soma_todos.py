# Crie uma função soma_todos(*numeros) que some todos os números passados.
import os
os.system('clear')

def soma_todos(*numeros):
    return sum(numeros)

print(f'{soma_todos(1, 2, 3, 4, 5)=}')