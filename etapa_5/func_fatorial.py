# Crie uma função recursiva fatorial(n) que calcule o fatorial (sem usar math).
import os
os.system('clear')

def fatorial(n):
    # Caso base (aonde termina)
    if n == 0 or n == 1:
        return 1
    else:
    # Caso recursivo (reutiliza função)
        return n * fatorial(n - 1)
    
print(fatorial(5))