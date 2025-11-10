# S'assigna les variables dels coeficients
a_0 = 1 # és una variable tipus float
a_1 = 0.5
a_2 = -2.5
a_3 = 1

# Se li mostra l'equació a l'usuari
print("JOC DE TROBAR LES ARRELS \n Busca les arrels")
print(f"De l'equació: ({a_3}x³+{a_2}x²+{a_1}x)+{a_0} amb dos intents per intentar determinar una de les arrels de l'equació")

# Se li dona la primera oportunitat al l'usuari, ha de provar amb un decímal
x = float(input("Intenta primer amb un decímal: "))
x_1 = x
x_2 = x*x
x_3 = x*x*x

# Mostra el resultat de l'equació amb el número que diu l'usuari
opera1 = print(float(a_3*x_3+a_2*x_2+a_1*x_1+a_0))

# Si l'operació es igual a 0
if opera1 == 0:
    boolea_1 = bool(True)
    print(f"Molt bé has descobert una de les arrels")

# Si l'operació es no igual a 0
else:
    boolea_1 = bool(False)
    print(f"Làstima, tens un altre intent")

# Se li dona la segona oportunitat al l'usuari, ha de provar amb un enter
x1 = int(input("Ara prova amb un enter: "))
x1_1 = x1
x1_2 = x1*x1
x1_3 = x1*x1*x1

# Mostra el resultat de l'equació amb el segon número que diu l'usuari
opera2 = print(float((a_3*x1_3+a_2*x1_2-a_1*x1_1+a_0)))

# Si l'operació 2 es igual a 0, però la primera no ha donat 0
if opera2 == 0 and opera1 != 0:
    boolea_2 = bool(True)
    print(f"Molt bé has descobert una de les arrels, en el segon intent")

# Si l'operació 2 es igual a 0 i la primera també ha donat 0
elif boolea_1 == True and opera2 == 0:
    boolea_2 = bool(True)
    print("Molt bé has trobat dues arrels")

# Si l'operació es no igual a 0
else:
    boolea_2 = bool(False)
    print(f"Làstima, t'ha quedat sense intents")

# Es mostra per pantalla
print("S'ha acabat el programa <3")

"""
Valora que tant bé ho ha fet l'usuari a partir de 
quantes arrels ha resolt
"""
if boolea_1 == True and boolea_2 == True:
    print("Molt bé ho has fet perfecte ;)")

if boolea_1 == True and boolea_2 == False:
    print("Ho has fet bé :)")

if boolea_1 == False and boolea_2 == True:
    print("Ho has fet bé :)")

if boolea_1 == False and boolea_2 == False:
    print("No has aconseguit trobar les arrels :(")

"""
x=1 (enter)
x=-0,5 (decimal)
x=2 (enter)
"""