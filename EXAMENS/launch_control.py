print("Això és un programa per validar els vols manualment")

denegat = 0
bateria = input("Nivell de bateria (0-100): ")

vent = input("Velocitat del vent (km/h): ")

urg = input("Tipus d'urgència: ")

if bateria <= 20 and vent >= 50:
    print("Bateria baixa i velocitat del vent inestable")
    denegat = 2

elif bateria > 20 and vent < 50:
    print("Bateria òptima i velocitat del vent estable")
    denegat = 0

elif bateria > 20 and vent >= 50:
    print("Bateria òptima i velocitat del vent inestable")
    denegat = 3

elif bateria <= 20 and vent < 50:
    print("Bateria baixa i velocitat del vent estable")
    denegat = 1

print("========================================")
print("[+] ECODRONE FLIGHT CONTROL v2.0")
print("========================================")
print("> DADES DE TELEMETRIA:")

if denegat == 0:
    print(f"Nivell Bateria: [ {bateria} % ] OK")  
    print(f"Velocitat Vent: [ {velocitat} km/h ] ESTABLE")  
    print("—————————————-")
    print("> ANALITZANT SISTEMES...")
    print("»> ESTAT FINAL: [ AUTORITZAT ]")
    print("========================================")

elif denegat == 2:
    print(f"Nivell Bateria: [ {bateria} % ] BATERIA BAIXA")  
    print(f"Velocitat Vent: [ {velocitat} km/h ] INESTABLE")  
    print("—————————————-")
    print("> ANALITZANT SISTEMES...")
    
    print("»> ESTAT FINAL: [ AUTORITZAT ]")
    print("========================================")