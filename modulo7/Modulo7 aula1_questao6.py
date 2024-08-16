""" Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
Anagramas são palavras com os mesmos caracteres rearranjados.
 """
sFrase = "Meu amor mora em Roma e me deu um ramo de flores"
sPalavraObjetivo = sorted("amor")

lListaFrase = sFrase.lower().split(" ")

for i in lListaFrase:
    if sorted(i) == sPalavraObjetivo:
        print(f"Os anagramas são: {i}")
