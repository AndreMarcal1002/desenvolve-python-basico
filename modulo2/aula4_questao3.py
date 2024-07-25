# Entrada:
# nome_produto1: calça  preco_unitario1: 199.90     qtde_produto1: 3
# nome_produto2: camisa preco_unitario2: 49.95      qtde_produto2: 10
# nome_produto3: cinto  preco_unitario3: 25         qtde_produto3: 3
# Saída:    Total: R$1,174.20

# ??? mensagem em itálico indicando o dado solicitado e dado de entrada em negrito
nome_produto1 = input("\033[3m Digite o nome do produto 1: \033[0m")
preco_unitario1 = float(input("\033[3m Digite o preço unitário do produto 1: \033[0m"))
qtde_produto1 = int(input("\033[3m Digite a quantidade do produto 1: \033[0m"))

nome_produto2 = input("\033[3m Digite o nome do produto 2: \033[0m")
preco_unitario2=float(input("\033[3m Digite o preço unitário do produto 2: \033[0m"))
qtde_produto2 = int(input("\033[3m Digite a quantidade do produto 2: \033[0m"))

nome_produto3 = input("\033[3m Digite o nome do produto 3: \033[0m")
preco_unitario3=float(input("\033[3m Digite o preço unitário do produto 3: \033[0m"))
qtde_produto3 = int(input("\033[3m Digite a quantidade do produto 3: \033[0m"))

#cálculo preço total da compra
preco_total_compra = (preco_unitario1*qtde_produto1)+(preco_unitario2*qtde_produto2)+(preco_unitario3*qtde_produto3)

print(f"Total: R$ {preco_total_compra:,.2f}")