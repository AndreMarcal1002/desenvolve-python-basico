""" 
Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, 
bem como a chave da criptografia. Regras:
Chave de criptografia: gere um valor n aleatório entre 1 e 10
Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de 
caracteres visíveis (entre 33 e 126 na tabela Unicode)

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = 5
nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']
"""
import random

def fCriptografia(sCaracter, nChave, nCaracterMin=33, nCaracterMax=127):
    nCaracter = ord(sCaracter) + nChave
    return chr(nCaracter) if nCaracter < nCaracterMax else chr(nCaracterMin + nCaracter % nCaracterMax)


lListaFrase = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nChaveAleatoria = random.randint(1,10)
# nChaveAleatoria = 5
lListaCriptografada = []

for i in range(len(lListaFrase)):
    lPalavra = [y for y in lListaFrase[i]]
    print(f"lPalavra é {lPalavra}")
    for y in range(len(lPalavra)):
        lListaCriptografada = map(fCriptografia(lPalavra[y], nChaveAleatoria), [2]*len(lListaFrase[y]))
    print(list(map(lListaCriptografada,lListaFrase[i], [2]*len(lListaFrase[i])))) # ERRO

print(f"A lista original é: {lListaFrase}")
# print(f"A lista original é: {lListaCriptografada}") # está imprimindo o endereçamento e não a lista
print(f"A chave aleatória é: {nChaveAleatoria}")


# print(list(map(fCriptografia(), lListaFrase[i], [2]*len(lListaFrase[i]))))
