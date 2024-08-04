""" Transforme em código o fluxograma a seguir """

n=int(input("Insira um número n: ")) 
maior=0 
while (n>0):
    x=int(input("Insira um número x: ")) 
    if (x>maior):
        maior=x 
    n=n-1 
print(f" {maior}") 