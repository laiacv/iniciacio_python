print("Hola mòn") 

x = input("Numero del 1 al 10: ")
   
print(f"{float(x)-2}, es el resultat del teu nombre -2")


import random

# Això és un comentari
"""
Això és un bloc de comentari

Puc escriure a totes les línies.
"""

"""
TIPUS DE VARIABLES:
* Nombres: Enters (int) i Decimals (float)
* Text: Cadena de caràcters (str)
* Booleans: Veritat o fals (bool)

Anem a declarar les variables:
Variables: en minúscula
CONSTANTS: en majúscula
"""
enter_1 = 17 # És una variable entera
float_1 = 3.

string_1 = "Això és un string"
string_2 = 'Un altre string'

boolea_1 = True
boolea_2 = False

print("Vull imprimir aquest missatge per pantalla")
print(string_1)
print(string_2)

print(type(enter_1))
print(type(float_1))
print(type(string_1))
print(type(boolea_1))
print(type(print))
print(random.random)

print(f"Això és un enter: {enter_1}, això és un float: {float_1}")

# Operadors aritmètics
operacio = enter_1 - float_1 + 4
print(f"L'operació té com a resultat: {operacio} i és de tipus: {type(operacio)}")

operacio_complexa = enter_1**5 + float_1/5 - 3*(enter_1 % 4)
print(operacio_complexa)

print(1%5, 2%5, 3%5, 4%5, 5%5, 6%5)

enter_2 = input("Introdueix un nombre enter: ")

print(enter_2)




# CTRL + ç (comento el bloc de codi)

# # import random
# import numpy as np
# import random
# y = random.choices()

# # print(y)
