
bases = [2, 4, 6]
altures = [1, 5, 15]

def calcul_area_triangle(bases: list, altures: list, text_final: str = "acabat") -> list:

    comptador = 1
    arees = [] # llista buida
    
    for base, altura in zip(bases, altures):

        print(f"\nEl triangle {comptador} té una base de: {base} unitats")
        print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

        # Calculem l'àrea del triangle
        area = 1/2 * (base * altura)

        arees.append(area)
       
        print(f"Per tant, el triangle {comptador} té una àrea de: {area} unitats quadrades")

        print("-" * 30)

        comptador += 1

    print(text_final)
    return arees


llista_arees = calcul_area_triangle(bases, altures, "hem acabat")

print(llista_arees)

print("--- Programa finalitzat ---")