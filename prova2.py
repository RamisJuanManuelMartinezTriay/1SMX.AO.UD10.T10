for i in range(1,11,2):
    print(i) # Imprimeix els nombres parells

print("--------------") # Separador

for i in range(1,11):
    print("{}x{}={}".format(3,i,i*3)) # Imprimeix la taula del 3 de l'un al deu

print("--------------") # Separador, ARA FER UNA SÉRIE

y = 0
for n in range(1,16):
    y = y + (n**2+3) + (n-3)
print("La série sumari d'n per n=1 a 11 (n2+1) el resultat és: {}".format(y))

print("--------------") # Separador, ARA FER UNA SÉRIE

z = 0 # començ i no té valor = dona error. 
for n in range(1,46):
    z = z

print("--------------") # Separador, ARA FER UNA SÉRIE

sumatori = 0
for i in range(1,11):
    sumatori = sumatori + i
    print("El valor del sumatori és {}".format(sumatori))

print("--------------") # Separador, ARA FER UNA SÉRIE

# EXEMPLE 4
sumatori = 0
for i in range(2,14):
    sumatori = sumatori + (i+1)
print("El valor de sumatori és {}".format(sumatori))

print("--------------") # Separador, ARA FER UNA SÉRIE

# EXEMPLE 4
sumatori = 0
for i in range(2,14):
    sumatori = sumatori + (i+1)
    print("El valor de sumatori és {}".format(sumatori))