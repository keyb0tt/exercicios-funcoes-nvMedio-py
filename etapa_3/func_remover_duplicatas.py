# Crie uma função remover_duplicatas(lista) que retorne uma nova lista sem elementos repetidos.
import os
os.system('clear')

def remover_duplicatas(numeros):
    numeros_copy = set(numeros)

    return numeros_copy

numeros = [1, 2, 3, 3, 3, 4, 5, 6, 6]
numeros_copy = remover_duplicatas(numeros)

print(f'{numeros=}')
print(f'{numeros_copy=}')