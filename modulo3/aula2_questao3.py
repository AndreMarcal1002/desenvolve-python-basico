#
nIdadeUsuario=int(input("\033[1m Digite sua idade:  \033[0m"))
bJogouAntes3=input("\033[1m Já jogou pelo menos 3 jogos de tabuleiro (TRUE/FALSE)? \033[0m") #resposta deve ser True ou False
nVenceu=int(input("\033[1m Quantos jogos já venceu? \033[0m"))

bPodeEntrar = ((nIdadeUsuario >= 16) and (nIdadeUsuario <= 18)) and \
                (bJogouAntes3 == "TRUE") and \
                (nVenceu > 0)

print(f"\033[3m Apto para ingressar no clube de jogos de tabuleiro? {bPodeEntrar} \033[0m")