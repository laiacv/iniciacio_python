import requests # Importa la llibreria requests que permet enviar peticions HTTP a una API i rebre les seves respostes
import json # importem la llibreria JSON
import time # importem la llibreria time, per després poder fer pauses d'uns segons durant el codi per fer veure que pensa

def crida_api(api_key: str, ciutat: str, dies: int) -> None:
    """
    Docstring para crida_api
    
    :param api_key: la APIkey que utilitzarà per buscar la informació
    :type api_key: str
    :param ciutat: la ciutat de la qual vol saber la informació l'usuari
    :type ciutat: str
    :param dies: de quants dies vol saber el temps l'usuari
    :type dies: int
    """
    
    base_url = "http://api.weatherapi.com/v1/forecast.json" # la base de l'enllaç de l'API de clima
    
    # crea un diccionari que es diu parametres que serà utilitzat per cridar a l'API juntament amb la llibreria requests
    parametres = {
        "key": api_key,
        "q": ciutat,
        "days": dies,
        "aqi": "no",
        "alerts": "no"
    }
    
    # li diu a l'usuari que està buscant la informació de la ciutat que acaba de solicitar i el fa esperar 1.5 segons
    print(f"\n🌍 Connectant amb el satèl·lit per veure el temps a {ciutat}...")
    time.sleep(1.5)
    
    # li assigna el valor de tota la informació obtinguda sobre la ciutat escollida de l'API a partir de la 
    # base_url i els paramentres que li hem donat a la variable resposta 
    resposta = requests.get(base_url, params=parametres)
    
    # si no dona error (error 200 vol dir que tot ha sortit bé)
    if resposta.status_code == 200:
        # la variable dades es la variable resposta pasada a JSON (format fàcil d'entendre i manipular, format per llistes i diccionaris)
        dades = resposta.json()
        
        # --- NOVES LÍNIES PER GUARDAR A TXT ---
        nom_fitxer = f"dades_temps_{ciutat}.txt" # li dona nom al fitxer
        
        with open(nom_fitxer, "w", encoding="utf-8") as fitxer:
            # Usem json.dump per escriure el diccionari directament al fitxer
            # indent=4 fa que el text sigui llegible per humans
            json.dump(dades, fitxer, indent=4, ensure_ascii=False)
        
        # li diu a l'usuari que les dades han sigut guardades a un fitxer que es dirà dades_temps_{ciutat}.txt 
        # i el fa esperar 1 segon
        print(f"\n✅ Dades guardades correctament a: {nom_fitxer}")
        time.sleep(1)
        # --------------------------------------
        
        # temp_actual = dades["current"]["temp_c"] aquesta dada no s'utilitza ja que no ens interessa el temps normal

        # li diu a l'usuari la previsió del temps de la ciutat que ha escollit, la funció upper passa el 
        # text a majúscules
        print(f"\nPREVISIÓ PER A {ciutat.upper()}")
        print("--------------------") # barra de guions estètica
        # bucle for que depen dels dies que vulgui l'usuari de previsió
        for i in range(dies):
            # busca la temperatura màxima i la data del dia entre les llistes i diccionaris del fitxer que hem 
            # creat a partir de l'API
            temp_max = dades["forecast"]["forecastday"][i]["day"]["maxtemp_c"]
            data_actual = dades["forecast"]["forecastday"][i]["date"]
            # calcula quina quantitat de barres ha de tenir el print respecte a a quina és la temperatura màxima 
            # cada barra contaria aproximadament 3 graus Celsius
            freq_barres = round(temp_max / 3)
            # determina a partir de la temperatura i uns paramentres l'estat -> si fa fred, calor o si es a
            # gradable la temperatura màxima
            if temp_max < 14:
                estat = "Fred"
            elif 14 <= temp_max <= 17.5:
                estat = "Agradable" 
            else:
                estat = "Calorós"
            # imprimeix per pantalla la previsió del temps de la ciutat seleccionada amb l'estructura:
            # data de dia una barra vertical, petit gràfic de barres respecte a la temperatura max, la temperatura 
            # màxima i entre parèntesis sí l'estat
            print(f"{data_actual} | {"█" * freq_barres} {temp_max} ({estat})")
    
    # si hi ha algun error s'executa la següent línia la qual diu quin error hi ha hagut i informa l'usuari que no 
    # s'ha pogut obtenir la informació
    else:
        print(f"❌ Error {resposta.status_code}: No s'ha pogut obtenir la informació.")

    

# --- CONFIGURACIÓ ---
#"POSSA L'API key" # s'ha de possar l'API
api_key = "62c192a50ec440b68f2122508262101" # la meva 

# bucle infinit fins que hi hagui un break
while True:
    # pregunta a l'usuari de quina ciutat vol saber el temps
    ciutat = input("\n> De quina ciutat vols saber el temps? ")
    # el segon bucle infinit
    while True:
        # el programa provarà la següent seqüencia sense petar
        try:
            # li pregunta a l'usuari fins a quants dies vol obtenir les dades de la previsió
            dies = int(input("> Quants dies? (entre 1 i 14) "))
            # si l'usuari vol una quantitat de dies que està entre 1 i 14 (inclosos), li dirà 
            # que ha d'estar entre 1 i 14 el nombre de dies i li tornarà a preguntar
            if 1 <= dies <= 14:
                break # si no dona error i està entre 1 i 14, sortirà del segon bucle i seguirà amb el programa
            else:
                print("Introdueix un número enter entre 1 i 14")
                continue 
        except ValueError: # si dona error (no és enter)
            print("Introdueix un número enter entre 1 i 14")

    # crida a la funció "crida_api" amb els parametres variable api_key com api_key, variable ciutat com ciutat
    # i la variable dies com dies
    crida_api(api_key, ciutat, dies)

    # pregunta a l'usuari si vol saber el clima d'una altra ciutat i aquest valor s'assigna a la variable seguir
    seguir = input("> Vols consultar una altra ciutat? (S/N): ").lower()
    # si respon amb alguna resposta que no sigui s o si surt del bucle infinit i el programa s'acaba
    if seguir != "s" and seguir != "si":
        print("Adéu! 👋") # li diu adéu a l'usuari
        break
    # si diu s o si (en minúscules o majúscules) el bucle torna a començar
    else:
        continue