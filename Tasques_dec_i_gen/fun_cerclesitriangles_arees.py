import numpy as np # importa/descarrega la llibreria numpy com np així podrem utilitzar el nombre pi
import time

def calcul_arees(figura: list, tipus: str, text_inicial: str = "acabat") -> list:

    # dona a la variable comptador el valor 1
    comptador = 1
    arees = [] # crea una llista buida
    # Ensenya per pantalla la variable string text_final
    print(text_inicial)
    temps = 1.5
    time.sleep(temps)
    
    if tipus == "triangles" or tipus == "triangle":
        for triangle in figura:
            base = triangle["base"]
            altura = triangle["altura"]

            # li recorda a l'usuari quin triangle és amb la variable comptador i diu la base i l'altura
            print(f"\nEl triangle {comptador} té una base de: {base} unitats")
            print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

            # Calculem l'àrea del triangle
            area = round(1/2 * (base * altura), 2)
            # guardem el valor de l'àrea que acabem de calcular
            arees.append(area)
            print(f"El triangle {comptador} té una area de: {area} unitats\n")
            # filera de 30 guions per millorar l'estètica
            print("-" * 30)
            # li suma 1 a la variable comptador cada com que s'acaba el bucle for, 
            # valor del comptador = número del triangle
            comptador += 1
            time.sleep(temps)
        
    else:
        for radi in figura:
            # Calculem l'àrea del cercle
            area = round((np.pi) * (radi)**2, 2)
            # guardem el valor de l'àrea que acabem de calcular
            arees.append(area)
            # li recorda a l'usuari quin cercle és amb la variable comptador i diu el radi que té
            print(f"\nEl cercle {comptador} té un radi de: {radi} unitats")
        
            # li diu a l'usuari quina és l'àrea del triangle respecte quin triangle és
            print(f"Per tant, el cercle {comptador} té una àrea de: {area} unitats quadrades")

            # filera de 30 guions per millorar l'estètica
            print("-" * 30)
            # li suma 1 a la variable comptador cada com que s'acaba el bucle for, 
            # valor del comptador = número del triangle
            comptador += 1
            time.sleep(temps)

    # la funció retorna la llista d'àrees
    return arees


decisio = input("\nVols calcular l'àrea de triangles o cercles? ").lower()

while True:
    if decisio == "triangles" or decisio == "triangle":
        triangles = []
    
        while True:
            while True:
                try:
                    base = float(input("Introdueix el valor de la base del triangle: "))
                    altura = float(input(f"Introdueix el valor de l'altura del triangle amb base '{base}': "))
                    break
                except ValueError:
                    print("\nHas d'introduir un número")
            triangle = {
                "base": base,
                "altura": altura
            }
            triangles.append(triangle)
            
            continuar = input("\nVols afegir més triangles? (si/no): ").lower()
            if continuar != "si":
                break
    
        print("\nTotal de dades sobre els triangles:")
        print(triangles)
        input("Prem enter per seguir: ")

        llista_arees = calcul_arees(triangles, decisio, "\nAquí tens les dades dels triangles")
        break

    elif decisio == "cercles" or decisio == "cercle":
        cercles = []
    
        while True:
            while True:
                try:
                    radi = float(input("Introdueix el valor del radi del cercle: "))
                    break
                except ValueError:
                    print("\nHas d'introduir un número")
    
            cercles.append(radi)
            
            continuar = input("\nVols afegir més cercles? (si/no): ").lower()
            if continuar != "si":
                break
    
        print("\nTotal de dades sobre els cercles:")
        print(cercles)
        input("Prem enter per seguir: ")
    
        llista_arees = calcul_arees(cercles, decisio, "\nAquí tens les dades dels cercles")
        break

    else:
        print("Has de dir si vols calcular triangles o cercles")
        decisio = input("\nVols calcular l'àrea de triangles o cercles? ").lower()
        continue
print("--- Programa finalitzat ---")
