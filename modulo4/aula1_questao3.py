""" Transforme em código o fluxograma a seguir """

n1 = int(input("Insira um número n1: ")) 
n2 = int(input("Insira um número n2: ")) 
n3 = int(input("Insira um número n3: ")) 
m = (n1+n2+n3)/3
if (m >= 60): 
    print(f" Aprovado") 
elif (m >= 40): 
    print(f" Recuperação") 
else: 
    print(f" Reprovado") 
print(f" FIM") 