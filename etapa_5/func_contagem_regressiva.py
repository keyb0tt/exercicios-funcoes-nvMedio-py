# Crie uma função recursiva contagem_regressiva(n) que conte até zero.
import os
os.system('clear')

def contagem_regressiva(n):
    # Caso base
    if n < 0:
        return 'Número igual ou menor a zero.'
    # Ação
    print(n)
    # Caso recursivo
    contagem_regressiva(n - 1)

contagem_regressiva(10)
