""" 1) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
Dica: usando listas você não precisa fazer um "if" para cada mês.
Ex:
Digite uma data de nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
 """
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

sDtaAniversario = input("a data de nascimento (dd/mm/aaaa) do usuário: ")
dDtaFormatada = datetime.strptime(sDtaAniversario, "%d/%m/%Y")
#sDtaFormatada = dDtaFormatada.strftime("%d de %B de %Y")
print(f"{dDtaFormatada.strftime("%d de %B de %Y")}")
