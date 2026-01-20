import numpy as np # importa/descarrega la llibreria numpy com np així podrem utilitzar el nombre pi
import time # importa/descarrega la llibreria time així podrem fer pauses durant el programa

# definim una funció com a calcul_arees la qual té com a paramentres les figures que poden ser altures o 
# bases de triangles en un diccionari dins d'una llista o una llista de radis, també un text que pot decidir 
# l'usuari o que per determinat és Càlculs: que apareix a l'inici de la funció, la funció retorna una llista
def calcul_arees(figura: list, tipus: str, text_inicial: str = "Càlculs:") -> list:
    """
    Docstring para calcul_arees
    
    :param figura: llista o diccionari dins d'una llista la qual introduirà l'usuari
    :type figura: list
    :param tipus: el tipus de calcul que s'ha de fer, l'escolleix l'usuari si vol triangles o cercles
    :type tipus: str
    :param text_inicial: string el qual pot decidir l'usuari o per defecte és "Càlcul:"
    :type text_inicial: str
    :return: retorna una llista, la llista d'àrees
    :rtype: list
    """

    # dona a la variable comptador el valor 1
    comptador = 1
    arees = [] # crea una llista buida
    # Ensenya per pantalla la variable string text_final
    print(text_inicial)
    # la variable temps és un float que val 1.5 segons serà el que s'aturarà el programa cada time.sleep
    temps = 1.5
    time.sleep(temps) # s'atura 1.5 segons
    
    # s'executa si la variable tipus és triangles o triangle
    if tipus == "triangles" or tipus == "triangle":
        # bucle for per determinar cada base i altura de cada triangle canviant al següent per cada itineració
        # els valor s'extreuen del diccionari que està dins la llista
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
            # li diu a l'usuari quan val l'àrea acabada de calcular
            print(f"El triangle {comptador} té una area de: {area} unitats\n")
            # filera de 30 guions per millorar l'estètica
            print("-" * 30)
            # li suma 1 a la variable comptador cada com que s'acaba el bucle for, 
            # valor del comptador = número del triangle
            comptador += 1
            time.sleep(temps) # s'atura 1.5 segons
    # si és un cercle, si la variable tipus no és ni triangle ni triangles    
    else:
        # bucle for per canviar el radi canviant al següent per cada itineració
        # els valor s'extreuen de la llista
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
            time.sleep(temps) # s'atura 1.5 segons

    # la funció retorna la llista d'àrees
    return arees

# la variable decisió té el valor d'una string en mínuscules que pot ser triangle, triangles, cercles o cercle
decisio = input("\nVols calcular l'àrea de triangles o cercles? ").lower()

# bucle infinit fins que hi hagui un break
while True:
    # s'executa quan l'usuari a escollit triangle/s
    if decisio == "triangles" or decisio == "triangle":
        triangles = [] # es crea una llista buida que es diu triangles
    
        while True:
            # s'executa infinitament fins que l'usuari introdueixi correctament les dades
            while True:
                try:
                    base = float(input("Introdueix el valor de la base del triangle: "))
                    altura = float(input(f"Introdueix el valor de l'altura del triangle amb base '{base}': "))
                    break
                # si no introdueix un número
                except ValueError:
                    print("\nHas d'introduir un número")
            # es crea un diccionari amb els valors que ha introduït l'usuari amb claus base i altura
            triangle = {
                "base": base,
                "altura": altura
            }
            # el diccionari acabat de crear s'afegueix a la llista triangles
            triangles.append(triangle)
            # es pregunta a l'usuari si vol continuar introduïnt dades
            continuar = input("\nVols afegir més triangles? (si/no): ").lower()
            # si diu qualsevol cosa que no sigui "si" ja sigui en majúscula o minúscula surt del últim bucle
            if continuar != "si":
                break
        # li diu a l'usuari les dades que té el programa sobre els triangles
        print("\nTotal de dades sobre els triangles:")
        print(triangles)
        # deixa veure a l'usuari les dades fins que premi enter
        input("Prem enter per seguir: ")

        # fa que la variable llista_arees cridi a la funció la variable figura com a la variable 
        # triangles, tipus com a decisio, text_inicial com "Aquí tens les dades dels triangles"
        llista_arees = calcul_arees(triangles, decisio, "\nAquí tens les dades dels triangles")
        break # surt de bucle

    # s'executa quan l'usuari a escollit cercle/s
    elif decisio == "cercles" or decisio == "cercle":
        cercles = [] # es crea una llista buida que es diu cercles
    
        while True:
            # s'executa infinitament fins que l'usuari introdueixi correctament les dades
            while True:
                try:
                    radi = float(input("Introdueix el valor del radi del cercle: "))
                    break
                # si no introdueix un número
                except ValueError:
                    print("\nHas d'introduir un número")
            # la variable radi acabat d'introduït per l'usuari s'afegueix a la llista cercles
            cercles.append(radi)
            # es pregunta a l'usuari si vol continuar introduint dades
            continuar = input("\nVols afegir més cercles? (si/no): ").lower()
            # si diu qualsevol cosa que no sigui "si" ja sigui en majúscula o minúscula surt del últim bucle
            if continuar != "si":
                break
        # li diu a l'usuari les dades que té el programa sobre els cercles
        print("\nTotal de dades sobre els cercles:")
        print(cercles)
        # deixa veure a l'usuari les dades fins que premi enter
        input("Prem enter per seguir: ")
        # fa que la variable llista_arees cridi a la funció la variable figura com a la variable 
        # cercles, tipus com a decisio, text_inicial com "Aquí tens les dades dels cercles"
        llista_arees = calcul_arees(cercles, decisio, "\nAquí tens les dades dels cercles")
        break
    # s'executa quan l'usuari no a escollit ni triangle/s ni cercle/s
    else:
        # li diu a l'usuari que ha d'escollir entre triangle i cercles
        print("Has de dir si vols calcular triangles o cercles")
        # torna a fer la pregunta
        decisio = input("\nVols calcular l'àrea de triangles o cercles? ").lower()
        continue # torna a l'inici del bucle
# Avisa a l'usuari que el programa a acabat
print("--- Programa finalitzat ---")
