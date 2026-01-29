import requests
import json

def crida_api(api_key: str, ciutat: str, dies: int):
    
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    
    parametres = {
        "key": api_key,
        "q": ciutat,
        "days": dies,
        "aqi": "no",
        "alerts": "no"
    }
    
    print(f"\n🌍 Connectant amb el satèl·lit per veure el temps a {ciutat}...")
    
    resposta = requests.get(base_url, params=parametres)
    
    if resposta.status_code == 200:
        dades = resposta.json()
        
        # --- NOVES LÍNIES PER GUARDAR A TXT ---
        nom_fitxer = f"dades_temps_{ciutat}.txt"
        
        with open(nom_fitxer, "w", encoding="utf-8") as fitxer:
            # Usem json.dump per escriure el diccionari directament al fitxer
            # indent=4 fa que el text sigui llegible per humans
            json.dump(dades, fitxer, indent=4, ensure_ascii=False)
        
        print(f"\✅ Dades guardades correctament a: {nom_fitxer}")
        # --------------------------------------
        
        data_actual = dades["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        temp_max = dades["forecast"]["forecastday"][0]["date"]
        temp_actual = dades["current"]["temp_c"]
       # print(f"🌡️  Ara mateix a {ciutat} esteu a: {temp_actual}ºC")
      #  print(f"🌡️  Ara mateix a {ciutat} esteu a: {temp_max}ºC")

        print("\nPREVISIÓ PER A TOKYO")
        print("--------------------")
        for i in range(dies):
            data_actual = dades["forecast"]["forecastday"][i]["day"]["maxtemp_c"]
            temp_max = dades["forecast"]["forecastday"][i]["date"]
            freq_barres = temp_max//3
            if temp_max < 14:
                estat = "Fred"
            elif 14 <= temp_max <= 17.5:
                estat = "Agradable" 
            else:
                estat = "Calorós"
            print(f"{data_actual} | {█ * freq_barres} {temp_max} ({estat})")
        #temp_actual = dades["current"]["temp_c"]
        #print(f"{data_actual} | █████ 15.5°C (Agradable)")
        #2026-02-12 | ████ 13.2°C (Fred)
    
    else:
        print(f"❌ Error {resposta.status_code}: No s'ha pogut obtenir la informació.")

# --- CONFIGURACIÓ ---
api_key = "62c192a50ec440b68f2122508262101" # Recorda posar la teva clau real!
ciutat = input("\n> De quina ciutat vols saber el temps? ")
dies = int(input("> Quants dies? (entre 1 i 14) ")) 

crida_api(api_key, ciutat, dies)