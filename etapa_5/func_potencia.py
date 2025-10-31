# Crie uma função recursiva potencia(base, expoente) que calcule a potência sem usar o operador **.
import os
os.system('clear')

def potencia(base, expoente):
    if expoente == 0:
        return 0
    elif expoente == 1:
        return base
    else:
        return base * potencia(base, expoente - 1)
    
print(potencia(5, 3))