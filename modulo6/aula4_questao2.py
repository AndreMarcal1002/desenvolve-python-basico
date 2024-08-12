""" 
2) Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase
Exemplo:
Digite uma frase: Eu gosto de programar em Python
Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

# Separar vogal e consoante
for i in range(len(sFrase)):
    if sFrase[i] in lListaVogal:
        lListaVogalFrase.append(sFrase[i])
    elif sFrase[i] in lListaConsoante:
        lListaConsoanteFrase.append(sFrase[i])
"""
 
i = 0
lListaVogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
lListaConsoante = ["b", "c", "d", "f","g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z", "B", "C", "D", "F","G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Y", "W", "Z"]
lListaVogalFrase = []
lListaConsoanteFrase = []
# entrada
sFrase = input("Digite uma frase: ")
sFrase = sFrase.strip("") # retirar espaços da string
# Separar vogal e consoante 
lListaVogalFrase = [sFrase[i] for i in range(len(sFrase)) if sFrase[i] in lListaVogal]
lListaConsoanteFrase = [sFrase[i] for i in range(len(sFrase)) if sFrase[i] in lListaConsoante]
# ordenar a lista de vogais
lListaVogalFrase = sorted(lListaVogalFrase)
# saída
print(f"Vogais: {lListaVogalFrase}")
print(f"Consoantes: {lListaConsoanteFrase}")