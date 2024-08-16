""" 2) Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da ) 
soma dos valores. Peça ao usuário o valor de n
Biblioteca random: Função  HYPERLINK "https://docs.python.org/pt-br/3/library/random.html#random.randint"randint()
Biblioteca math: Função  HYPERLINK "https://docs.python.org/pt-br/3/library/math.html#math.sqrt"sqrt()
 """

import math
import random 
nSomatorio = 0 
nRaizQuadrada = 0
nQtdeValores = int(input("Insira a quantidade de valores: "))
for i in range(0, nQtdeValores, 1):
    nSomatorio = nSomatorio + random.randint(0,100)
nRaizQuadrada = math.sqrt(nSomatorio)
print (f"A raiz quadrada da soma dos valores é: {nSomatorio:,.2f}")