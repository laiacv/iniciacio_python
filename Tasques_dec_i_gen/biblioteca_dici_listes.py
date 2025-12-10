# Importem la funció time per poder-la utilitzar més endavant
import time
# Creem una llista buida
biblioteca = []
# Li assignem el valor 0 a la variable opcio al iniciar el programa
opcio = 0

# Un bucle que funciona per sempre
while True:

    # Aquest text sortirà avans de que l'usuari escolleixi el que vol fer
    print("\n=== GESTOR DE BIBLIOTECA v1.0 ===")

    print("\nSELECCIONA UNA OPCIÓ:")
    print("[1] Afegir un nou llibre\n[2] Veure tots els llibres\n[3] Sortir del programa")

    # L'usuari esolleix l'opció
    opcio = int(input("\n> La teva opció: "))

    # S'executa si l'usuari escolleix l'opció 1
    if opcio == 1:

        # Demana l'informació sobre el llibre a l'usuari
        print("--- AFEGINT NOU LLIBRE ---")
        titol = input("Nom del llibre: ")
        autor = input("Autor: ")

        # Prova fins al break
        while True:
            
            # Prova el que està dins del try, si funciona ho executa si no diu quin és l'error
            try:
                any = int(input("Any de publicació: ")) #mil nou-cents...
                break
            except ValueError:
                print("ERROR: L'any ha de ser un número enter (ex: 1990). Torna-ho a provar.")

        # Crea un diccionari el qual li afegueix la informació avans proporcionada per l'usuari
        Info_llibre = {
            "titol": titol, #El Senyor dels Anells
            "autor": autor, #J.R.R. Tolkien
            "any": any #1954
        }

        # Afegueix el diccionari anterior a la llista, per guardar la informació i poder mostrar-la després
        biblioteca.append(Info_llibre)

        # Ve de la funció time i sutilitza per fer pauses el programa espera el temps en segons que està entre parentesi, en aquest cas 2 segons
        time.sleep(2)

        # Li diu a l'usuari que el llibre s'ha afeguit correctament
        print("\n✅ Llibre afegit correctament!")
        print("----------------------------------------")

        time.sleep(1)

    # S'executa si l'usuari escolleix l'opció 2
    elif opcio == 2:

        # el programa calcula quants llibres hi ha a la biblioteca contant la longuitud que té la llista
        print(f"--- LLISTAT DE LLIBRES ({len(biblioteca)} llibres trobats) ---")

        # S'executa si la llista està buida
        if len(biblioteca) == 0:
            print("No hi ha llibres a la biblioteca")
            
        # S'executa si la llista no està buida
        else:
            valor = 1 # S'assigna el valor 1 a la variable valor
            # Es un bucle per ordenar els llibre de la llista
            for llibre in biblioteca:
                valor1 = llibre["titol"]
                valor2 = llibre["autor"]
                valor3 = llibre["any"]
                # Ensenya a l'usuari nombre del llibre 'Nom Llibre' escrit per l'Autor (any)
                print(f"{valor}. '{valor1}' escrit per {valor2} ({valor3})")
                # li suma 1 a la variable valor per després es vagui ben ordenat en una llista 1.,2.,3. ...
                valor += 1

        # l'usuari ha de prémer l'enter per continuar (no importa si escriu alguna cosa més)
        input("Pren enter per continuar... ")
        print("\n----------------------------------------")

    # S'executa si l'usuari escolleix l'opció 3
    elif opcio == 3:
        print("\nGuardant dades...") # Diu a l'usuari que s'està guardant les dades
        time.sleep(2.5)
        print("Adéu! Fins la propera.") # S'acomiada de l'usuari
        break # Treca/Acaba el bucle

    # Si l'usuari no posa com a opció 1, 2 o 3 i li diu que ho torni a intentar
    else:
        print("\nOpció no vàlida. Torna-ho a provar.\n")