# Crie uma função perfil(**dados) que receba nome, idade e curso (como parâmetros nomeados) e 
# retorne uma string formatada com as informações.
import os
os.system('clear')

def perfil(**dados):
    string_result = []

    

    for par_name, data in dados.items():
        
        string_result.append(f'{par_name} = {data}\n')

    return string_result

