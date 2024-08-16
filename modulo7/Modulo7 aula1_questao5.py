""" Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e 
quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
19 vogais
Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]
 """
i = 0
lListaVogalIndice = []
lListaVogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sFrase = input("Digite uma frase: ")
lListaVogalIndice = [i for i in range(len(sFrase)) if sFrase[i] in lListaVogal]
print(f"Quantidade de Vogais: {len(lListaVogalIndice)}")
print(f"Indices: {lListaVogalIndice}")
