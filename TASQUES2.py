nom = "Prova"
edat = 30
pes = 70.0
estudiant = True

print(f"Dades fixades: nom={nom}, edat={edat}, pes={pes}, estudiant={estudiant}")

nom_per = input("Introdueix el teu nom: ")
edat_per = int(input("Introdueix la teva edat: "))
pes_per = float(input("Introdueix el teu pes (kg): "))
alt_per = float(input("Introdueix la teva altura (m): "))

print("---- Informe de salut ----")

print(f"Nom: {nom_per}")
print(f"Edat: {edat_per} (tipo: {type(edat_per)})")
print(f"Pes: {pes_per} (tipo: {type(pes_per)})")
print(f"Altura: {alt_per} (tipo: {type(alt_per)})")

imc = pes_per/(alt_per**2)

print(f"Índex de massa corporal (IMC): {imc}")


if imc <= 18.5:
    IMC = "peso bajo"

elif 18.5 > imc <= 24.9:
    IMC = "peso normal u óptimo"

elif 25 >= imc <= 29.9:
    IMC = "sobrepeso"

elif 30 >= imc <= 34.9:
    IMC = "obesidad de clase I"

elif 35.0 >= imc <= 39.9:
    IMC = "obesidad de clase II"

elif imc >= 40:
    IMC = "obesidad de clase III o mórbida"

print(f"Classificació: {IMC}")