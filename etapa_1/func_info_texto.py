# Crie uma função info_texto(texto) que retorne o número de caracteres, o número de palavras e o número de vogais.
import os
os.system('clear')

def contar_vogais(texto):
    vogais = 'aeiou'
    cont_vogais = 0
    lista_letras = list(texto)

    for letra in lista_letras:
        if letra.lower() in vogais:
            cont_vogais += 1
    return cont_vogais

def info_texto(texto):
    letras = list(texto)
    palavras = texto.split()

    qnt_letras = len(letras)
    qnt_palavras = len(palavras)
    qnt_vogais = contar_vogais(texto)

    result = [qnt_letras, qnt_palavras, qnt_vogais]
    return result

texto = 'Meu escritório é na praia'
info_lista = info_texto(texto)

qnt_letras = info_lista[0]
qnt_palavras = info_lista[1]
qnt_vogais = info_lista[2]

print(f'{qnt_letras=}\n'
    f'{qnt_palavras=}\n'
    f'{qnt_vogais=}\n')

