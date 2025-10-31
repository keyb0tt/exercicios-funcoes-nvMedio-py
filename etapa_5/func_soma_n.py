# Crie uma função recursiva soma_n(n) que calcule a soma de 1 até n.
import os
os.system('clear')

def soma_n(n):
    # Caso base
    if n == 0:
        return 0
    else:
    # Caso recursivo
        # print(n)
        return n + soma_n(n - 1)    

print(soma_n(5))