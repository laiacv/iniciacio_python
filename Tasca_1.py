a_0 = float(7.5)
a_1 = int(3)
a_2 = int(4)
a_3 = int(2)

print(f"De l'equació: ({a_3}x³+{a_2}x²-{a_1}x)/{a_0} amb dos intents per intentar determinar una de les arrels de l'equació")

x = int(input("Intenta primer amb un decímal: "))
x_1 = x
x_2 = x*x
x_3 = x*x*x

opera = print(float((a_3*x_3+a_2*x_2-a_1*x_1)/{a_0}))

if opera == 0:
    boolea_1 = bool(True)
    print(f"Molt bé has descobert una de les arrels")

else:
    boolea_1 = bool(False)
    print(f"Làstima, tens un altre intent")

x1 = int(input("Ara prova amb un enter: "))
x1_1 = x1
x1_2 = x1*x1
x1_3 = x1*x1*x1

opera = print(float((a_3*x1_3+a_2*x1_2-a_1*x1_1)/{a_0}))

if opera == 0:
    boolea_2 = bool(True)
    print(f"Molt bé has descobert una de les arrels, en el segon intent")

elif boolea_1 == True and opera == 0:
    boolea_2 = bool(True)
    print("Molt bé has trobat dues arrels")

else:
    boolea_2 = bool(False)
    print(f"Làstima, t'ha quedat sense intents")

