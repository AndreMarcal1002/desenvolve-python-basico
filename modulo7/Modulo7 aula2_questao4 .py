""" 4) Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida 
atende todos os seguintes critérios:
"""

def fValidadorSenha(sFrase, lLista): # saber se as letras da senha atendem condição de ter pelo menos uma ocorrência
    nOcorrencia = 0

    #opção 2
    for i in range(len(sFrase)):
        if sFrase[i] in lLista:
            nOcorrencia = nOcorrencia + 1 
    return nOcorrencia 
"""  
    # opção 1
    nOcorrencia = [1  for i in range(len(sFrase)) if sFrase[i] in lLista]
    return nOcorrencia 
"""
    
# Inicialização variáveis
lListaNumero = ["0","1","2","3","4","5","6","7","8","9"]
lListaCaracterEspecial = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "^", "`", "{", "|", "}", "~" ]
lListaLetraMaiuscula = ["A", "E", "I", "O", "U", "B", "C", "D", "F","G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Y", "W", "Z"]
lListaLetraMinuscula = ["a", "e", "i", "o", "u", "b","c", "d", "f","g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z"]
i = 0
sSenha = "1@Senhasenha" # variável teste
# entrada
#sSenha = input("Insira uma senha com no mínimo 8 caracteres: ")

# Senha com pelo menos 8 caracteres de comprimento.
if (len(sSenha) < 8):
    print(f"Senha inválida. A senha deverá conter no mínimo 8 caracteres.")

# Senha com pelo menos um número    
elif (fValidadorSenha(sSenha, lListaNumero) == 0):
    print(f"Senha inválida. A senha deverá conter pelo menos um número.")

# Senha com pelo menos um caractere especial.
elif (fValidadorSenha(sSenha, lListaCaracterEspecial) == 0):
    print(f"Senha inválida. A senha deverá conter pelo menos um caractere especial.")

# Contém pelo menos uma letra maiúscula 
elif (fValidadorSenha(sSenha, lListaLetraMaiuscula) == 0):
    print(f"Senha inválida. A senha deverá conter pelo menos uma letra maiúscula.")

# Contém pelo menos uma letra minúscula
elif (fValidadorSenha(sSenha, lListaLetraMinuscula) == 0):
    print(f"Senha inválida. A senha deverá conter pelo menos uma letra minúscula.")

else:
    print(f"Senha Válida.")


