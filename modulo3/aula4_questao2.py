"""2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma 
escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:
Se a avaliação for 5, imprima "Excelente!"
Se a avaliação for 4, imprima "Muito Bom!"
Se a avaliação for 3, imprima "Bom!"
Se a avaliação for 2, imprima "Regular."
Se a avaliação for 1, imprima "Ruim."""

# entrada de dados
nAvaliacao = int(input("Avalie o filme assistido (nota entre 1 e 5): "))

# processamento 
if nAvaliacao == 5:
    sNota = "Excelente!" 
if nAvaliacao == 4:
    sNota = "Muito Bom!"
if nAvaliacao == 3:
    sNota = "Bom!"
if nAvaliacao == 2:
    sNota = "Regular!"
if nAvaliacao == 1:
    sNota = "Ruim!"

# saída de dados 
print(f"\033[3m Sua avaliação foi {nAvaliacao}, você classificou o filme como {sNota}! \033[0m")