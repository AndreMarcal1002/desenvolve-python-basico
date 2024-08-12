""" 4) Crie um programa em Python que receba duas listas de 
números do usuário, podendo cada lista ter uma quantidade 
diferente de valores. Em seguida, combine essas duas listas 
de forma alternada para formar uma terceira lista. 
Intercale os elementos até o final da primeira lista, 
adicionando ao final os elementos remanescentes da maior 
lista.
Exemplo de interação via terminal (entradas em negrito):
Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1
2
3
4Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5
6
7
8
9
10Lista intercalada: 1 5 2 6 3 7 4 8 9 10
 """
#import random

def fPreencheValores(nQtde):
    lLista=[]
    for i in range(nQtde):
        lLista.append(int(input("Insira valores na lista: ")))
        #lLista.append( random.randint(0, 10) )
    return lLista
        
i=0
nQtdeValores=0
lLista1=[]
lLista2=[]
lLista3=[]

# Preencha lista1
nQtdeValores = int(input("Insira a quantidade de valores na lista 1: "))
lLista1 = fPreencheValores(nQtdeValores)

# Preencha lista2
nQtdeValores=int(input("Insira a quantidade de valores na lista 2: "))
lLista2 = fPreencheValores(nQtdeValores)

# Formar lista3
if len(lLista1) <= len(lLista2):
    for i in range(0, len(lLista1), 1): 
        lLista3.append( lLista1[i] )
        lLista3.append( lLista2[i] )

    for i in range(len(lLista1), len(lLista2), 1):
        lLista3.append( lLista2[i] )
else: 
    for i in range(0, len(lLista2), 1): 
        lLista3.append( lLista1[i] )
        lLista3.append( lLista2[i] )
    for i in range(len(lLista2), len(lLista1), 1):
        lLista3.append( lLista1[i] )

print(f"Lista 1: {lLista1}")
print(f"Lista 2: {lLista2}")
print(f"Lista 3: {lLista3}")