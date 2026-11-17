def menu():
    opcio = 0
    while opcio < 1 or opcio > 4:
        print("""
        Menú principal:
        1. Suma
        2. Resta
        3. Multiplicació
        4. Divisió
        """)
        opcio = int(input("Indiqui el número de la funció que vol executar: "))
    return opcio

# Programa principal
# En comptes de fer molts elif, podem emprar match i queda millor

op =menu()
match(op):
    case 1:
        print("Operacions de suma \n ")
        x = int(input("Indiqui el primer número: "))
        y = int(input("Indiqui el primer número: "))
        print("El resultat de {} + {} és {}".format(x, y, x+y))
    case 2:
        print("Operacions de resta")
        x = int(input("Indiqui el primer número: "))
        y = int(input("Indiqui el primer número: "))
        print("El resultat de {} - {} és {}".format(x, y, x-y))
    case 3:
        print("Operacions de multiplicació")
        x = int(input("Indiqui el primer número: "))
        y = int(input("Indiqui el primer número: "))
        print("El resultat de {} * {} és {}".format(x, y, x*y))
    case 4:
        print("Operacions de divisió")
        x = int(input("Indiqui el primer número: "))
        y = int(input("Indiqui el primer número: "))
        print("El resultat de {} / {} és {}".format(x, y, x/y))
    case _: # Barra baixa (underscore) vol dir qualsevol altre cas
        print("En qualsevol altre cas")
