""" 
4) Reescreva o código a seguir para construir a lista aprovados 
usando compreensão de listas, ou seja, eliminando o laço de repetição.

alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = []
for i in range(len(notas)):
    if notas[i] >= 60:
      aprovados.append(alunos[i])
 """
i = 0
lListaAlunos = ["Maria", "Jose", "Carla", "Sol"]
lListaNotas = [35, 50, 20, 80]
lListaAprovados = [lListaAlunos[i] for i in range(len(lListaNotas)) if lListaNotas[i] >= 60]
print(lListaAprovados)