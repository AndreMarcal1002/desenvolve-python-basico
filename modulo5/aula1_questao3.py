""" 3) Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório 
entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, 
muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
Exemplo de interação:
Adivinhe o número entre 1 e 10: 5
Muito alto, tente novamente!
Adivinhe o número entre 1 e 10: 3
Correto! O número é 3.
 """
# entrada de dados
import random 
nNumeroAleatorio = random.randint(0,10)
while True:
    nAdivinha = int(input("Tente adivinhar o valor entre 1 e 10: "))
    if (nAdivinha > nNumeroAleatorio):
        print("Escolha um número menor, tente novamente!") 
    elif (nAdivinha < nNumeroAleatorio):
        print("Escolha um número maior, tente novamente!") 
    elif (nAdivinha == nNumeroAleatorio):
        print(f"Você acertou! O número aleatório é {nNumeroAleatorio}")
        break