# Compta quantes vegades apareix una lletra en un text
def comptar_lletres(text: str, lletra: str) -> int:
    """
    Docstring para comptar_lletres
    
    :param text: És el text el qual li volem contar les lletres
    :type text: str
    :param lletra: la lletra que s'està contant en aquell moment
    :type lletra: str
    :return: torna el nombre de vegades surt la lletra en el text
    :rtype: int
    """
    comptador = 0
    for caracter in text:
        if caracter == lletra:
            comptador += 1
    return comptador


# El text que volem analitzar i el passem tot a minúscules amb lower
text = ("vyrueoifrbeyughoinregureoginre").lower()

# Alfabet sencer
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Recorrem cada lletra de l'alfabet
for lletra in alfabet:
    # freqüencia = al nombre enter (int) que retorna la funció
    freq = comptar_lletres(text, lletra)
    
    # Només mostrem les lletres que apareixen mínim 1 cop
    # Les mostrem lletra en majúscula | barra de freqüencia i en nombre de 
    # vegades que surt la lletra en el text
    if freq > 0:
        barra = "██" * freq
        print(lletra.upper() + "|" + barra + freq)