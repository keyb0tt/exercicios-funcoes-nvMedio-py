# Crie uma função temperaturas(celsius) que receba uma lista de temperaturas em °C e 
# retorne uma lista com as mesmas em °F.
import os
os.system('clear')

def temperaturas(celsius):
    def celsius_to_fahr(temp_c):
        temp_f = (temp_c * 1.8) + 32
        return temp_f
    
    fahrenheit = []
    for temp_c in celsius:
        temp_f = celsius_to_fahr(temp_c)
        fahrenheit.append(round(temp_f, 1))
    return fahrenheit

lista_c = [30, 40, 35, 37]
lista_f = temperaturas(lista_c)
print(f'{lista_c=}')
print(f'{lista_f=}')

