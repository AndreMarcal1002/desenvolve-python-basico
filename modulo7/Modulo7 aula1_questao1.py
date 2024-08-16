""" Escreva um programa que solicita o nome do usuário e o 
imprime em forma de escada, como indicado no exemplo a seguir.
Digite seu nome: Fulano
F
Fu
Ful
Fula
Fulan
Fulano

 """
i = 0
sFrase =""
sIndex = ""

sFrase = input("Digite um nome: ")

for i in range(len(sFrase)): 
    sIndex = sIndex + sFrase[i]
    print(f"{sIndex}")

