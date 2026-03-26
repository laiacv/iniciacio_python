
bases = [2, 4, 6] # crea una llista amb les bases de cada triangle
altures = [1, 5, 15] # crea una llista amb les altures de cada triangle

# definim una funció per calcular les àrees dels triangles la qual té com a paràmetres una 
# llista que es dirà bases, una altre que es dirà altures i un string que es dirà text_final 
# amb valor predeterminat: acabat, dins de la funció. I la funció ha de retornar una llista
def calcul_area_triangle(bases: list, altures: list, text_final: str = "acabat") -> list:
    """
    Docstring para calcul_area_triangle
    
    :param bases: llista que introdueix que es fa fora de la funció de les bases dels triangles
    :type bases: list
    :param altures: llista que introdueix que es fa fora de la funció de les altures dels triangles
    :type altures: list
    :param text_final: string el qual pot decidir l'usuari o per defecte és "acabat"
    :type text_final: str
    :return: retorna una llista, la llista d'àrees
    :rtype: list
    """

    # dona a la variable comptador el valor 1
    comptador = 1
    arees = [] # crea una llista buida
    
    # bucle for el qual va itinerant les variables base i altura, dels paràmetres de la funció
    # (bases i altures)
    for base, altura in zip(bases, altures):

        # li recorda a l'usuari quin triangle és amb la variable comptador i diu la base i l'altura
        print(f"\nEl triangle {comptador} té una base de: {base} unitats")
        print(f"El triangle {comptador} té una altura de: {altura} unitats\n")

        # Calculem l'àrea del triangle
        area = 1/2 * (base * altura)

        # guardem el valor de l'àrea que acabem de calcular
        arees.append(area)
        
        # li diu a l'usuari quina és l'àrea del triangle respecte quin triangle és
        print(f"Per tant, el triangle {comptador} té una àrea de: {area} unitats quadrades")

        # filera de 30 guions per millorar l'estètica
        print("-" * 30)
        # li suma 1 a la variable comptador cada com que s'acaba el bucle for, 
        # valor del comptador = número del triangle
        comptador += 1

    # Ensenya per pantalla la variable string text_final
    print(text_final)
    # la funció retorna la llista d'àrees
    return arees

# la variable llista_arees el que fa es cridar la funció calcul_area_triangles, dient que la 
# llista de bases que hi ha fora la funció serà la mateixa a la variable bases que hi ha dins,
# al igual amb la variable altures i li dona el valor: hem acabat, a la variable de text_final
llista_arees = calcul_area_triangle(bases, altures, "hem acabat")

# mostra per pantalla/executa la variable llista_arees, la qual es la que crida la funció
print(llista_arees)

# li diu a l'usuari que s'ha acabat el programa
print("--- Programa finalitzat ---")