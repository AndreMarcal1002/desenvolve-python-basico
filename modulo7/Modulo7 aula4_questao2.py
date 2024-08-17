""" 2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt",
 removendo todos os espaços em branco e caracteres não  alfabéticos, e separando cada palavra em uma linha. 
 Ao final, imprima o conteúdo do arquivo "palavras.txt".
Ex:
Bom
dia
meu
nome
é
Davi
 """
import os # interação com o sistema operacional
import re

sArquivo1 = "frase.txt"
sArquivo2 = "palavras.txt"

fiArquivo = open(sArquivo1, "r", encoding="utf-8")
sFrase = fiArquivo.read()
fiArquivo.close()
#print(f"Impressão frase arquivo original. {sFrase}")


# bloco interno de comando de manipulação de arquivo.
with open(sArquivo2, "w", encoding="utf-8") as fiArquivo: 
    sFrase = re.sub("[0-9]", "", sFrase) # remover os caracteres numéricos
    lFrase = sFrase.split(" ") # colocar palavras numa lista
    #lFrase = [i.strip() for i in lFrase] # remover espaços em branco do início e fim do elemento
    
    for i in range(len(lFrase)): # remover todos os espaços em branco e caracteres não  alfabéticos
        if lFrase[i] != "":
            sFrase = lFrase[i].strip() # remover todos os espaços em branco
            #sFrase = re.sub('[^a-zA-Z0-9]', '', lFrase[i]) # remover todos os caracteres especiais
            #sFrase = "".join(filter(str.isalnum, lFrase[i]))
            sFrase = re.sub(r"[\W_]+", "", lFrase[i]) # remover todos os caracteres não alfanuméricos MELHOR SOLUÇÃO USANDO EXPRESSÕES REGULARES
            sFrase = "\n" + sFrase
            fiArquivo.write(sFrase)

#print(f"Impressão diretório em que frase foi salva: {os.path.abspath(sArquivo2)}") # imprimir caminho completo do arquivo
fiArquivo = open(sArquivo2, "r", encoding="utf-8")
print(f"Impressão do conteúdo do arquivo {sArquivo2}. {fiArquivo.read()}")