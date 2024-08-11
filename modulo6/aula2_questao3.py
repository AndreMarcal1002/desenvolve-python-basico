""" 3) Preencha duas listas (lista1, lista2) com 20 valores 
inteiros aleatórios entre 0 a 50. 
Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas.
Ao final imprima:
Ambas as listas
A lista intersecção ordenada
A quantidade de vezes que cada elemento aparece em cada lista
Atenção, a lista de intersecções não pode ter duplicatas. 
Segue um exemplo da saída esperada.
lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
Interseccao - [10, 11, 20]
Contagem
10: (lista1=4, lista2=1)
11: (lista1=1, lista2=2)
20: (lista1=1, lista2=1)
 """
import random
i=0
lLista1=[]
lLista2=[]
lListaIntersecao=[]
# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
for i in range(20):
    lLista1.append(random.randint(0, 50))
    lLista2.append(random.randint(0, 50))

# Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas.
#for a in range(len(lLista1)): 
#    for b in range(len(lLista2)):
#        if lLista1[a]==lLista2[b]:
#            lListaIntersecao.append(lLista1[a])
for i in lLista1: 
    if (i in lLista2) and (i not in lListaIntersecao):
        lListaIntersecao.append(i)

lListaIntersecao=sorted(lListaIntersecao)
for i in lListaIntersecao:
    print(f"{i}: {lLista1.count(i)}, {lLista2.count(i)} ")

print(f"Lista 1: {sorted(lLista1)}")
print(f"Lista 2: {sorted(lLista2)}")
print(f"Lista interseção ordenada: {sorted(lListaIntersecao)}")
# print(f"Quantidade cada elemento aparece em cada lista: {sorted(lListaIntersecao)}")