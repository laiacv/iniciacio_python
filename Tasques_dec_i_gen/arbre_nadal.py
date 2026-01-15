while True:
    try:
        altura_arbre = int(input("Digues l'altura que vols per l'arbre: "))
        break
    except ValueError:
        print("Ha de ser un nombre enter")

for i in range(altura_arbre):
    espais = (altura_arbre - 1) - i
    print(" " * espais + "*" * (2 * i + 1))