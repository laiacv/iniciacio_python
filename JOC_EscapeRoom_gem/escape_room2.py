import tkinter as tk
from tkinter import messagebox, simpledialog

class EscapeRoomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ESCAPE ROOM v2.1 - By Coding with Gemini")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        # Estat del joc
        self.inventory = []
        self.current_room = "Lobby"
        self.safe_opened = False
        self.terminal_hacked = False

        # Definició del mapa
        self.rooms_data = {
            "Lobby": {
                "desc": "Estàs a l'entrada principal. Hi ha una catifa vella i una porta de fusta al nord.",
                "exits": {"Nord": "Biblioteca"}
            },
            "Biblioteca": {
                "desc": "Milers de llibres t'envolten. Hi ha una palanca a la paret i una porta a l'est.",
                "exits": {"Sud": "Lobby", "Est": "Laboratori"}
            },
            "Laboratori": {
                "desc": "Un lloc fosc ple de provetes. Hi ha un terminal informàtic i una porta al sud.",
                "exits": {"Oest": "Biblioteca", "Sud": "Soterrani"}
            },
            "Soterrani": {
                "desc": "Està molt fosc. Necessites una llum per veure-hi.",
                "exits": {"Nord": "Laboratori", "Sud": "Sortida Final"}
            },
            "Sortida Final": {
                "desc": "La gran porta d'acer cap a la llibertat. Requereix autorització màxima.",
                "exits": {"Nord": "Soterrani"}
            }
        }

        self.setup_ui()
        self.update_ui()

    def setup_ui(self):
        # Títol
        self.title_label = tk.Label(self.root, text="ESCAPE THE LAB", font=("Courier", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=10)

        # Pantalla de descripció
        self.desc_frame = tk.Frame(self.root, bg="#34495e", bd=2, relief="sunken")
        self.desc_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.desc_text = tk.Label(self.desc_frame, text="", wraplength=700, font=("Verdana", 12), bg="#34495e", fg="#ecf0f1", justify="center")
        self.desc_text.pack(expand=True, fill="both", padx=20, pady=20)

        # Panell de Control (Botons d'acció)
        self.control_frame = tk.Frame(self.root, bg="#2c3e50")
        self.control_frame.pack(pady=10)

        self.btn_action1 = tk.Button(self.control_frame, text="Acció 1", width=25, height=2, bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=lambda: self.handle_action(1))
        self.btn_action1.grid(row=0, column=0, padx=10, pady=5)

        self.btn_action2 = tk.Button(self.control_frame, text="Acció 2", width=25, height=2, bg="#e67e22", fg="white", font=("Arial", 10, "bold"), command=lambda: self.handle_action(2))
        self.btn_action2.grid(row=0, column=1, padx=10, pady=5)

        # Botons de Moviment
        self.move_frame = tk.Frame(self.root, bg="#2c3e50")
        self.move_frame.pack(pady=10)
        
        tk.Label(self.move_frame, text="PANEL DE NAVEGACIÓ", bg="#2c3e50", fg="#95a5a6", font=("Arial", 8)).pack()
        self.dir_buttons_frame = tk.Frame(self.move_frame, bg="#2c3e50")
        self.dir_buttons_frame.pack()

        btn_style = {"width": 10, "height": 1, "bg": "#95a5a6", "font": ("Arial", 9, "bold")}
        
        self.btn_n = tk.Button(self.dir_buttons_frame, text="▲ NORD", **btn_style, command=lambda: self.move("Nord"))
        self.btn_n.grid(row=0, column=1, pady=2)
        self.btn_w = tk.Button(self.dir_buttons_frame, text="◀ OEST", **btn_style, command=lambda: self.move("Oest"))
        self.btn_w.grid(row=1, column=0, padx=2)
        self.btn_e = tk.Button(self.dir_buttons_frame, text="EST ▶", **btn_style, command=lambda: self.move("Est"))
        self.btn_e.grid(row=1, column=2, padx=2)
        self.btn_s = tk.Button(self.dir_buttons_frame, text="▼ SUD", **btn_style, command=lambda: self.move("Sud"))
        self.btn_s.grid(row=2, column=1, pady=2)

        # Inventari
        self.inv_label = tk.Label(self.root, text="INVENTARI: Buit", font=("Consolas", 11), bg="#2c3e50", fg="#f1c40f")
        self.inv_label.pack(side="bottom", pady=20)

    def update_ui(self):
        room = self.rooms_data[self.current_room]
        description = room["desc"]

        # Lògica d'habitacions fosques
        if self.current_room == "Soterrani" and "Lot" not in self.inventory:
            description = "Està tot fosc. No pots veure res sense una font de llum.\n(Necessites el Lot del laboratori)"
            self.btn_action1.config(state="disabled", text="---", bg="#7f8c8d")
            self.btn_action2.config(state="disabled", text="---", bg="#7f8c8d")
        else:
            # Configurar botons segons l'habitació
            self.btn_action1.config(state="normal", bg="#3498db")
            self.btn_action2.config(state="normal", bg="#e67e22")
            
            if self.current_room == "Lobby":
                self.btn_action1.config(text="Mirar sota la catifa")
                self.btn_action2.config(text="Trucar al timbre")
            elif self.current_room == "Biblioteca":
                self.btn_action1.config(text="Llegir llibre vell")
                self.btn_action2.config(text="Tirar palanca secreta")
            elif self.current_room == "Laboratori":
                self.btn_action1.config(text="Accedir al Terminal")
                self.btn_action2.config(text="Agafar Lot de mà")
            elif self.current_room == "Soterrani":
                self.btn_action1.config(text="Buscar la Targeta")
                self.btn_action2.config(text="Escoltar sorolls")
            elif self.current_room == "Sortida Final":
                self.btn_action1.config(text="VALIDAR SORTIDA", bg="#27ae60")
                self.btn_action2.config(state="disabled", text="---", bg="#7f8c8d")

        self.desc_text.config(text=description)
        self.inv_label.config(text=f"INVENTARI: {' | '.join(self.inventory) if self.inventory else 'Buit'}")

        # Activar/Desactivar botons de moviment segons sortides
        exits = room["exits"]
        self.btn_n.config(state="normal" if "Nord" in exits else "disabled")
        self.btn_s.config(state="normal" if "Sud" in exits else "disabled")
        self.btn_e.config(state="normal" if "Est" in exits else "disabled")
        self.btn_w.config(state="normal" if "Oest" in exits else "disabled")

    def move(self, direction):
        next_room = self.rooms_data[self.current_room]["exits"].get(direction)
        if next_room:
            if next_room == "Soterrani" and not self.safe_opened:
                messagebox.showwarning("Porta Tancada", "La porta cap avall està bloquejada per un sistema electrònic.")
                return
            self.current_room = next_room
            self.update_ui()

    def handle_action(self, action_num):
        if self.current_room == "Lobby":
            if action_num == 1:
                if "Clau Vella" not in self.inventory:
                    self.inventory.append("Clau Vella")
                    messagebox.showinfo("Inventari", "Has trobat una Clau Vella sota la catifa!")
                else:
                    messagebox.showinfo("Lobby", "Ja has mirat aquí.")
            else:
                messagebox.showinfo("Lobby", "El timbre sona llunyà... ningú respon.")
        
        elif self.current_room == "Biblioteca":
            if action_num == 1:
                messagebox.showinfo("Llibre", "El llibre diu: 'L'ordinador central respon al codi 1234'.")
            else:
                self.safe_opened = True
                messagebox.showinfo("Mecanisme", "Has activat la palanca! S'ha sentit un soroll d'engranatges obrint el pas al soterrani.")
        
        elif self.current_room == "Laboratori":
            if action_num == 1:
                code = simpledialog.askstring("Terminal de Seguretat", "Introdueix codi d'accés:")
                if code == "1234":
                    self.terminal_hacked = True
                    messagebox.showinfo("Terminal", "ACCÉS CONCEDIT. La porta de seguretat final està a l'espera de la targeta física.")
                else:
                    messagebox.showerror("Error", "Codi incorrecte.")
            else:
                if "Lot" not in self.inventory:
                    self.inventory.append("Lot")
                    messagebox.showinfo("Inventari", "Has agafat el Lot. Ara podràs veure en llocs foscos.")
        
        elif self.current_room == "Soterrani":
            if action_num == 1:
                if "Targeta" not in self.inventory:
                    self.inventory.append("Targeta")
                    messagebox.showinfo("Inventari", "Has trobat la Targeta de Seguretat al terra!")
            else:
                messagebox.showinfo("Soterrani", "Sents el so de les canonades d'aigua.")

        elif self.current_room == "Sortida Final":
            if "Targeta" in self.inventory and self.terminal_hacked:
                messagebox.showinfo("Llibertat", "HAS ESCAPAT! La porta s'obre lentament i veus la llum del dia. Felicitats!")
                self.root.destroy()
            else:
                messagebox.showwarning("Seguretat", "La porta no s'obre. Requereix hackeig de terminal i targeta física.")

        self.update_ui()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = EscapeRoomGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error en iniciar el joc: {e}")
        print("Assegura't de tenir instal·lat 'python3-tk' si estàs a Linux.")
