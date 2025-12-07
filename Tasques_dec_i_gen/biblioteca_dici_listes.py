import time
biblioteca = []
op = 0

while True:

    print("\n=== GESTOR DE BIBLIOTECA v1.0 ===")

    print("\nSELECCIONA UNA OPCIÓ:")
    print("[1] Afegir un nou llibre\n[2] Veure tots els llibres\n[3] Sortir del programa")

    op = int(input("\n> La teva opció: "))

    if op == 1:
        print("--- AFEGINT NOU LLIBRE ---")
        titol = input("Nom del llibre: ")
        autor = input("Autor: ")
        while True:
            try:
                any = int(input("Any de publicació: ")) #mil nou-cents...
                break
            except ValueError:
                print("ERROR: L'any ha de ser un número enter (ex: 1990). Torna-ho a provar.")

        Info_llibre = {
            "titol": titol, #El Senyor dels Anells
            "autor": autor, #J.R.R. Tolkien
            "any": any #1954
        }

        biblioteca.append(Info_llibre)

        time.sleep(2)

        print("\n✅ Llibre afegit correctament!")
        print("----------------------------------------")

        time.sleep(1)

    elif op == 2:

        print(f"--- LLISTAT DE LLIBRES ({len(biblioteca)} llibres trobats) ---")

        if len(biblioteca) == 0:
            print("No hi ha llibres a la biblioteca")
            

        else:
            num = 1
            for llibre in biblioteca:
                valor1 = llibre["titol"]
                valor2 = llibre["autor"]
                valor3 = llibre["any"]
                print(f"{num}. '{valor1}' escrit per {valor2} ({valor3})")
                num += 1
        print("\n----------------------------------------")

    elif op == 3:
        print("\nGuardant dades...")
        time.sleep(2.5)
        print("Adéu! Fins la propera.")
        break

    else:
        print("\nOpció no vàlida. Torna-ho a provar.\n")