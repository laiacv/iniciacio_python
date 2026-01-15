import numpy as np

radis = [3, 2, 7, 15]

def calcul_area_cercles(radis: list, text_final: str = "acabat") -> list:

    comptador = 1
    arees = [] # llista buida
    
    for radi in radis:

        print(f"\nEl cercle {comptador} té un radi de: {radi} unitats")

        # Calculem l'àrea del triangle
        area = (np.py) * (radi)**2

        arees.append(area)
       
        print(f"Per tant, el cercle {comptador} té una àrea de: {area} unitats quadrades")

        print("-" * 30)

        comptador += 1

    print(text_final)
    return arees


llista_arees = calcul_area_cercles(radis, "hem acabat")

print(llista_arees)

print("--- Programa finalitzat ---")