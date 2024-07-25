"""3) Você está desenvolvendo um programa para verificar se um ano é bissexto. 
Escreva um código em Python que solicita ao usuário para inserir um ano e 
imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, 
ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto".
Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 
2016 (bissexto) e 2017 (não bissexto). """

# entrada de dados
nAno = int(input("Insira um ano: "))

# processamento 
if (((nAno % 4) == 0) and ((nAno % 100) != 0)) or ((nAno % 400) == 0):
    sClassificacao = "bissexto" 
else: 
    sClassificacao = "não bissexto" 

# saída de dados 
print(f"\033[3m O ano escolhido é {sClassificacao}. \033[0m")