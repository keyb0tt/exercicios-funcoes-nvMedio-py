# Crie uma função formatar_nome_completo(nome, sobrenome) que use uma função interna 
# capitalizar() para deixar as iniciais maiúsculas.
import os
os.system('clear')

def formatar_nome_completo(nome, sobrenome):
    def capitalizar(palavra):
        return palavra.capitalize()

    nome = capitalizar(nome)
    sobrenome = capitalizar(sobrenome)

    return {
        'nome': nome,
        'sobrenome': sobrenome,
    }

print(formatar_nome_completo('kaique', 'bosco'))
    