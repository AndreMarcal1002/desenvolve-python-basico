""" 2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
Ex:
Digite uma frase: O rato roeu a roupa do rei
Frase modificada: * r*t* r*** * r**p* d* r**
"""

lListaVogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#sFrase = "O rato roeu a roupa do rei" 
sFrase = input("Digite uma frase: ")

lListaVogalFormatada = ["*" if sFrase[i] in lListaVogal else sFrase[i] for i in range(len(sFrase))]
#sFraseFormatada = ""
#for i in lListaVogalFormatada:
#    sFraseFormatada = sFraseFormatada + i

sFraseFormatada = "".join(lListaVogalFormatada)

print(f"Frase original: {sFrase}")
print(f"Frase formatada: {sFraseFormatada}")
