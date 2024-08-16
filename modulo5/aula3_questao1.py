""" 
1) Escreva um script em Python que solicita do usuário uma quantidade 
indefinida de números inteiros (pelo menos 4 valores), os armazena em 
uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … ) 
"""

#import random
i=0
lLista1=[]
lLista2=[]
lLista3=[]
lLista4=[]
lLista5=[]
lLista6=[]

# Preencha lista1
nQtdeValores = int(input("Insira a quantidade de valores na lista 1: "))
for i in range(nQtdeValores):
    lLista1.append(int(input("Insira valores na lista: ")))
    #lLista1.append( random.randint(0, 10) )

# Lista original  
print(f"Lista lLista1 - Lista original: {lLista1}")

# Os 3 primeiros elementos
lLista2=lLista1[0:3:1]
print(f"Lista lLista2 - Os 3 primeiros elementos: {lLista2}")

# Os 2 últimos elementos
lLista3=lLista1[-2:len(lLista1):1]
print(f"Lista lLista3 - Os 2 últimos elementos: {lLista3}")

# A lista invertida (do fim para o começo)
#lLista4=lLista1[len(lLista1):0:-1]
lLista4=lLista1[::-1]
print(f"Lista lLista4 - A lista invertida (do fim para o começo): {lLista4}")

# Os elementos de índice par (0, 2, 4 … )
lLista5=lLista1[0:len(lLista1):2]
print(f"Lista lLista5 - Os elementos de índice par: {lLista5}")

# Os elementos de índice ímpar (1, 3, 5, … ) 
lLista6=lLista1[1:len(lLista1):2]
print(f"Lista lLista6 - Os elementos de índice ímpar: {lLista6}")