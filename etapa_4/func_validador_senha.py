# Crie uma função validador_senha(senha) que tenha uma função interna tem_numero() e outra
# tem_maiuscula(); retorne True se a senha for forte.
import os
os.system('clear')

def validador_senha(senha):
    validador_num = False
    validador_char = False

    def tem_numero(senha_def):
        int_filter = ''.join(filter(str.isdigit, senha_def))

        if len(int_filter) > 0:
            return True
        else:
            return False
    
    def tem_maiuscula(senha_def):
        for caracter in senha_def:
            if isinstance(caracter, str) and caracter.upper() == caracter:
                return True



print(validador_senha('sexosemprotecao123.'))