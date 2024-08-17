""" 1) Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo 
local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
Ex: 
Digite uma frase: Bom2 dia, 123 meu nome é Davi 123.
Frase salva em /Users/laranjeira/python-basico/frase.txt
 """

import os # interação com o sistema operacional
# import sys # interação com o interpretador 

#sFrase = "\n Frase do usuário2" 
sFrase = input("Insira uma frase: ")
sArquivo1 = "frase.txt" # nome do arquivo.txt

if os.path.isfile(sArquivo1):
    print(f"Nome de arquivo {sArquivo1} já existe. O texto será sobrescrito.")

fiArquivo = open(sArquivo1, "w", encoding="utf-8") # abrir arquivo frase.txt. Modo "w" e "a" criam novos arquivos
fiArquivo.write(sFrase) # escrever no arquivo frase.txt
fiArquivo.close() # fechar arquivo frase.txt para salvar

# bloco interno de comando de manipulação de arquivo.
# with open("frase.txt", "w", encoding="utf-8") as fiArquivo: 
#    fiArquivo.write(sFrase) # escrever no arquivo frase.txt

# sCaminhoArquivo1 = os.getcwd() # caminho do arquivo1
sCaminhoArquivo1 = os.path.abspath(sArquivo1) # caminho do arquivo2

print(f"Frase salva em {sCaminhoArquivo1}" ) # imprimir caminho completo do arquivo1

#fiArquivo = open(sArquivo1, "r", encoding="utf-8")
#sFrase = fiArquivo.read()
#fiArquivo.close()
#print(sFrase)
