nom_empresa = "BotigaX"
InVA = 0.21

print(f"Dades fixades: nom_empresa={nom_empresa}, IVA={InVA}")

producte = input("\nIntrodueix el nom del producte: ")
preu = float(input("Introdueix el preu unitari (€): "))
quant = int(input("Introdueix la quantitat: "))

print("\nFactura:")

print(f"Producte: {producte}")
print(f"Preu unitari: {preu} €")
print(f"Quantitat: {quant}")
print(f"Subtotal: {preu*quant} €  (tipo: {type(preu*quant)})")
print(f"IVA ({InVA*100}%): {preu*InVA: .2f} €")
print(f"Total: {preu*quant+preu*InVA: .2f} €")
