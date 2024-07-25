""" 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) 
e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, 
de acordo com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25."""

sGenero = input ("Informe o gênero M/F: ") 
nIdade = int(input ("Informe sua idade: "))
nTempoServico = int(input ("Informe seu tempo de serviço em anos: "))

bPodeAposentar = (((sGenero == "F") and (nIdade > 60)) or ((sGenero == "M") and (nIdade > 65))) or \
                    (nTempoServico >= 30) or \
                    ((nIdade >= 60) and (nTempoServico >= 25))

print(f"Pode se aposentar? {bPodeAposentar}")
