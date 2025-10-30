# Crie uma função validador_senha(senha) que tenha uma função interna tem_numero() e outra
# tem_maiuscula(); retorne True se a senha for forte.
import os
os.system('clear')

def validador_senha(senha):
    validador_num = False
    validador_char = False

    def tem_numero(senha):


        int_filter = int(''.join(filter(str.isdigit, senha)))
        # senha_int = int(int_filter)
        return int_filter
        # for caracter in senha_int:
            # return isinstance(caracter, int)

    # def tem_maiuscula(senha):
        # for caracter in senha:
            # if isinstance(caracter, str) and caracter.upper() == caracter:
                # return True



print(validador_senha(123))