# 2.2 Tipus de dades https://docs.google.com/document/d/1K-Z_EUgv0fFQgm48rKAp5p0ov-dfKQ1GB9Em0z57CyA/edit
# Bàsics (enters, reals, booleans, cadenes)
# PER DEFECTE ES PASSEN PER VALOR -> QUAN ACABA LA FUNCIÓ NO CANVIA EL VALOR. PER REFERÈNCIA PASSES UNA POSICIÓ DE MEMÒRIA QUE LA FUNCIÓ POT TOCAR (MODIFICAR) DIRECTAMENT. HI HA MANERA QUE SEMPRE ES PASSI COM A REFERÈNCIA UN VALOR O QUE UNA REFERÈNCIA SIGUI COM UN VALOR I NO ES PUGUI TOCAR.
# ÉS PUNYETERO LO DE PASSAR COM A VALOR / REFERÈNCIA I QUÈ ÉS UN VALOR O UNA REFERÈNCIA PER DEFECTE. BÀSIC -> VALOR -> INMUTABLE
nombre = 3 # Nombres enters

real = 3.124141412

cadena = "Hola, Ramis!" # string, per a text

bool = True #booleà és true o false
print(cadena)


# Tipus compost, més complexes, els hi definirem

llista = [3, [4, 5], (1, 2, 3), "Hola"] # valors heterogènics, no tenen perquè ser homogènics. VA EN CLAUDÀTORS

tupla = (1, 2, 3)

rang = range(1, 11, 2) # DE L'1 AL 10 DE DOS EN DOS

diccionari = {"nom":"Joan","cognoms":"Ramis","edat":28, "Telèfon":"971360133"}

# Si Python fuera compilado habría que mantener siempre el mismo tipo de variable

# VALOR VS. REFERÈNCIA APRENDRE LA DIFERÈNCIA 
# qualsevol variable de tipus bàsica és inmutable una vegada definida. NO ÉS AIXÍ AMB TIPUS COMPOST
# pot ser així a una variable tipus compost
exempletipuscompost = [3, 4]

exempletipuscompost[0] =  "Hola món!" # es reemplaça la referència
print(exempletipuscompost)

def canvi(x): # açò és una funció
    x= x +1
    print(x)
def canvireferencia(llista):
    if len(llista)>0:
        llista[0]="Guapo"
    else:
        print("No té cap valor")
# Programa principal
nombre = 3
canvi(nombre)
print(nombre)

# AÇÒ REALMENT SÓN APUNTS, ELS DELS PROFESSOR ESTÀN A UNA PUBLICACIÓ DEL CLASSROOM https://classroom.google.com/c/ODY2ODc1MTI2ODI3/p/ODk5OTc0OTA2MDcx/details
# JO ELS HE COPIAT DE MANERA QUE HO ENTENC

marc =  3 # nombre enter
canvi(marc) # vull que se modifiqui marc, que per defecte és bàsic
exemple12341252 = "Hola" # exemple cadena caràcters, és inmutable

exempletalcualsimprimira =  """Hola
    1. Com va?
    2. Esteu bé?
    """
print(exempletalcualsimprimira)

primeracadena = "Hola, "
segonacadena = "Ramis"
# Podem concatenar (concatenate) (sumar) cadenes
print(primeracadena+segonacadena)

# Si hi ha cadena amb valor "3" i altre "4" i les sumam el resultat és "34" perquè és text
print(primeracadena*3) # imprimirà Hola, Hola, Hola,

salutacio = "Hola, Ramis"
print(salutacio[-5::-1]) # a l'inrevès del primer caràcter fins al ?
print(salutacio[::]) # a l'inrevès

# Llegir una paraula i comprovar si és un palíndrom
laparaula = input("Escriu la paraula per veure si és un palíndrom: ")
if laparaula == laparaula[::-1]:
    print("És un palíndrom")
else:
    print("No és un palíndrom")

# Què fa aquest troç de codi?
for c in laparaula:
    print(c)    # imprimeix p
                #           e
                #           p

# Quantes a té la paraula introduïda
cuantas = input("Introduce la palabra: ")
sum_a=0
for c in cuantas:
    if c=="a":
        sum_a=sum_a+1
print("La paraula {} té {}-a".format(cuantas, str(sum_a)))