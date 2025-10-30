# Crie uma função calculos(a, b) que tenha funções internas para somar, subtrair, multiplicar e dividir, 
# retornando os quatro resultados em um dicionário.
import os
os.system('clear')

def calculos(a, b):
    def soma(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b

    return {
        'soma': soma(a, b),        
        'sub': sub(a, b),     
        'mult': mult(a, b),        
        'div': div(a, b),        
    }

print(calculos(10, 10))

