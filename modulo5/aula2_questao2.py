""" 2) Faça um programa que gere aleatoriamente um valor 
entre 5 e 20 e armazene em uma variável chamada num_elementos. 
Em seguida gere aleatoriamente valores entre 1 e 10 em 
quantidade correspondente a num_elementos, e armazene em uma 
lista chamada elementos. Em seguida imprima:
A lista elementos
A soma dos valores da lista
A média dos valores da lista
 """
import random
i=0
nNumElemento=0
nSomaValores=0
nMediaValores=0
lListaElementos=[]
nNumElemento=random.randint(5,20)
#gere aleatoriamente um valor entre 5 e 20
for i in range(nNumElemento):
    lListaElementos.append(random.randint(1, 10))
nSomaValores=sum(lListaElementos)
nMediaValores=(nSomaValores/len(lListaElementos))
print(f"Lista de elementos: {lListaElementos}")
print(f"A soma dos valores da lista: {nSomaValores}")
print(f"A média dos valores da lista: {nMediaValores}")