# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
lListaPares = [i for i in range(20,51,2) if ((i%2)==0)]
print(f"Todos os números pares entre 20 e 50: {lListaPares}")

# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lLista1 = [1,2,3,4,5,6,7,8,9]
lListaElevaQuadrado = [i**2 for i in lLista1 ]
print(f"Os quadrados de todos os valores da lista {lLista1} são: {lListaElevaQuadrado}")

# Todos os números entre 1 e 100 que sejam divisíveis por 7
lListaDivisivel7 = [i for i in range(1,101,2) if ((i%7)==0)]
print(f"Todos os números entre 1 e 100 que sejam divisíveis por 7: {lListaDivisivel7}")

#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento 
lListaParidade = ['par' if ((i%2)==0) else 'ímpar' for i in range(0,30,3) ]
print(f"Todos os números pares entre 20 e 50: {lListaParidade}")