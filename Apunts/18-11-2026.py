# 2.2.2 Llistes, que són el tipus de dades més important de Python
# prova6.py

l=[1, 2, [2, 3], "Hola"]

print(l[3][3]) # Imprimeix "a" sense les cometes

l[3]="Hola"
print(l[::-1])

for e in l:
    print(e) # Imprimirà cada valor de la llista. ÍNDEX (POSICIÓ) DINS SA LLISTA. for -> per fer un recorregut

# Com canviariem tots els 1s d'una llista a un altre número

for i in range(len(l)):
    print(i)

for i,e in enumerate(l):
    print("La posició {} val {}".format(i, e))
    if e == 1 or e == "1":
        l[i]="a"
for e in l:
    print("ho he afegit jo per identificar què s'està imprimint --->",e)

# ----------------------------------------------------

print("Canviar 2 per b -------------------------------")

l=[1, 2, [2, 3], "Hola"]

for i,e in enumerate(l):
    if e == 2 or e == "2":
        l[i]="b"
    if 2 in e: # Mirar si 2 está en el elemento que es una lista dentro de una lista, sino no coge el 2 de dentro del valor de la lista dentro de la lista
        pass # ignora açò, no acaba de funcionar perquè em vaig oblidar de copiar-ho tot. no sé perquè if 2 in e: no hi funciona
# Per a afegir elements a una llista de Python

l=list() #l és una llista
for i in range(10):
    l.append(int(input("Introduce un número: "))) # Leer diez números

for e in l:
    print(e) # per cada posició me retorna s'element de sa llista