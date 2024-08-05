""" 1) Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e 
calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir 
que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
	Exemplo de interação:
Digite o primeiro número: 3.1415
Digite o segundo número: 1.4142
A diferença absoluta entre os números é: 1.73 """

nPrimeiroNumero = float(input("Insira primeiro número decimal: ")) 
nSegundoPrimeiroNumero = float(input("Insira segundo número decimal: ")) 
nResultado = 0 
nResultado = round(abs(nPrimeiroNumero-nSegundoPrimeiroNumero),2)
print(f"A diferença absoluta entre os números é: {nResultado}.")