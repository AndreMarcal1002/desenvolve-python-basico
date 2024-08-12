""" 
2) Dada uma lista de endereços web (URLs) que sempre começam com "www." 
e sempre terminam com ".com", use o conceito de fatiamento de listas para 
criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.

URLs: ["www.google.com&quot;, "www.gmail.com&quot;, "www.github.com&quot;, "www.reddit.com&quot;, "www.yahoo.com&quot;]
dominios:  ["google", "gmail", "github", "reddit", "yahoo"]
 """

sDominio=""
lLista1=["www.google.com&quot;", "www.gmail.com&quot;", "www.github.com&quot;", "www.reddit.com&quot;", "www.yahoo.com&quot;"]
print(f"Lista lLista1 - Lista original: {lLista1}")
#lLista2=["google", "gmail", "github", "reddit", "yahoo"]

for i in range(len(lLista1)):
    sDominio = lLista1[i]
    #retirar "www." de sDominio
    if sDominio.startswith('www.'):
        sDominio = sDominio.replace("www.", "")

    #retirar ".com&quot;" de sDominio
    if sDominio.endswith(".com&quot;"):
        sDominio = sDominio.replace(".com&quot;", "")
        
    lLista1[i] = sDominio

# Lista original  
print(f"Lista lLista1 atualizada - Lista domínio: {lLista1}")