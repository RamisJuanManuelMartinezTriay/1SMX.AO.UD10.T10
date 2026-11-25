# Llegir 10 números i guardar-los en una llista. Després crear una nova llista amb els seus quadrats (i²). Imprimir els números i al costat el seu quadrat

l = list()

r = list()

for i in range(10):
    l.append(int(input("Número: ")))

    r.append(l[i]**2)

for i in range(10):
    print("El quadrat de {} és {}".format(l[i],r[i]))