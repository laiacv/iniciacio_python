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

print("😈 BENVINGUT AL TRIVIAL DE LA MORT 😈")
print(f"Comences amb {vides} vides. Bona sort...\n")


# Pista: El joc ha de continuar MENTRE quedin vides (> 0) I l'índex sigui menor que el total de preguntes.
while vides > 0 and index_pregunta < len(banc_de_preguntes):

    # --------------------------------------------------------------------------
    # PAS A: Recuperar la informació
    # --------------------------------------------------------------------------
    # TODO: Crea una variable 'pregunta_actual' i assigna-li el diccionari que toca segons l'índex.
    

    # --------------------------------------------------------------------------
    # PAS B: Mostrar per pantalla
    # --------------------------------------------------------------------------
    # TODO: Fes print de l'enunciat i de les opcions possibles.
    

    # --------------------------------------------------------------------------
    # PAS C: Demanar resposta a l'usuari (Validació)
    # --------------------------------------------------------------------------
    # TODO: Fes un bucle infinit amb TRY-EXCEPT per assegurar que l'usuari introdueix un NÚMERO enter.
    # Guarda la resposta en una variable.
    

    # --------------------------------------------------------------------------
    # PAS D: Comprovar si ha encertat (Lògica del joc)
    # --------------------------------------------------------------------------
    # TODO: Fes un IF/ELSE comparant la resposta de l'usuari amb la 'correcta' del diccionari.
    # - Si encerta: Suma 10 punts i felicita'l.
    # - Si falla: Resta 1 vida i avisa'l de quantes li queden.
    

    # --------------------------------------------------------------------------
    # PAS E: Avançar
    # --------------------------------------------------------------------------
    # TODO: IMPORTANT! Incrementa l'índex per passar a la següent pregunta a la propera volta.
    
    
    print("-" * 30) # Separador estètic entre preguntes


# ==============================================================================
# 3. FINAL DEL JOC
# ==============================================================================

# TODO: Fora del bucle, comprova com ha acabat la partida.
# - Si vides és 0 -> GAME OVER.
# - Si no -> ENHORABONA.
# Finalment, mostra els punts totals.







# ==============================================================================
# 2. BUCLE PRINCIPAL DEL JOC
# ==============================================================================

# TODO: Defineix el WHILE. 
# Pista: El joc ha de continuar MENTRE quedin vides (> 0) I l'índex sigui menor que el total de preguntes.
while vides > 0 and index_pregunta < len(banc_de_preguntes):

    # --------------------------------------------------------------------------
    # PAS A: Recuperar la informació
    # --------------------------------------------------------------------------
    # TODO: Crea una variable 'pregunta_actual' i assigna-li el diccionari que toca segons l'índex.
    

    # --------------------------------------------------------------------------
    # PAS B: Mostrar per pantalla
    # --------------------------------------------------------------------------
    # TODO: Fes print de l'enunciat i de les opcions possibles.
    

    # --------------------------------------------------------------------------
    # PAS C: Demanar resposta a l'usuari (Validació)
    # --------------------------------------------------------------------------
    # TODO: Fes un bucle infinit amb TRY-EXCEPT per assegurar que l'usuari introdueix un NÚMERO enter.
    # Guarda la resposta en una variable.
    

    # --------------------------------------------------------------------------
    # PAS D: Comprovar si ha encertat (Lògica del joc)
    # --------------------------------------------------------------------------
    # TODO: Fes un IF/ELSE comparant la resposta de l'usuari amb la 'correcta' del diccionari.
    # - Si encerta: Suma 10 punts i felicita'l.
    # - Si falla: Resta 1 vida i avisa'l de quantes li queden.
    

    # --------------------------------------------------------------------------
    # PAS E: Avançar
    # --------------------------------------------------------------------------
    # TODO: IMPORTANT! Incrementa l'índex per passar a la següent pregunta a la propera volta.
    
    
    print("-" * 30) # Separador estètic entre preguntes


# ==============================================================================
# 3. FINAL DEL JOC
# ==============================================================================

# TODO: Fora del bucle, comprova com ha acabat la partida.
# - Si vides és 0 -> GAME OVER.
# - Si no -> ENHORABONA.
# Finalment, mostra els punts totals.