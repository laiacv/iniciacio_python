nom = "Prova"
edat = 30
pes = 70.0
estudiant = True

print(f"Dades fixades: nom={nom}, edat={edat}, pes={pes}, estudiant={estudiant}")

nom_per = input("\nIntrodueix el teu nom: ")
edat_per = int(input("Introdueix la teva edat: "))
pes_per = float(input("Introdueix el teu pes (kg): "))
alt_per = float(input("Introdueix la teva altura (m): "))

print("\n---- Informe de salut ----")

print(f"Nom: {nom_per}")
print(f"Edat: {edat_per} (tipo: {type(edat_per)})")
print(f"Pes: {pes_per} kg (tipo: {type(pes_per)})")
print(f"Altura: {alt_per} m (tipo: {type(alt_per)})")

imc = pes_per/(alt_per**2)

print(f"\nÍndex de massa corporal (IMC): {imc: .2f}")


if imc <= 18.5:
    IMC = "pes baix"

elif 18.5 < imc <= 24.9:
    IMC = "pes normal o òptim"

elif 24.9 < imc <= 29.9:
    IMC = "sobrepès"

elif 29.9 < imc <= 34.9:
    IMC = "obesitat de classe I"

elif 34.9 < imc <= 39.9:
    IMC = "obesitat de classe II"

elif imc > 39.9:
    IMC = "obesitat de classe III o mòrbida"

print(f"Classificació: {IMC}")

print("----------------------------------")