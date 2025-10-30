# Crie uma função operacoes(a, b) que retorne a soma, subtração, multiplicação e divisão de a e b.
import os
os.system('clear')

def operacoes(a, b):

    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    resultados = [soma, sub, mult, div]

    print(f'Soma: {a} + {b} = {soma}\n'
          f'Subtração: {a} - {b} = {sub}\n'
          f'Multiplicação: {a} x {b} = {mult}\n'
          f'Divisão: {a} / {b} = {div}\n')
    
    return resultados
    

print(operacoes(5, 5))