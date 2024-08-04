""" Exercício de maratona: https://www.beecrowd.com.br/judge/pt/problems/view/1094
Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual 
de cada tipo de cobaia utilizada. 
Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados.

As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas 
e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada 
uma em relação ao total de cobaias utilizadas
 """
# inicialização de dados
nQtdeTotalCobaia=0
nQtdeCobaia = 0 
nQtdeSapo = 0
nQtdeRato = 0
nQtdeCoelho = 0
nQtdeExperimento = int(input("Insira a quantidade de experimentos registrados: ")) 
nCont=0
#processamento
while (nCont < nQtdeExperimento):
    nQtdeCobaia = int(input("Insira a quantidade de cobaia: ")) 
    sTipoCobaia = input("Insira o tipo de cobaia: ") 
    if sTipoCobaia == 'S':
        nQtdeSapo = nQtdeSapo + nQtdeCobaia 
    elif sTipoCobaia == 'R':
        nQtdeRato = nQtdeRato + nQtdeCobaia 
    elif sTipoCobaia == 'C': 
        nQtdeCoelho = nQtdeCoelho + nQtdeCobaia 
    else: 
        print(f"{sTipoCobaia} Não existe este tipo de cobaia. Entre com novos dados.")
    nCont = nCont + 1 

nQtdeTotalCobaia = nQtdeSapo + nQtdeRato + nQtdeCoelho
# Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas
print(f"Total de cobaias: {nQtdeTotalCobaia}.")
print(f"Total de sapos: {nQtdeSapo}. Percentual de sapos: {nQtdeSapo/nQtdeTotalCobaia:,.2f}.")
print(f"Total de ratos: {nQtdeRato}. Percentual de ratos: {nQtdeRato/nQtdeTotalCobaia:,.2f}.")
print(f"Total de coelhos: {nQtdeCoelho}. Percentual de coelhos: {nQtdeCoelho/nQtdeTotalCobaia:,.2f}.")