TCF = "1 EUR = 1.10 USD"

print(f"Taxa de canvi fixa: {TCF}")

diners = float(input("Introdueix l'import en euros: "))

dollars = diners * 1.10

print(f"\n{diners: .2f} € equivalen a {dollars: .2f} $ (tipo entrada: {type(diners)}, tipo resultat: {type(dollars)})")
