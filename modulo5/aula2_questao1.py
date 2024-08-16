""" 1) Faça um programa que gere aleatoriamente 20 valores 
inteiros entre -100 e 100 e os armazene em uma lista. 
Em seguida imprima na ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista """
import random
i=0
nIndiceMenorValor=0
nIndiceMaiorValor=0
lListaValores=[]
lListaOrdenada=[]
#gerar 20 número aleatórios
for i in range(1,20,1):
    lListaValores.append(random.randint(-100, 100))

nIndiceMenorValor=lListaValores.index(min(lListaValores))
nIndiceMaiorValor=lListaValores.index(max(lListaValores))
lListaOrdenada=sorted(lListaValores)

print(f"Lista Ordenada: {lListaOrdenada}")
print(f"Lista original: {lListaValores}")
print(f"O índice do menor valor da lista: {nIndiceMenorValor}")
print(f"O índice do maior valor da lista: {nIndiceMaiorValor}")