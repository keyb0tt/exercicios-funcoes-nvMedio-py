# Crie uma função filtrar_pares(lista) que retorne apenas os números pares de uma lista.
import os
os.system('clear')

def filtrar_pares(lista):
    lista_pares = []

    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares

numeros = [1, 2, 3, 4, 5]
numeros_pares = filtrar_pares(lista=numeros)

print(f'{numeros=}')
print(f'{numeros_pares=}')