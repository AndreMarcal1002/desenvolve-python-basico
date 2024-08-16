""" 5) De acordo com uma pesquisa do linguista Matt Davis, 
o cérebro humano consegue ler palavras com as letras 
embaralhadas, contanto que a primeira e a última letra 
estejam no lugar correto. Implemente uma função chamada 
embaralhar_palavras() para ajudar a testar a hipótese do 
Matt Davis. Sua função vai receber uma frase, embaralhar 
as letras internas de cada palavra e retornar a frase 
modificada. Dica: use a biblioteca random.

Complete o seguinte código:
def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
 """
receber frase
colocar cada palavra da frase numa lista = lista formada de palavras
para cada palavra/elemento da lista
	retirar a 1ª letra da palavra/elemento (LetraPrimeira
	retirar a última letra da palavra/elemento ou inverter a palavra e retirar a 1ª letra.(LetraUltima)
	retirar as letras que sobraram e embaralhar (função?) ou colocar essas letras numa lista e embaralhar? (LetrasEmbaralhadas)
	montar a palavras com LetraPrimeira+LetrasEmbaralhadas+LetraUltima
colocar cada palavra/elemento da lista numa string
imprimir

