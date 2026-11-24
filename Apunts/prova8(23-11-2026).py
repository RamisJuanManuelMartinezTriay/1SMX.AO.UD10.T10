# llista buida, cinc elements, posar a la llista, concatenar els elements amb un print

l = list()
for i in range(5):
    l.append(input("Escriu un número: "))
elementsconcatenats = ", ".join(l) # Concatenar. Han de ser strings (no afegir int() antes d'input)
print(elementsconcatenats)