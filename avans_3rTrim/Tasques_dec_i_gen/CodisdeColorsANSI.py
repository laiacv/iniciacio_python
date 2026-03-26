# Codi ANSI per treure/reiniciar color de text
reset = "\033[0m"
# Codi ANSI  de color verd per l'arbre
verd = "\033[92m"
# Codi ANSI  de color marró pel tronc de l'arbre
marro = "\033[33m"
# Codi ANSI  de color groc per l'estrella de l'arbre
groc = "\033[93m"

# Bucle que es repeteix per sempre fins que es trobi amb un break
while True:
    # intenta fer el que hi ha dins del try i si no funciona fa el que hi ha 
    # dins del except
    try:
        # Demana a l'usuari l'altura de l'arbre
        altura_arbre = int(input("\nDigues l'altura que vols per l'arbre: "))
        # Multipliquem per 2, ja que cada filera d'asteriscs té 2 més que 
        # l'anterior, es resta 1 perquè la punta de l'arbre tingui un sol 
        # asterisc
        amplada_max = 2 * altura_arbre - 1
        break # Per sortir del bucle
    except ValueError: # S'executa si no és un nombre enter
        print("Ha de ser un nombre enter") 
# Pregunta a l'usuari si vol que l'arbre tingui una estrella
estrella = (input("Vols que tingui una estrella? (Només amb “sí” es posa" \
" l’estrella) ")).lower()

# si respon si, ja sigui en majúscules o minúscules s'executarà:
if estrella == "si":
    # calcula on ha de d'estar col·locada l'estrella:
    # el -1 es per l'amplada de l'estrella. I per últim 
    # la divisió entera de 2 es per que l'estrella estgui al mitg de l'arbre
    amplada_estrella = ((amplada_max - 1) // 2)
    # dibuixa l'estrella groga
    print(groc + " " * amplada_estrella + "★" + reset)
    # bucle for per escriure els asteriscs necessaris
    for i in range(altura_arbre):
        # calcul pels espais que va disminuint a cada línia
        espais = (altura_arbre - 1) - i
        # calcul per els esteriscos necesaris a cada línia que va augmentant
        estrelles = "*" * (2 * i + 1)
        # fa cada línia d'asteriscs de color verd per l'arbre
        print(verd + " " * espais + estrelles + reset)

# si no respon si s'executarà (les explicacions no les mateixes):
else:
    for i in range(altura_arbre):
        espais = (altura_arbre - 1) - i
        estrelles = "*" * (2 * i + 1)
        print(verd + " " * espais + estrelles + reset)
        
# Calcula d'amplada del tronc 
amplada_tronc = (((2 * altura_arbre - 1) - 3) // 2)
print(marro + " " * amplada_tronc + "|||" + reset)