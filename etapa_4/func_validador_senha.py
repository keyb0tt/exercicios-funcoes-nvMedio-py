# Crie uma função validador_senha(senha) que tenha uma função interna tem_numero() e outra
# tem_maiuscula(); retorne True se a senha for forte.
import os
os.system('clear')

def validador_senha(senha):
    def tem_numero(senha_def):
        int_filter = ''.join(filter(str.isdigit, senha_def))

        if len(int_filter) > 0:
            return True
        else:
            return False
            
    def tem_maiuscula(senha_def):
        upper_filter = ''.join(filter(str.isupper, senha_def))
        
        if len(upper_filter) > 0:
            return True
        else: 
            return False
            
    validador_num = tem_numero(senha)
    validador_char = tem_maiuscula(senha)

    if validador_num and validador_char:
        return True
    else:
        return False

print(f'{validador_senha('teste123')=}')
print(f'{validador_senha('teste')=}')
print(f'{validador_senha('123')=}')
print(f'{validador_senha('Teste')=}')
print(f'{validador_senha('Teste123')=}')