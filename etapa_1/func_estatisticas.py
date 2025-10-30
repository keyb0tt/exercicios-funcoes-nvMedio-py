# Crie uma função estatisticas(lista) que receba uma lista e retorne o valor máximo, mínimo e média.
import os
os.system('clear')

def estatisticas(lista):
    valor_max = max(lista)
    valor_min = min(lista)
    valor_media = sum(lista) / len(lista)
    valores = [valor_max, valor_min, valor_media]
    
    return valores

numeros = [1, 2, 3, 4, 5]
resultados = estatisticas(numeros)

print(f'Valor máximo: {resultados[0]}\n'
      f'Valor mínimo: {resultados[1]}\n'
      f'Valor média: {resultados[2]}\n')