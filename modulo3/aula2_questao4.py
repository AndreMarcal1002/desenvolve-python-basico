""" Escolha a classe (guerreiro, mago ou arqueiro): mago
Digite os pontos de força (de 1 a 20): 8
Digite os pontos de magia (de 1 a 20): 17
Pontos de atributo consistentes com a classe escolhida: True 
"""
# sistema para validar uma ficha de personagem
""" Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), 
    os pontos de força e os pontos de magia atribuídos ao personagem."""
sClassePersonagem = input("\033[1m Escolha a classe ((G)uerreiro, (M)ago ou (A)rqueiro): \033[0m")
nPontosForca = int(input("\033[1m Digite os pontos de força (de 1 a 20): \033[0m"))
nPontosMagia = int(input("\033[1m Digite os pontos de magia (de 1 a 20): \033[0m"))
bAtributoConsistente =  ((sClassePersonagem == "G") and (nPontosForca >= 15) and (nPontosMagia <= 10)) or \
                        ((sClassePersonagem == "M") and (nPontosForca <= 10) and (nPontosMagia >= 15)) or \
                        (sClassePersonagem == "A") and ((nPontosForca > 5) and (nPontosForca <= 15)) and \
                                                        ((nPontosMagia > 5) and (nPontosMagia <= 15))

print(f"\033[3m Pontos de atributo consistentes com a classe escolhida: {bAtributoConsistente} \033[0m")