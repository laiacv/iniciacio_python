import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import threading

class EscapeRoom3GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ESCAPE ROOM v3.0 - MISSÍO CRÍTICA")
        self.root.geometry("850x700")
        self.root.configure(bg="#1a1a1a")

        # Estat del joc
        self.inventory = []
        self.current_room = "Lobby"
        self.safe_opened = False
        self.terminal_hacked = False
        self.machine_stable = False
        self.time_left = 300  # 5 minuts en segons
        self.game_over = False

        # Definició del mapa
        self.rooms_data = {
            "Lobby": {
                "desc": "Estàs a l'entrada principal de la instal·lació secreta. Hi ha una catifa vella i una porta de fusta al nord.",
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
                "desc": "L'aire és dens aquí baix. Una gran porta d'acer a l'est porta a la Sala de Control.",
                "exits": {"Nord": "Laboratori", "Est": "Sala de Control", "Sud": "Sortida Final"}
            },
            "Sala de Control": {
                "desc": "Plena de pantalles parpellejant. La unitat central sembla inestable.",
                "exits": {"Oest": "Soterrani"}
            },
            "Sortida Final": {
                "desc": "La gran porta d'acer cap a la llibertat. Requereix autorització màxima.",
                "exits": {"Nord": "Soterrani"}
            }
        }

        self.setup_ui()
        self.update_ui()
        self.start_timer()

    def setup_ui(self):
        # Títol i Timer
        self.header_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.header_frame.pack(pady=10, fill="x")

        self.title_label = tk.Label(self.header_frame, text="ESCAPE THE CORE", font=("Courier", 26, "bold"), bg="#1a1a1a", fg="#e74c3c")
        self.title_label.pack(side="left", padx=30)

        self.timer_label = tk.Label(self.header_frame, text="TEMPS: 05:00", font=("Courier", 20, "bold"), bg="#1a1a1a", fg="#f1c40f")
        self.timer_label.pack(side="right", padx=30)

        # Pantalla de descripció
        self.desc_frame = tk.Frame(self.root, bg="#2d3436", bd=3, relief="flat")
        self.desc_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.desc_text = tk.Label(self.desc_frame, text="", wraplength=750, font=("Verdana", 14), bg="#2d3436", fg="#dfe6e9", justify="center")
        self.desc_text.pack(expand=True, fill="both", padx=20, pady=20)

        # Panell de Control (Botons d'acció)
        self.control_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.control_frame.pack(pady=10)

        self.btn_action1 = tk.Button(self.control_frame, text="Acció 1", width=30, height=2, bg="#2980b9", fg="white", font=("Arial", 11, "bold"), command=lambda: self.handle_action(1))
        self.btn_action1.grid(row=0, column=0, padx=10, pady=5)

        self.btn_action2 = tk.Button(self.control_frame, text="Acció 2", width=30, height=2, bg="#d35400", fg="white", font=("Arial", 11, "bold"), command=lambda: self.handle_action(2))
        self.btn_action2.grid(row=0, column=1, padx=10, pady=5)

        # Botons de Moviment
        self.move_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.move_frame.pack(pady=10)
        
        tk.Label(self.move_frame, text="NAVEGACIÓ", bg="#1a1a1a", fg="#636e72", font=("Arial", 10, "bold")).pack()
        self.dir_buttons_frame = tk.Frame(self.move_frame, bg="#1a1a1a")
        self.dir_buttons_frame.pack()

        btn_style = {"width": 12, "height": 1, "bg": "#34495e", "fg": "white", "font": ("Arial", 10, "bold")}
        
        self.btn_n = tk.Button(self.dir_buttons_frame, text="▲ NORD", **btn_style, command=lambda: self.move("Nord"))
        self.btn_n.grid(row=0, column=1, pady=3)
        self.btn_w = tk.Button(self.dir_buttons_frame, text="◀ OEST", **btn_style, command=lambda: self.move("Oest"))
        self.btn_w.grid(row=1, column=0, padx=3)
        self.btn_e = tk.Button(self.dir_buttons_frame, text="EST ▶", **btn_style, command=lambda: self.move("Est"))
        self.btn_e.grid(row=1, column=2, padx=3)
        self.btn_s = tk.Button(self.dir_buttons_frame, text="▼ SUD", **btn_style, command=lambda: self.move("Sud"))
        self.btn_s.grid(row=2, column=1, pady=3)

        # Inventari
        self.inv_label = tk.Label(self.root, text="INVENTARI: Buit", font=("Consolas", 12), bg="#1a1a1a", fg="#2ecc71")
        self.inv_label.pack(side="bottom", pady=25)

    def start_timer(self):
        def count_down():
            while self.time_left > 0 and not self.game_over:
                mins, secs = divmod(self.time_left, 60)
                time_str = f"{mins:02d}:{secs:02d}"
                self.timer_label.config(text=f"TEMPS: {time_str}")
                time.sleep(1)
                self.time_left -= 1
            
            if self.time_left <= 0 and not self.game_over:
                self.game_over = True
                messagebox.showerror("FI DEL TEMPS", "L'edifici ha entrat en autodestrucció. HAS PERDUT!")
                self.root.destroy()

        threading.Thread(target=count_down, daemon=True).start()

    def update_ui(self):
        room = self.rooms_data[self.current_room]
        description = room["desc"]

        # Lògica específica segons l'estat
        if self.current_room == "Soterrani" and "Lot" not in self.inventory:
            description = "Està tot fosc. No pots veure res sense una font de llum.\n(Has d'agafar el Lot del laboratori)"
            self.btn_action1.config(state="disabled", text="---", bg="#4b4b4b")
            self.btn_action2.config(state="disabled", text="---", bg="#4b4b4b")
        else:
            self.btn_action1.config(state="normal", bg="#2980b9")
            self.btn_action2.config(state="normal", bg="#d35400")
            
            if self.current_room == "Lobby":
                self.btn_action1.config(text="Mirar sota la catifa")
                self.btn_action2.config(text="Inspeccionar bust de marbre")
            elif self.current_room == "Biblioteca":
                self.btn_action1.config(text="Consultar enciclopèdia")
                self.btn_action2.config(text="Tirar palanca de ferro")
            elif self.current_room == "Laboratori":
                self.btn_action1.config(text="Hackejar Terminal Central")
                self.btn_action2.config(text="Agafar Lot tàctic")
            elif self.current_room == "Soterrani":
                self.btn_action1.config(text="Buscar la Targeta VIP")
                self.btn_action2.config(text="Obrir quadre elèctric")
            elif self.current_room == "Sala de Control":
                self.btn_action1.config(text="Estabilitzar Nucli (Seqüència)")
                self.btn_action2.config(text="Cercar clau mestra")
            elif self.current_room == "Sortida Final":
                self.btn_action1.config(text="VALIDAR PROTOCOL DE SORTIDA", bg="#27ae60")
                self.btn_action2.config(state="disabled", text="---", bg="#4b4b4b")

        self.desc_text.config(text=description)
        self.inv_label.config(text=f"INVENTARI: {' | '.join(self.inventory) if self.inventory else 'Buit'}")

        # Activar/Desactivar botons de moviment
        exits = room["exits"]
        self.btn_n.config(state="normal" if "Nord" in exits else "disabled")
        self.btn_s.config(state="normal" if "Sud" in exits else "disabled")
        self.btn_e.config(state="normal" if "Est" in exits else "disabled")
        self.btn_w.config(state="normal" if "Oest" in exits else "disabled")

    def move(self, direction):
        next_room = self.rooms_data[self.current_room]["exits"].get(direction)
        if next_room:
            # Bloquejos
            if next_room == "Soterrani" and not self.safe_opened:
                messagebox.showwarning("Bloqueig", "La porta de l'ascensor al soterrani no té corrent.")
                return
            if next_room == "Sala de Control" and not self.terminal_hacked:
                messagebox.showwarning("Seguretat", "La porta de control requereix accés de l'administrador.")
                return
                
            self.current_room = next_room
            self.update_ui()

    def handle_action(self, action_num):
        if self.current_room == "Lobby":
            if action_num == 1:
                if "Nota" not in self.inventory:
                    self.inventory.append("Nota")
                    messagebox.showinfo("Lobby", "Has trobat una nota: 'El protocol segueix la seqüència R-G-B'.")
            else:
                messagebox.showinfo("Lobby", "El bust de marbre té una placa: '1984'.")
        
        elif self.current_room == "Biblioteca":
            if action_num == 1:
                messagebox.showinfo("Biblioteca", "L'enciclopèdia té marcat l'any '1984'.")
            else:
                self.safe_opened = True
                messagebox.showinfo("Mecanisme", "Corrent restaurat. L'ascensor al soterrani ara funciona.")
        
        elif self.current_room == "Laboratori":
            if action_num == 1:
                code = simpledialog.askstring("Terminal", "Codi d'administrador (4 xifres):")
                if code == "1984":
                    self.terminal_hacked = True
                    messagebox.showinfo("Terminal", "ACCÉS CONCEDIT. Portes internes obertes.")
                else:
                    messagebox.showerror("Error", "Codi incorrecte.")
            else:
                if "Lot" not in self.inventory:
                    self.inventory.append("Lot")
                    messagebox.showinfo("Inventari", "Lot tàctic afegit!")
        
        elif self.current_room == "Soterrani":
            if action_num == 1:
                if "Targeta VIP" not in self.inventory:
                    self.inventory.append("Targeta VIP")
                    messagebox.showinfo("Inventari", "Has trobat la Targeta VIP al terra!")
            else:
                messagebox.showinfo("Soterrani", "El quadre elèctric ja està actiu.")

        elif self.current_room == "Sala de Control":
            if action_num == 1:
                seq = simpledialog.askstring("Nucli", "Introdueix seqüència de colors (Inicials):")
                if seq and seq.upper() == "RGB":
                    self.machine_stable = True
                    messagebox.showinfo("Nucli", "ESTABILITZAT. Sortida principal autoritzada.")
                else:
                    messagebox.showerror("Error", "Seqüència incorrecta!")
            else:
                messagebox.showinfo("Cerca", "Només trobes pantalles trencades.")

        elif self.current_room == "Sortida Final":
            if "Targeta VIP" in self.inventory and self.machine_stable:
                self.game_over = True
                messagebox.showinfo("Llibertat", f"HAS ESCAPAT! Et quedaven {self.time_left} segons. EXCEL·LENT!")
                self.root.destroy()
            else:
                messagebox.showwarning("Denegat", "Requereix Targeta VIP i estabilització del Nucli.")

        self.update_ui()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = EscapeRoom3GUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
