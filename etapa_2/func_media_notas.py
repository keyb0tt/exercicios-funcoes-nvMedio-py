# Crie uma função media_notas(*notas) que calcule a média das notas passadas, independente da quantidade.
import os
os.system('clear')

def media_notas(*notas):
    media = sum(lista_notas) / len(lista_notas)
    return media

lista_notas = [10, 7, 8, 5, 6]
media = media_notas(lista_notas)

print(f'{media=}')
