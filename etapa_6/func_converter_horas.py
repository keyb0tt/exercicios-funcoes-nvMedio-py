# Crie uma função converter_horas(minutos) que converta minutos em horas e minutos 
# (ex: 125 → 2h 5min).
import os
os.system('clear')

def converter_horas(minutos):
    horas = 0

    while minutos >= 60:
        if minutos >= 60:
            horas += 1
            minutos -= 60
    
    return print(f'{horas}h {minutos}min')

converter_horas(150)