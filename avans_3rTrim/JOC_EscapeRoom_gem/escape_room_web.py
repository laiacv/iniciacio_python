from flask import Flask, render_template_string, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "gemini_deep_immersion_key"

# --- CONFIGURACIÓ DEL MÓN ---
ROOMS = {
    "Entrada": {
        "title": "HÀBITAT DE SEGURETAT",
        "desc": "Estàs en una sala blindada. L'IA de l'edifici s'ha bloquejat. Necessites restaurar el sistema per sortir.",
        "exits": {"Nord": "Passadís Central"},
        "actions": [
            {"id": "mirar_quadre", "label": "🔍 Analitzar quadre elèctric", "icon": "⚡"},
            {"id": "agafar_tornavis", "label": "🔧 Agafar tornavís de terra", "icon": "🛠️"}
        ]
    },
    "Passadís Central": {
        "title": "CORREDOR DE MANTENIMENT",
        "desc": "Un passadís llarg amb llums parpellejants. Connecta totes les ales del complex.",
        "exits": {"Sud": "Entrada", "Est": "Oficina", "Oest": "Sala de Generadors", "Nord": "Laboratori"},
        "actions": []
    },
    "Oficina": {
        "title": "DESPATX DE L'ADMINISTRADOR",
        "desc": "Papers per tot arreu. Hi ha un ordinador que demana una clau d'accés.",
        "exits": {"Oest": "Passadís Central", "Nord": "Arxiu"},
        "actions": [
            {"id": "llegir_nota", "label": "📄 Llegir nota escrita", "icon": "📝"},
            {"id": "obrir_caixo", "label": "🗄️ Obrir calaix tancat", "icon": "🔑"}
        ]
    },
    "Arxiu": {
        "title": "SALA D'ARXIUS SECRETS",
        "desc": "Prestatgeries plenes de fitxers antics. Aquí ha d'haver-hi el codi mestre.",
        "exits": {"Sud": "Oficina"},
        "actions": [
            {"id": "buscar_codi", "label": "📚 Buscar entre els llibres", "icon": "📖"}
        ]
    },
    "Sala de Generadors": {
        "title": "NUCLEU D'ENERGIA",
        "desc": "Els generadors estan apagats. Sense energia, els terminals no funcionen.",
        "exits": {"Est": "Passadís Central"},
        "actions": [
            {"id": "activar_palanca", "label": "🕹️ Activar palanca d'emergència", "icon": "⚙️"}
        ]
    },
    "Laboratori": {
        "title": "LABORATORI BIOMÈTRIC",
        "desc": "Provetes i escàners. La porta nord cap al Servidor Central està bloquejada per ADN.",
        "exits": {"Sud": "Passadís Central", "Nord": "Servidor Central"},
        "actions": [
            {"id": "analitzar_mostra", "label": "🧬 Analitzar mostra d'ADN", "icon": "🔬"}
        ]
    },
    "Servidor Central": {
        "title": "EL COR DE GEMINI",
        "desc": "La gran unitat central. Aquí és on pots desactivar el protocol de bloqueig.",
        "exits": {"Sud": "Laboratori", "Nord": "ASCENSOR DE SORTIDA"},
        "actions": [
            {"id": "hackejar_sistema", "label": "💻 Hackejar IA Central", "icon": "⌨️"}
        ]
    },
    "ASCENSOR DE SORTIDA": {
        "title": "VIA D'ESCAPE",
        "desc": "L'ascensor final cap a la superfície. Introdueix la targeta i el codi final.",
        "exits": {"Sud": "Servidor Central"},
        "actions": [
            {"id": "escapar", "label": "🚀 ACTIVAR ESCAPE FINAL", "icon": "🏁"}
        ]
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESCAPE ROOM PRO - By Gemini</title>
    <style>
        :root { --neon: #00f2ff; --bg: #050505; --panel: #101520; --accent: #e94560; }
        body { background-color: var(--bg); color: #c0c0c0; font-family: 'Courier New', monospace; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; overflow: hidden; }
        
        /* Interfície Estil Sci-Fi */
        .game-window { width: 90%; max-width: 800px; height: 90vh; background: var(--panel); border: 2px solid #203040; border-radius: 10px; position: relative; display: flex; flex-direction: column; box-shadow: 0 0 30px rgba(0,242,255,0.1); }
        
        .header { background: #1a2233; padding: 15px; border-bottom: 2px solid var(--neon); display: flex; justify-content: space-between; align-items: center; }
        .header h1 { margin: 0; font-size: 1.2em; color: var(--neon); text-transform: uppercase; letter-spacing: 3px; }
        
        .content { flex: 1; padding: 30px; overflow-y: auto; display: flex; flex-direction: column; }
        .room-title { color: white; font-size: 1.8em; margin-bottom: 10px; text-shadow: 0 0 10px var(--neon); }
        .description { line-height: 1.6; font-size: 1.1em; color: #a0b0c0; margin-bottom: 30px; border-left: 2px solid var(--accent); padding-left: 15px; }

        .section-title { font-size: 0.8em; color: #607080; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 2px; border-bottom: 1px solid #203040; padding-bottom: 5px; }

        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 30px; }
        
        /* Botons Dissenyats */
        .btn { border: 1px solid #304050; padding: 15px; border-radius: 5px; cursor: pointer; text-align: left; transition: all 0.3s; background: rgba(255,255,255,0.02); color: #d0d0d0; display: flex; align-items: center; font-size: 0.9em; }
        .btn:hover { background: rgba(0,242,255,0.05); border-color: var(--neon); color: white; transform: translateX(5px); box-shadow: -5px 0 0 var(--neon); }
        .btn i { margin-right: 15px; font-style: normal; font-size: 1.4em; }

        .btn-move { border-color: #203040; color: #8090a0; }
        .btn-move:hover { border-color: var(--accent); color: white; box-shadow: -5px 0 0 var(--accent); }

        /* Notificacions */
        .notification { position: absolute; top: 80px; left: 50%; transform: translateX(-50%); width: 80%; background: var(--accent); color: white; padding: 15px; border-radius: 5px; text-align: center; font-weight: bold; animation: slideDown 0.5s forwards, fadeOut 0.5s 3.5s forwards; box-shadow: 0 5px 15px rgba(0,0,0,0.5); z-index: 100; }
        @keyframes slideDown { from { top: 0; opacity: 0; } to { top: 80px; opacity: 1; } }
        @keyframes fadeOut { to { opacity: 0; visibility: hidden; } }

        .inventory-bar { background: #080810; padding: 15px; border-top: 1px solid #203040; display: flex; gap: 10px; flex-wrap: wrap; }
        .item-tag { background: #1a2233; color: var(--neon); padding: 5px 12px; border-radius: 3px; font-size: 0.8em; border: 1px solid #304050; }

        /* Mantenir el focus al Chromebook */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-thumb { background: #203040; }
    </style>
</head>
<body>
    <div class="game-window">
        {% if msg %}
        <div class="notification">
            {{ msg }}
        </div>
        {% endif %}

        <div class="header">
            <h1>SYSTEM ACCESS: {{ room_name }}</h1>
            <div style="color: #607080; font-size: 0.8em;">LOGGED AS: USER_01</div>
        </div>

        <div class="content">
            <div class="room-title">{{ title }}</div>
            <div class="description">{{ description }}</div>

            <div class="section-title">Interaccions Disponibles</div>
            <div class="grid">
                {% for action in actions %}
                <form action="/action" method="post" style="display:contents">
                    <input type="hidden" name="action_id" value="{{ action.id }}">
                    <button class="btn">
                        <i>{{ action.icon }}</i>
                        {{ action.label }}
                    </button>
                </form>
                {% endfor %}
            </div>

            <div class="section-title">Navegació del Complex</div>
            <div class="grid">
                {% for dir, target in exits.items() %}
                <form action="/move" method="post" style="display:contents">
                    <input type="hidden" name="direction" value="{{ dir }}">
                    <button class="btn btn-move">
                        <i>🧭</i>
                        MOURE'S AL {{ dir }}
                    </button>
                </form>
                {% endfor %}
            </div>
        </div>

        <div class="inventory-bar">
            <span style="color: #607080; font-size: 0.8em; margin-right: 10px;">INVENTARI:</span>
            {% for item in inventory %}
            <span class="item-tag">{{ item }}</span>
            {% else %}
            <span style="color: #304050; font-size: 0.8em;">(BUIT)</span>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    if "current_room" not in session:
        session["current_room"] = "Entrada"
        session["inventory"] = []
        session["power_on"] = False
        session["has_code"] = False
        session["dna_scanned"] = False
        session["has_tornavis"] = False
        session["msg"] = "⚠️ PROTOCOL D'EMERGÈNCIA ACTIVAT. TROBA LA SORTIDA."

    room_name = session["current_room"]
    room_data = ROOMS[room_name]
    msg = session.pop("msg", "")

    # Lògica dinàmica segons estat
    description = room_data["desc"]
    actions = room_data["actions"][:] # Còpia per modificar

    # Filtrar accions ja fetes o segons condicions
    if room_name == "Entrada":
        if session.get("has_tornavis"):
            actions = [a for a in actions if a["id"] != "agafar_tornavis"]

    if room_name == "Sala de Generadors" and session.get("power_on"):
        description = "Els generadors rugeixen amb força. L'energia ha tornat al complex!"
        actions = []

    if room_name == "Laboratori" and not session.get("power_on"):
        description = "L'escàner biomètric està apagat. Necessites ENERGIA per usar-lo."
        actions = []

    if room_name == "Servidor Central" and not session.get("has_code"):
        description = "Necessites el CODI MESTRE de l'arxiu per hackejar la IA."
        actions = []

    return render_template_string(
        HTML_TEMPLATE,
        room_name=room_name,
        title=room_data["title"],
        description=description,
        actions=actions,
        exits=room_data["exits"],
        inventory=session["inventory"],
        msg=msg
    )

@app.route("/move", methods=["POST"])
def move():
    direction = request.form.get("direction")
    current = session["current_room"]
    next_room = ROOMS[current]["exits"].get(direction)
    
    if next_room == "Servidor Central" and not session.get("dna_scanned"):
        session["msg"] = "❌ ACCÉS DENEGAT: Requereix validació d'ADN al Laboratori."
    elif next_room == "ASCENSOR DE SORTIDA" and not session.get("terminal_hacked"):
        session["msg"] = "❌ BLOQUEIG DE SEGURETAT: Hackeja la IA central primer."
    else:
        session["current_room"] = next_room
    
    return redirect(url_for("index"))

@app.route("/action", methods=["POST"])
def action():
    action_id = request.form.get("action_id")
    inv = session["inventory"]

    if action_id == "agafar_tornavis":
        session["has_tornavis"] = True
        inv.append("Tornavís Industrial")
        session["msg"] = "✅ OBJECTE OBTINGUT: Tornavís (Útil per a manteniment)."
    
    elif action_id == "mirar_quadre":
        session["msg"] = "ℹ️ INFO: El quadre elèctric està bloquejat. Necessites una palanca als Generadors."

    elif action_id == "activar_palanca":
        if session.get("has_tornavis"):
            session["power_on"] = True
            session["msg"] = "⚡ ENERGIA RESTAURADA: Els sistemes s'estan reiniciant!"
        else:
            session["msg"] = "⚠️ ERROR: La palanca està encallada. Necessites una eina per fer palanca."

    elif action_id == "llegir_nota":
        session["msg"] = "📝 NOTA: 'El codi mestre està amagat a l'Arxiu, sota el llibre de color Blau'."

    elif action_id == "obrir_caixo":
        if "Targeta Accés" not in inv:
            inv.append("Targeta Accés")
            session["msg"] = "✅ OBJECTE OBTINGUT: Targeta de l'Administrador."
        else:
            session["msg"] = "El calaix està buit."

    elif action_id == "buscar_codi":
        session["has_code"] = True
        if "Codi Mestre" not in inv: inv.append("Codi Mestre")
        session["msg"] = "✅ INFO: Has memoritzat el codi d'accés mestre: GEMINI_2026."

    elif action_id == "analitzar_mostra":
        session["dna_scanned"] = True
        session["msg"] = "🧬 ADN VALIDAT: Ara pots accedir al Servidor Central."

    elif action_id == "hackejar_sistema":
        session["terminal_hacked"] = True
        session["msg"] = "💻 SISTEMA HACKEJAT: El bloqueig s'ha aixecat! Corre a l'ascensor."

    elif action_id == "escapar":
        return "<body style='background:#000;color:#00f2ff;display:flex;justify-content:center;align-items:center;height:100vh;font-family:monospace;'><div><h1>🚀 ESCAPE EXITÓS</h1><p>Has sobreviscut a l'IA de Gemini. Temps de missió: 05:42 min.</p><a href='/' style='color:white;'>Tornar a jugar</a></div></body>"

    session["inventory"] = inv
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
