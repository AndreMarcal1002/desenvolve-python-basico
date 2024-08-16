""" Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, 
acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. 
Adicione o separador "-" na sua impressão.
Digite o número: 97651234
Número completo: 99765-1234
Digite o número: 980876543
Número completo: 98087-6543 


10Lista intercalada: 1 5 2 6 3 7 4 8 9 10
 """
#sFrase = "97651234"
i=0 
sFrase2=""
sFrase = input("Digite um número de telefone celular com 9 dígitos: ")
if (len(sFrase) == 8):
    sFrase = "9" + sFrase
if (len(sFrase) == 9):
    if (sFrase[0] == "9"):
        # Adicione o separador "-" na sua impressão
        for i in range(0, len(sFrase)):
            if (i == 5): 
                sFrase2 = sFrase2 + "-"
            sFrase2 = sFrase2 + sFrase[i]

print(f"Frase original: {sFrase}")
print(f"Frase formatada: {sFrase2}")
