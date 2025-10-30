# Crie uma função perfil(**dados) que receba nome, idade e curso (como parâmetros nomeados) e 
# retorne uma string formatada com as informações.
import os
os.system('clear')

def perfil(**dados):
    for key, data in dados.items():
        print(f'{key} = {data}')

nome = str(input('Nome: '))
os.system('clear')
idade = int(input('Idade: '))
os.system('clear')
curso = str(input('Curso: '))
os.system('clear')

dados_str = perfil(nome=nome, idade=idade, curso=curso)


