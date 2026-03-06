# DOCUMENT DE CONTINUÏTAT: Agent G - Operation Anything Goes

Aquest fitxer és la memòria viva del projecte. Serveix perquè Gemini CLI (IA) pugui reprendre el desenvolupament en qualsevol moment, entenent totes les decisions preses, les mecàniques implementades i l'estil de joc acordat amb la Laia Cabrera Vallejos.

## 1. INFORMACIÓ DEL PROJECTE
- **Títol:** Agent G: Operation Anything Goes
- **Gènere:** Escaperoom / Point & Click
- **Basat en:** Agent A i AnythingGOES
- **Desenvolupadors:** Laia Cabrera Vallejos (Idea i direcció) i Gemini CLI (Codi i implementació)
- **Mètode:** Vibe Coding / Bycoding
- **Tecnologia:** HTML5, CSS3, Vanilla JavaScript, Python (Llançador del servidor)
- **Data d'inici:** 4 de març de 2026
- **Data d'actualització:** 6 de març de 2026
- **Professorat:** Adrià Santacreu

## 2. ESTRUCTURA DE FITXERS
Tots els fitxers estan agrupats a la carpeta `/AgentG_OperationAnythingGoes/`:
1. `index.html`: Conté tot el motor del joc (HTML, CSS i la lògica JS).
2. `musica_AgentG.mp3`: Banda sonora principal del joc.
3. `AgentG_unMisteri.py`: Llançador del servidor web (automatitzat per carregar l'index.html local).
4. `diàleg_gem_JocAgentG.md`: Aquest document de context actualitzat.

## 3. MECÀNIQUES DE JOC DETALLADES

### A. Escena 1: El Jardí Nord
- **Pedres Aleatòries:** Hi ha 5 pedres repartides amb separacions irregulars. En iniciar la partida (`startGame`), la clau de la mansió s'amaga aleatòriament darrere d'una d'elles.
- **Moviment de Pedres:** En fer clic, les pedres es desplacen cap a baix (`translateY`) i redueixen la seva opacitat per revelar si hi ha la clau. **SO:** Efecte de fregament de pedra pesant i potent.
- **L'Arbre Dinàmic:** L'alçada de l'arbre es genera aleatòriament entre **5.00m i 30.00m**. **SO:** Soroll de fulles en examinar-lo.
- **Entrada de la Mansió:** Porta situada a la dreta amb una façana detallada.
    - **Timbre:** S'ha afegit un timbre funcional al costat de la porta. **SO:** "Ding-dong" clàssic amplificat.

### B. Escena 2 i 3: Rebedor i Despatx
- **Armari:** Conté la llanterna. **SO:** Obertura de porta de fusta robusta.
- **Biblioteca:** El llibre "1924" dona la pista. **SO:** Fulleig de llibre en buscar-hi.
- **Caixa Forta:** En encertar el codi **1924**, s'obre una vista especial. **SO:** Mecanisme metàl·lic i obertura pesant.
- **Fusible:** S'ha de recollir de la caixa forta.

### C. Escena 4: El Soterrani i la Foscor
- **Foscor Total:** Bloqueja la vista fins que s'encén la llum.
- **Llanterna:** Revela el contingut mitjançant una màscara radial.
- **Fusible:** S'ha de col·locar al panell. **SO:** Click metàl·lic sec en encaixar-lo.
- **Entrada/Sortida:** El moviment entre el rebedor i el soterrani té un **SO** de pases amb eco.

### D. Hacking i Final
- **Terminal Omega:** Demana un codi de 4 dígits (alçada de l'arbre).
- **Atmosfera de Hacking:** En activar-se el terminal, s'inicia un so d'atmosfera tecnològica i de baixa freqüència.
- **Música de Tensió:** Durant la fase de hacking, la música procedimental canvia a un mode més ràpid i tens, combinant-se amb la música de fons.

### E. Disseny Sonor i UX
- **Música de Fons:** Fitxer `musica_AgentG.mp3` configurat al **20% de volum** per ser un acompanyament atmosfèric no intrusiu.
- **Sons d'Interacció:** Volums apujats (**80%-100%**) per donar feedback clar de les accions (pedres, portes, claus, etc.).
- **Crèdits Interactius:** Es pot disparar un làser retro (so i flash).
    - **Mecànica de Dany:** En disparar als crèdits, la pantalla pateix un efecte de **glitch i distorsió de color durant 3 segons**, després dels quals es restaura automàticament.

## 4. LÒGICA TÈCNICA RELLEVANT
- **Sistema de Sons Mixte:** Combina l'objecte `Audio` (per l'MP3) amb l'`AudioContext` (per als efectes generats per oscil·ladors).
- **Control Global:** El botó de música de l'inventari controla tant el fitxer MP3 com la música procedimental.
- **Estat del joc:** Gestionat per l'objecte `state` (flags, inventari, variables aleatòries).

---
*Gràcies per jugar! 🎮✨*
