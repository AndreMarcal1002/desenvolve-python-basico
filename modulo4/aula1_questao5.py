""" 
Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. 
Ao final, imprima a média das idades.
(idade1 + idade2 + idade3 + … + idade_n)/N
"""

nTotalRespondente=int(input("Insira um número N: ")) 
n=nTotalRespondente
nIdade=0 
nSomaIdade=0 
nMedia=0 
while (n>0):
    nIdade=int(input("Insira a idade do respondente: ")) 
    nSomaIdade=nSomaIdade+nIdade
    n=n-1 
nMedia=(nSomaIdade/nTotalRespondente)
print(f"A média das idades é: {nMedia}")