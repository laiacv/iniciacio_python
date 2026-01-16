import numpy as np # importa/descarrega la llibreria numpy com np així podrem utilitzar el nombre pi

radis = [3, 2, 7, 15] # crea una llista amb els radis de cada cercle

# definim una funció per calcular les àrees dels cercles la qual té com a paràmetres una 
# llista que es dirà radis i un string que es dirà text_final amb valor predeterminat: 
# acabat, dins de la funció. I la funció ha de retornar una llista
def calcul_area_cercles(radis: list, text_final: str = "acabat") -> list:

    # dona a la variable comptador el valor 1
    comptador = 1
    arees = [] # crea una llista buida

    # bucle for el qual va itinerant la variable radis, dels paràmetres de la funció
    for radi in radis:

        # li recorda a l'usuari quin cercle és amb la variable comptador i el seu radi
        print(f"\nEl cercle {comptador} té un radi de: {radi} unitats")

        # Calculem l'àrea del cercle
        area = round((np.pi) * (radi)**2, 2)
        
        # guardem el valor de l'àrea que acabem de calcular
        arees.append(area)
       
        # li diu a l'usuari quina és l'àrea del cercle respecte quin cercle és
        print(f"Per tant, el cercle {comptador} té una àrea de: {area:.2f} unitats quadrades\n")

        # filera de 30 guions per millorar l'estètica
        print("-" * 30)

        # li suma 1 a la variable comptador cada com que s'acaba el bucle for, 
        # valor del comptador = número del cercle
        comptador += 1

    # Ensenya per pantalla la variable string text_final
    print(text_final)
    # la funció retorna la llista d'àrees
    return arees

# la variable llista_arees el que fa es cridar la funció calcul_area_cercles, dient que la 
# llista de radis que hi ha fora la funció serà la mateixa a la variable radis que hi ha dins,
# i li dona el valor: hem acabat, a la variable de text_final
llista_arees = calcul_area_cercles(radis, "\nHem acabat")

# mostra per pantalla/executa la variable llista_arees, la qual es la que crida la funció
print(llista_arees)

# li diu a l'usuari que s'ha acabat el programa
print("\n--- Programa finalitzat ---")