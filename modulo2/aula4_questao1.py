#  Faça um programa para ler as dimensões de um terreno em inteiros 
# (comprimento e largura), bem como o preço do metro quadrado da região 
# em ponto flutuante. Calcule o valor do terreno e imprima o resultado 
# com a formatação apresentada a seguir.
# O terreno possui 250m2 e custa R$512,490.50
# Comente na linha acima de cada instrução uma breve descrição da instrução.
# Fórmulas:
# area_terreno=250 
# valor_terreno=512,490.50
# entrada de dados
comprimento=int(input("Informe o comprimento (m): "))
largura=int(input("Informe a largura (m): "))
preco_m2=float(input("Informe o preço por m2: "))
#cálculo da área 
area_m2=comprimento * largura
#cálculo valor do terreno
preco_valor_terreno=area_m2*preco_m2 
print(f"O terreno possui {area_m2} m2")
print(f"O terreno custa R$ {preco_valor_terreno:,.2f}")