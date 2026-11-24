
# El professor diu que string és lo que més s'empra a sa informàtica. string = cadena de caràcters
# Hem d'emprar tant els condicionals com ses
# explicacióllista -> conjunt d'elements que no tenen per què ser iguals (poden ser de tipus diferents, com una capsa) (com tenen un ordre a cada posició els hi podem canviar). 
# QUÈ FA EL CODI QUE ARA FUNCIONA? -> Demanar números per crear una llista de cinc i imprimir-la invertida (ordre dels números invertit)
l=list() # crear una llista assignada a una variable
for i in range(5): # repetir cinc vegades
    l.append(int(input("Intro un número: "))) # IMPORTANT INT. AFEGIR ELEMENTS A LA LLISTA demanant a l'usuari el número

l2 = list()
for i in range(len(l)):
    l2.append(l[i])
for i in range(4,-1, -1):
    l2.append(l[i])
print(l2)

# for e in l:
#   print(e)

#print(", ".join(l)) # NOMÉS FUNCIONA SI ÉS UN STRING, ARA ÉS INT

# A cada element de la llista sumar un número llegit
#k = int(input("Intro el número a sumar: "))
#for i in range(len(l)):
#    l[i] = l[i]+k
#for e in l:
#    print(e)
