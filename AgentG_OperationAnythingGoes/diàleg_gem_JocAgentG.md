# DOCUMENT DE CONTINUÏTAT: Agent G - Operation Anything Goes

Aquest fitxer és la memòria viva del projecte. Serveix perquè Gemini CLI (IA) pugui reprendre el desenvolupament en qualsevol moment, entenent totes les decisions preses, les mecàniques implementades i l'estil de joc acordat amb la Laia Cabrera Vallejos.

## 1. INFORMACIÓ DEL PROJECTE
- **Títol:** Agent G: Operation Anything Goes
- **Gènere:** Escaperoom / Point & Click
- **Basat en:** Agent A i AnythingGOES
- **Desenvolupadors:** Laia Cabrera Vallejos (Idea i direcció) i Gemini CLI (Codi i implementació)
- **Mètode:** Vibe Coding / Bycoding
- **Tecnologia:** HTML5, CSS3, Vanilla JavaScript, Python (Backend de servei)
- **Data d'inici:** 4 de març de 2026
- **Data de finalització:** 5 de març de 2026
- **Professorat:** Adrià Santacreu

## 2. ESTRUCTURA DE FITXERS
Tots els fitxers estan agrupats a la carpeta `/AgentG_OperationAnythingGoes/`:
1. `index.html`: Conté tot el motor del joc (HTML, CSS i la lògica JS).
2. `AgentG_unMisteri.py`: Servidor web en Python configurat per detectar automàticament la ruta de l'html.
3. `diàleg_gem_JocAgentG.md`: Aquest document de context.

## 3. MECÀNIQUES DE JOC DETALLADES

### A. Escena 1: El Jardí Nord
- **Pedres Aleatòries:** Hi ha 5 pedres repartides amb separacions irregulars. En iniciar la partida (`startGame`), la clau de la mansió s'amaga aleatòriament darrere d'una d'elles.
- **Moviment de Pedres:** En fer clic, les pedres es desplacen cap a baix (`translateY`) i redueixen la seva opacitat per revelar si hi ha la clau.
- **L'Arbre Dinàmic:** L'alçada de l'arbre es genera aleatòriament entre **5.00m i 30.00m**.
    - **Escalat Visual:** El dibuix de l'arbre creix o s'encongeix proporcionalment segons l'alçada.
    - **Copa Corregida:** S'ha ajustat el posicionament de les fulles perquè en arbres petits no sobresurti el tronc.
    - **Pista Clau:** La seva alçada és la base del codi de hacking final.
- **Entrada de la Mansió:** Porta situada a la dreta amb una façana detallada (finestres i marcs).

### B. Escena 2 i 3: Rebedor i Despatx
- **Armari:** Conté la llanterna necessària per al soterrani.
- **Biblioteca:** El llibre "1924" dona la pista per a la caixa forta.
- **Caixa Forta Visual:** En encertar el codi **1924**, s'obre una vista especial (`#safe-interior`). L'usuari ha d'agafar manualment el fusible fent clic. La caixa es mostra buida si s'hi torna a entrar després de recollir l'objecte.

### C. Escena 4: El Soterrani i la Foscor
- **Foscor Total:** S'usa una cortina negra (`#dark-curtain`) que bloqueja la vista i els clics fins que s'encén la llum.
- **Llanterna:** Funciona mitjançant una màscara radial de CSS que segueix el ratolí, revelant el contingut del soterrani.
- **Fusible:** S'ha de col·locar al panell de control per donar energia a l'ordinador.

### D. Hacking i Final
- **Terminal Omega:** Demana un codi de 4 dígits.
- **Post-it d'ajuda:** Apareix una nota groga a la dreta del teclat que diu: *"Recorda Ruby, el codi és el que mesura l'arbre centenari"*.
- **Codi Dinàmic:** El codi és l'alçada de l'arbre sense el punt (ex: 07.45m -> 0745).

### E. Interfície i Feedback (UX)
- **Tooltip Intel·ligent:** El text "inspeccionar..." segueix el cursor però només s'activa per a objectes que encara no han estat utilitzats. Les portes no activen el tooltip per no interferir amb el sistema de drag & drop.
- **Crèdits Interactius:** Botó disponible a la pantalla de victòria. Inclou una **mecànica de pistola retro**:
    - El cursor és una mira.
    - Cada clic fa un soroll de làser retro (`AudioContext`).
    - Es genera un efecte visual de centelleig blanc (`shot-flash`).

## 4. LOGICA TÈCNICA RELLEVANT
- **Estat del joc:** Gestionat per l'objecte `state` en JavaScript (flags, inventari, variables aleatòries).
- **Audio:** Generat sintèticament per codi per no dependre de fitxers externs.
- **Drag & Drop:** Sistema manual basat en `pointerevents` per moure objectes de l'inventari a les zones de drop.

## 5. NOTES PER A FUTURES SESSIÓNS
- Mantenir l'estètica "Low-Fi / Terminal" del terminal verd.
- Qualsevol modificació en la dificultat ha de respectar el sistema aleatori de la clau i l'arbre.
- L'arxiu `index.html` és autònom; conté estils i scripts per evitar dependències de xarxa.

---
*Gràcies per jugar! 🎮✨*
