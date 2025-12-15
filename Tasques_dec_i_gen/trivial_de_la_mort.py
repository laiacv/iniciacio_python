import time 

banc_de_preguntes = [
    {
        "enunciat": "Quin és el planeta més gran del Sistema Solar?",
        "opcions": ["1. Mart", "2. Júpiter", "3. Terra"],
        "correcta": 2
    },
    {
        "enunciat": "Quant és 2 + 2 x 2?",
        "opcions": ["1. 6", "2. 8", "3. 4"],
        "correcta": 1
    },
    {
        "enunciat": "Quina extensió tenen els fitxers de Python?",
        "opcions": ["1. .pyt", "2. .pt", "3. .py"],
        "correcta": 3
    }
]

# Variables d'Estat del joc
vides = 3
punts = 0
index_pregunta = 0 # Per saber per quina pregunta anem (0, 1, 2...)

# presenta el joc a l'usuari i li diu quantes vides té
print("\n😈 BENVINGUT AL TRIVIAL DE LA MORT 😈")
time.sleep(0.5)
print(f"Comences amb {vides} vides. Bona sort...\n")
time.sleep(1)


# El joc continuarà mentre quedin vides (> 0) I l'índex sigui menor que el total de preguntes.
while vides > 0 and index_pregunta < len(banc_de_preguntes):

    # a la variable 'pregunta_actual' se li dona el valor del diccionari que toca segons l'índex.
    pregunta_actual = banc_de_preguntes[index_pregunta]

    # mostra a l'usuari l'enunciat de la pregunta i les opcions possibles.
    print(f"Pregunta: {pregunta_actual["enunciat"]}")
    
    for resposta in pregunta_actual["opcions"]:
        print("     " + resposta)
    
    # Assegura que l'usuari introdueix un NÚMERO enter i que sigui una de les 3 opcions.
    while True:
        try:
            resposta_usuari = int(input("Respon la pregunta: "))
            if 1 <= resposta_usuari <= 3:
                break
            else:
                print("Posa una de les 3 opcions. Torna-ho a provar")
        except ValueError:
            print("Has d'introduir un número enter. Torna-ho a provar")

    # determina si la resposta de l'usuari és la 'correcta' del diccionari
    # - Si encerta: Se'l felicita i se li sumen 10 punts
    # - Si falla: Se'l resta 1 vida i se li diu quantes li queden.
    if pregunta_actual["correcta"] == resposta_usuari:
        print("Molt bé, tens 10 punts més!!!!!!!!!!!!!!") #14
        punts += 10
        print(f"Tens {punts} punts en total")
        time.sleep(2)
    else:
        vides -= 1
        print(f"T'has equivocat. :( Et queden {vides} vides")
        time.sleep(2)

    # Suma líndex de la pregunta en +1 per passar a la següent pregunta quan torni a fer el bucle
    index_pregunta += 1
    print("-" * 30) # Separador estètic entre preguntes

time.sleep(1.5)
# Li proporciona a l'usuar un resum de la partida
# - Si té 0 vides -> GAME OVER.
if vides == 0:
    print("GAME OVER")
else:   # S'executa s l'usuari li queda alguna vida
    print(f"Has sobreviscut. Amb {punts} punts en total.\nENHORABONA") # Diu els punts que ha aconseguit l'usuari
    # A partir d'aquí té més sentit si el trivial tingués més preguntes
    puntuacio = (punts / (len(banc_de_preguntes) * 10)) * 10    # calcula la nota del usuari a partir de la puntuació aconseguida entre el nombre de preguntes que hi ha al test (x 10, perquè cada pregunta dona 10 punts) sobre 10 (el segon x10)
    if 5 <= puntuacio < 7:
        print(f"Has sobreviscut satisfacoriament, és encara més sorprenent ({puntuacio:.2f})/10)")
    elif 7 <= puntuacio < 9:
        print(f"Has sobreviscut notablement, és encara més sorprenent ({puntuacio:.2f}/10)")
    elif 9 <= puntuacio < 10:
        print(f"Ho has fet gairebé perfecte, ets fascinant :O ({puntuacio:.2f}/10)")
    elif puntuacio == 10:
        print(f"Ho has fet perfecte, ets fascinant :O ({puntuacio:.2f}/10)")
    else:
        print(f"Has sobreviscut, però has d'estudiar més que el pròxim com no tindràs tanta sort ;) ({puntuacio}/10)")
        