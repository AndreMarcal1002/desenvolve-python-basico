"""4) Você está implementando um sistema de entrega expressa e precisa calcular 
o valor do frete com base na distância e no peso do pacote. 

Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg"""

# entrada de dados 
nFrete = 0
nTaxaExcessoPeso = 10.00
nTarifa = 0 
nDistancia = int(input("Insira a distância para entrega (km): "))
nPeso = int(input("Insira o peso do pacote (kg): ")) 

# processamento 
if (nPeso > 10):
    nFrete = nFrete + nTaxaExcessoPeso 

if ((nDistancia > 0) and (nDistancia <= 100)): 
    nTarifa = 1.00 
if ((nDistancia > 100) and (nDistancia <= 300)): 
    nTarifa = 1.50 
if (nDistancia > 300):
    nTarifa = 2.00 

nFrete = nFrete + (nDistancia * nPeso * nTarifa)

# saída de dados 
print(f"\033[3m O valor do frete é {nFrete:,.2f} \033[0m")