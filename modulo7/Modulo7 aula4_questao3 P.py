""" 3) Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador 
com o nome "estomago.txt". 
Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
O texto das primeiras 25 linhas 
O número de linhas do arquivo
A linha com maior número de caracteres
O número de menções aos nomes dos personagens "Nonato" e 
"Íria" (inclua todas as variações de maiúsculas e minúsculas 
e atenção para não incluir a substring "iria" se ela fizer 
parte de outras palavras).
 """
sNomeArquivo = "estomago.txt"
#Texto = open(sNomeArquivo, "r", encoding="utf-8")
#sTexto = fArquivoTexto.readlines()
#i=1
#for sLinha in sTexto:
#    if (i <= 25):
#        sLinha = sLinha.strip()
#        print(f"Linha {i}: {sLinha}")
#        i=i+1
#    else:
#        break
#fArquivoTexto.close()
with open(sNomeArquivo, "r") as fArquivoTexto: # Porque ocorre erro se colocar encoding="utf-8"?
    sTexto = fArquivoTexto.readlines()
    i=1
    for sLinha in sTexto:
        if (i <= 25):
            sLinha = sLinha.strip()
            print(f"{len(sLinha)}. Linha {i}: {sLinha}")
            i=i+1
        else:
            break
# imprimir o número de linhas do arquivo
print(f"Total de linhas do arquivo: {len(sTexto)}")
# imprimir a linha com maior número de caracteres
nLinhaMaior = 0
nTamanhoMaior = 0
nTamanhoLinha = 0
with open(sNomeArquivo, "r") as fArquivoTexto: # Porque ocorre erro se colocar encoding="utf-8"?
    sTexto = fArquivoTexto.readlines()
    i = 0
    for sLinha in sTexto:
        sLinha = sLinha.strip()
        nTamanhoLinha = len(sLinha)
        if (nTamanhoMaior < nTamanhoLinha):
            nTamanhoMaior = nTamanhoLinha
            nLinhaMaior = i
        i+=1
    print(f"A linha {nLinhaMaior} possui o maior número de caracteres. {nTamanhoMaior}")
        
# imprimir o número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas 
# e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).
