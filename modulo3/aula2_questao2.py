""" 2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos 
onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). 
Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, 
e False caso contrário."""

nJuliana=int(input("Qual idade de Juliana: "))
nCris=int(input("Qual idade de Cris: "))
bMaior17 = (nJuliana > 17) or (nCris > 17)
print(f"Juliana tem {nJuliana} anos e Cris tem {nCris} anos. Entrada permitida a ambos? {bMaior17}")