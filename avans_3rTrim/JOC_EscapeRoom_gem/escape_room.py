import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class EscapeRoom:
    def __init__(self):
        self.inventory = []
        self.code_known = False
        self.playing = True
        self.current_location = "Sala d'Estar"

    def show_header(self):
        clear_screen()
        print("="*40)
        print("     ESCAPE ROOM: L'HABITACIÓ DE GEMINI     ")
        print("="*40)
        print(f" Ubicació: {self.current_location}")
        print(f" Inventari: {', '.join(self.inventory) if self.inventory else 'Buit'}")
        print("-" * 40)

    def show_controls(self, options):
        print("\n--- PANEL DE CONTROLS ---")
        for i, option in enumerate(options, 1):
            print(f" [{i}] {option}")
        print(" [Q] Sortir del joc")
        print("-" * 40)

    def play(self):
        while self.playing:
            self.show_header()
            
            if self.current_location == "Sala d'Estar":
                options = ["Mirar sota el sofà", "Anar a la Cuina", "Anar a la Porta de Sortida"]
                self.show_controls(options)
                choice = input("Selecciona un botó: ").upper()
                
                if choice == "1":
                    if "Clau de Plata" not in self.inventory:
                        print("\nHas trobat una Clau de Plata!")
                        self.inventory.append("Clau de Plata")
                    else:
                        print("\nNo hi ha res més sota el sofà.")
                elif choice == "2":
                    self.current_location = "Cuina"
                elif choice == "3":
                    self.current_location = "Porta de Sortida"
                elif choice == "Q":
                    self.playing = False

            elif self.current_location == "Cuina":
                options = ["Obrir la nevera", "Mirar la nota a la paret", "Tornar a la Sala d'Estar"]
                self.show_controls(options)
                choice = input("Selecciona un botó: ").upper()
                
                if choice == "1":
                    print("\nNomés hi ha un iogurt caducat...")
                elif choice == "2":
                    print("\nLa nota diu: 'El codi és el número de potes d'una aranya multiplicat per 100'.")
                    self.code_known = True
                elif choice == "3":
                    self.current_location = "Sala d'Estar"
                elif choice == "Q":
                    self.playing = False

            elif self.current_location == "Porta de Sortida":
                options = ["Utilitzar la clau", "Introduir codi numèric", "Tornar a la Sala d'Estar"]
                self.show_controls(options)
                choice = input("Selecciona un botó: ").upper()
                
                if choice == "1":
                    if "Clau de Plata" in self.inventory:
                        print("\nLa clau gira perfectament!")
                        self.inventory.remove("Clau de Plata")
                        self.inventory.append("Porta Desbloquejada")
                    else:
                        print("\nNecessites una clau!")
                elif choice == "2":
                    code = input("Introdueix el codi de 3 xifres: ")
                    if code == "800":
                        print("\nCodi correcte! El teclat es posa en verd.")
                        self.inventory.append("Codi Acceptat")
                    else:
                        print("\nCodi incorrecte.")
                elif choice == "3":
                    self.current_location = "Sala d'Estar"
                elif choice == "Q":
                    self.playing = False

            # Condició de victòria
            if "Porta Desbloquejada" in self.inventory and "Codi Acceptat" in self.inventory:
                self.show_header()
                print("\nFELICITATS! Has obert la porta i has escapat de l'habitació!")
                print("Gràcies per jugar a 'By Coding with Gemini'.")
                self.playing = False
            
            if self.playing:
                input("\nPrem [ENTER] per continuar...")

if __name__ == "__main__":
    game = EscapeRoom()
    game.play()
