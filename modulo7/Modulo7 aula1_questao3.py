""" Escreva um script que dado uma frase conta os espaços 
em branco.
Digite a frase: Meu amor mora em Roma e me deu um ramo de 
flores 
Espaços em branco: 11
 """
#sFrase = "Meu amor mora em Roma e me deu um ramo de flores" 
sFrase = input("Digite uma frase: ")
nEspacoBranco = 0
for i in range(0, len(sFrase)): 
    if sFrase[i] == " ": 
        nEspacoBranco = nEspacoBranco + 1

print(f"Frase original: {sFrase}")
print(f"Espaço(s) em branco: {nEspacoBranco}")