# 2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit 
# e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e 
# F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. 
# A mensagem deve estar formatada da seguinte maneira:
# 86 graus Fahrenheit são 30 graus Celsius.

# entrada de dados
temperatura_fahrenheit=int(input("Informe a temperatura em graus Fahrenheit: "))
#conversão 
temperatura_celsius=(temperatura_fahrenheit-32)* (5/9)
print(f"{temperatura_fahrenheit} graus Fahrenheit são {temperatura_celsius:,.0f} graus Celsius ")