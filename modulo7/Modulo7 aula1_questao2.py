""" Escreva um programa que solicite ao usuário inserir seu 
primeiro nome e sobrenome separadamente. 
Em seguida, concatene essas duas strings e exiba a mensagem 
de boas-vindas.
Digite seu primeiro nome: Alice
Digite seu sobrenome: Silva
Bem-vinda, Alice Silva! 


 """
sNome = ""
sSobrenome = ""
sNome = input("Insira o 1º nome: ")
sSobrenome = input("Insira o sobrenome: ")
sNome = "Bem-vindo(a) " + sNome + " " + sSobrenome +"!"
print (sNome)
