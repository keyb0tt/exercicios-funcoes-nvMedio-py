# Crie uma função contar_palavras(lista_texto) que receba uma lista de frases e retorne
# quantas palavras há no total.
import os
os.system('clear')

def contar_palavras(lista_texto):
    soma_palavras = 0
    
    for frase in lista_texto:
        soma_palavras += len(frase.split())
    return soma_palavras

frases = ['Arroz e feijão', 'Bife acelobado', 'Imposto de renda']
qnt_palavras = contar_palavras(frases)

print(f'{qnt_palavras=}')