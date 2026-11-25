# Llegir 10 noms i juntar-los de 2 en dos i llavors imprimir-los
l = list()

for i in range(10):
    l.append(int(input("Nombre: ")))
suma = 0
for i in range(0,10,2):
    suma = suma + l[i]
print(suma)
