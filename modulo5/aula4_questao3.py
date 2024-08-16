""" 
3) Reescreva o código a seguir para construir a lista pagamentos usando 
compreensão de listas, ou seja, eliminando o laço de repetição.

horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = []
for hora in horas_trabalhadas:
    pagamentos.append(ganho_por_hora * min(hora, 40) + \
                                         hora_extra * max(0, hora-40))
print(pagamentos)

 """
nNum1 = 0
lListaPagamento = []
nGanhoHora = 20
nHoraExtra = 25
lListaHorasTrabalhadas = [40, 37, 45, 40, 40, 48]

lListaPagamento = [nGanhoHora * min(nNum1, 40) + nHoraExtra * max(0, nNum1-40) for nNum1 in lListaHorasTrabalhadas]
print(lListaPagamento)