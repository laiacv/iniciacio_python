# base1 = 2
# base2 = 4
# base3 = 6

# altura1 = 1
# altura2 = 5
# altura3 = 15

bases = [2, 4, 6]
altures = [1, 5, 15]
comptador = 1
# area1 = base1 * altura1
# area2 = base2 * altura2
# area3 = base3 * altura3

# print(f"l'àrea del triangle 1 és: {area1}")
# print(f"l'àrea del triangle 2 és: {area2}")
# print(f"l'àrea del triangle 3 és: {area3}")
for base, altura in zip(bases, altures):
    print(f"El triangle {comptador} té una base de: {base} unitats")
    print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

    # Calculem l'àrea del triangle
    area = 1/2 * (base * altura)

    print(f"Per tant, el triangle {comptador} té una àrea de: {area} unitats quadrades\n")

    comptador += 1      


# for character in "estem iterant l'string":
#     print(character)

# llista = [1, 2, "string", 4.2, True]

# for item in llista:
#     print(llista)
#     print(item)


# Imaginem que tenim una llista on cada element és un diccionari
triangles = [
    {"base": 10, "altura": 5},
    {"base": 8, "altura": 4},
    {"base": 12, "altura": 7}
]

comptador = 1

# Iterem directament sobre la llista de diccionaris
for triangle in triangles:
    base = triangle["base"]
    altura = triangle["altura"]
    
    print(f"El triangle {comptador} té una base de: {base} unitats")
    print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

    # Calculem l'àrea del triangle
    area = 1/2 * (base * altura)

    print(f"Per tant, el triangle {comptador} té una àrea de: {area} unitats quadrades\n")
    print("-" * 30) # Una línia separadora per claredat
    
    comptador += 1


"""
DEFINIREM UNA FUNCIÓ
"""
# Imaginem que tenim una llista on cada element és un diccionari
triangles = [
    {"base": 10, "altura": 5},
    {"base": 8, "altura": 4},
    {"base": 12, "altura": 7}
]

def calcul_area_triangle(triangles: list, text_final: str) -> list:
    """
    Aquesta funció calcula les àrees dels triangles del diccionari i la 
    retorna en una llista 
    
    :param triangles: Una llista que conté diccionaris dins amb les dades de cada triangle, les seves claus han de ser "base" i "altura"
    :type triangles: list
    :param text_final: Text que es mostra per pantalla en finalitzat
    :type text_final: str
    :return: Àrees dels triangles del diccionari en una llista
    :rtype: list
    """

    arees = [] # llista

    comptador = 1

    # Iterem directament sobre la llista de diccionaris
    for triangle in triangles:
        base = triangle["base"]
        altura = triangle["altura"]
        
        print(f"El triangle {comptador} té una base de: {base} unitats")
        print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

        # Calculem l'àrea del triangle
        area = 1/2 * (base * altura)

        arees.append(area)

        print(f"Per tant, el triangle {comptador} té una àrea de: {area} unitats quadrades\n")
        print("-" * 30) # Una línia separadora per claredat
        
        comptador += 1

    print(text_final)

    return arees

llista_arees = calcul_area_triangle(triangles, "hem acabat")

print(llista_arees)

print("--- programa finalitzat ---")