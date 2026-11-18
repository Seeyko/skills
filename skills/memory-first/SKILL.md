---
name: memory-first
description: Lire ce qu'une mémoire MCP a déjà appris sur un sujet avant de commencer une tâche, et y noter ce qu'on apprend. À utiliser au début de chaque tâche (« fais une app », « fais l'onboarding », « la fiche App Store », « un nouveau site ») et chaque fois que l'humain corrige un agent.
---

# La mémoire d'abord

Une mémoire MCP garde des leçons courtes par sujet (des outils du type `lessons_read`, `lesson_add`, `lesson_revise`, `lesson_retire`). Les leçons renvoient au détail, dans ce playbook ou dans le dépôt du projet.

## Au début d'une tâche
1. Choisis l'espace de la mémoire (s'il y en a plusieurs, celui de la personne ou du projet).
2. Lis les leçons de chaque sujet de la tâche :

| Sujet | Quand |
|---|---|
| `work.agents` | toujours : comment travailler et rendre son travail |
| `app.create` | une nouvelle app |
| `app.onboarding` | l'onboarding, le paywall, le premier lancement |
| `app.aso` | la fiche App Store, les mots-clés, les captures |
| `app.store-release` | un envoi TestFlight ou App Store, la review |
| `web.create` | un nouveau site |

3. Ouvre la page que la leçon cite (son champ `source`).
4. Quand une leçon change ce que tu fais, dis-le en une ligne.

Sans mémoire MCP, lis directement [`../../memoire/lecons.json`](../../memoire/lecons.json).

## Pendant et à la fin
- L'humain te corrige ou demande une chose nouvelle sur sa façon de travailler : ajoute la leçon tout de suite.
- Si la leçon vaut pour tout le monde, ouvre aussi une PR qui l'écrit dans la page du sujet et dans `memoire/lecons.json`.
- Un fait de la vie de la personne (un projet, un budget, une machine) va dans une note de la mémoire, jamais dans ce dépôt.

## Une bonne leçon
- `rule` : une ou deux phrases à l'impératif, applicables sans l'histoire.
- `when` : le déclencheur qu'un agent reconnaîtra. `why` : la raison. `check` : comment vérifier.
- `source` : `playbook:<clé>` et la page du dépôt. La clé permet à `sync-memory` de retrouver la leçon.
- Pas de leçon pour un fait d'un jour (un id, l'état d'une PR).
