# Llegir 10 noms i juntar-los de 2 en dos i llavors imprimir-los
l = list()

for i in range(10):
    l.append(input("Nom: "))

r = list()

for i in range(0, 10, 2):
    r.append(l[i]+" "+l[i+1])
print(r)

####################

r2 = list()

for i in range(5):
    r2.append(l[i]+" "+l[-(i+1)])

print(r2)

########################

r3 = list()

for r3 in range(1,10,2):
    print(r3) # AIXÓ NO FA EL QUE HA DE FER

####################### Posar en una llista del 9 al 0
k = list()

for k in range(9,2,2):
    pass #NO HO HE FET