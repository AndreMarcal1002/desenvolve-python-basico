""" 1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores 
de 17 anos, indicando que podem entrar no bar, e False caso contrário. """

nJuliana=int(input("Qual idade de Juliana: "))
nCris=int(input("Qual idade de Cris: "))
bMaior17 = (nJuliana > 17) and (nCris > 17)
print(f"Juliana tem {nJuliana} anos e Cris tem {nCris} anos. Entrada permitida a ambos? {bMaior17}")