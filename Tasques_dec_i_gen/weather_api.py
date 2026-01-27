import requests
import json

def crida_api():
    
    # --- 2. PREPARACIÓ DE LA PETICIÓ ---
    # La URL on preguntarem pel temps
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    
    # Els paràmetres que enviem al servidor
    parametres = {
        "key": api_key,
        "q": ciutat,
        "days": dies,
        "aqi": "no",
        "alerts": "no"
    }
    
    print(f"🌍 Connectant amb el satèl·lit per veure el temps a {ciutat}...")
    
    # --- 3. LA CRIDA (Request) ---
    resposta = requests.get(base_url, params=parametres)
    
    # --- 4. PROCESSAMENT DE LA RESPOSTA ---
    if resposta.status_code == 200:
        # Convertim la resposta (text) a un diccionari Python (JSON)
        dades = resposta.json()
        
        # -----------------------------------------------------------
        # DEBUG: Això imprimeix TOTA l'estructura de dades.
        # Feu servir això per investigar on s'amaguen les temperatures.
        # Quan ho tingueu clar, elimineu aquesta línia.
        # -----------------------------------------------------------
        print(json.dumps(dades, indent=4))
        
        # Exemple d'accés a una dada simple:
        temp_actual = dades["current"]["temp_c"]
        print(f"\nAra mateix estem a: {temp_actual}ºC")
    
    else:
        print(f"❌ Error {resposta.status_code}: No s'ha pogut obtenir la informació.")

# --- 1. CONFIGURACIÓ (Variables que haureu de fer interactives) ---
api_key = "ENGANXA_AQUI_LA_TEVA_CLAU"  # <--- Important: Posa la teva API Key!
ciutat = "Girona"
dies = 3 