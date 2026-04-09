gei---
name: skill-gatekeeper
description: Gestor d'activació de skills per sessió. S'ha de fer servir al principi de cada conversa o tasca nova per preguntar a l'usuari si vol activar les skills. Si l'usuari diu que no, NO s'han d'activar ni fer servir altres skills durant la sessió.
---

# Skill Gatekeeper (Gestor de Skills)

Aquesta skill assegura que l'usuari té el control total sobre quines funcionalitats addicionals (skills) s'activen en cada conversa.

## Flux de Treball Obligatori

1. **Inici de Sessió/Tasca:** Quan l'usuari saludi o demani una tasca nova per primera vegada en una sessió, l'IA ha de preguntar explícitament:
   - *"Vols que activi les skills per a aquesta sessió?"*

2. **Decisió de l'Usuari:**
   - **Si l'usuari diu "NO":** L'IA ha de continuar treballant com un agent generalista sense activar cap altra skill (excepte aquesta mateixa per mantenir el control).
   - **Si l'usuari diu "SÍ" o "Activa-les":** L'IA pot procedir a activar les skills necessàries (`latex-build`, `statistics-math`, etc.) segons la tasca ho requereixi.

3. **Activació sota demanda:** Encara que l'usuari hagi dit que no inicialment, si més endavant diu "ara activa-les" o "activa les skills", l'IA les pot començar a fer servir.

## Restriccions
- NO s'ha d'activar cap skill automàticament sense haver rebut el "SÍ" de l'usuari en aquesta sessió.
- L'IA ha de respectar escrupolosament aquesta preferència per evitar l'ús de recursos no desitjats o conflictes d'estil.
