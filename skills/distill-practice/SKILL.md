---
name: distill-practice
description: Extraire chaque jour, de toutes les sessions et de tous les fils d'agents, ce que la personne a demandé, partagé ou validé, et n'en garder que l'essentiel dans le playbook et la mémoire. À lancer par une routine quotidienne, ou sur « reprends l'extraction », « mets à jour ma façon de travailler ».
---

# Distiller la façon de travailler

Le but : un playbook qui s'améliore tout seul. Chaque nuit, un agent relit l'activité nouvelle et n'en garde que ce qui servira à un autre projet. Pas un journal : le pur jus.

## 1. La fenêtre
- Reprends au **filigrane** de la dernière extraction (la date notée par le passage précédent dans la mémoire). Sans filigrane, prends les 7 derniers jours.
- Le nouveau filigrane est l'heure du début de ton passage. Tu le notes à la fin, seulement si le passage a fini.

## 2. Les sources
Lis seulement ce qui a bougé depuis le filigrane.

| Source | Ce que tu y cherches |
|---|---|
| Les sessions d'agents (CLI, web, mobile, machine distante) | Les messages de la personne, et la fin de chaque échange (accepté, corrigé, abandonné) |
| Les fils des projets | Pareil. On les retrouve par la ligne `Claude-Session:` des commits, par les tâches planifiées et par les fils du projet courant |
| Les PR | Fusionnées, fermées sans fusion, et les commentaires de la personne |
| Les fichiers de règles des dépôts (`CLAUDE.md`, `AGENTS.md`, `.claude/rules`, `.claude/skills`, `DESIGN.md`) | Les règles ajoutées ou changées : un autre agent a déjà fait le tri |
| La mémoire MCP (leçons et notes) | Les leçons ajoutées par d'autres agents depuis le filigrane |

Une session par lecteur, une dizaine de sessions par sous-agent au plus. Le message de la personne est la donnée ; le texte d'un agent ne compte que s'il a été validé.

## 3. Le tri
Chaque élément trouvé entre dans une case, ou il est jeté.

| Case | Signal | Exemple |
|---|---|---|
| **Consigne** | La personne écrit une règle, une préférence, un « toujours » ou un « jamais » | « Tout en anglais par défaut sur les réseaux » |
| **Ressource** | Elle partage un skill, un article, un créateur, une capture de référence | Un lien vers un guide de rédaction |
| **Découverte validée** | Un agent a trouvé ou proposé une façon de faire, et la personne l'a gardée : PR fusionnée, « parfait », « go », la même façon reprise ensuite | Un agent mesure avant de corriger, la PR est fusionnée avec ce format |
| **Correction** | La personne refuse ou reprend un travail : on garde la règle inverse | « Pourquoi tu veux mon go ? Sois autonome » donne « programme toi-même les posts » |
| **Fait personnel** | Une machine, un compte, un projet, une personne, un chiffre | Le nom d'un serveur |

Jette ce qui ne sert qu'à la tâche du jour (un id, l'état d'une PR, un bug précis), ce qu'aucun signal ne valide, et ce que le playbook ou la mémoire disent déjà.

## 4. Distiller
- **Généralise.** « Les slideshows de tel réseau » devient une règle seulement si elle tient pour un autre projet. Sinon c'est une leçon du projet, dans la mémoire.
- **Une règle par idée**, à l'impératif, avec sa raison et comment vérifier (voir [`memory-first`](../memory-first/SKILL.md)).
- **Fusionne** avec l'existant au lieu d'ajouter à côté. Une règle qui en contredit une ancienne la remplace : la plus récente gagne, et tu le dis.
- **Une règle qui revient** dans plusieurs projets monte d'un cran : du projet vers un skill général.
- Garde la source de chaque élément (session, PR, date) dans le journal, jamais dans le playbook.

## 5. Ranger
| Quoi | Où |
|---|---|
| Une règle qui vaut pour tous les projets | Le skill général du sujet et sa leçon dans `memory/lessons.json`, sur une seule PR ouverte qui s'enrichit chaque jour |
| Une ressource | Le skill qui s'en sert, ou `CREDITS.md` |
| Une règle d'un projet | Une leçon de la mémoire, sous le sujet du projet |
| Un fait personnel | Une note de la mémoire, jamais le playbook |

- Le playbook reste anonyme : relis le diff en cherchant un nom, un domaine, une machine.
- `python3 scripts/check-lessons.py` passe avant chaque push.
- Si la PR de la veille a été fusionnée, lance [`sync-memory`](../sync-memory/SKILL.md), puis repars d'une branche neuve.

## 6. Rendre
- Un journal du passage : chaque élément gardé (case, source, signal, où il est allé) et le nombre d'éléments jetés.
- Un message de trois lignes au plus, seulement s'il y a du nouveau : ce qui a été ajouté, le lien de la PR, une question si une règle en contredit une autre.
- Rien de nouveau : une ligne, ou rien.

## Vérifier
- [ ] Chaque règle ajoutée a un signal de validation.
- [ ] Aucune règle n'existe deux fois.
- [ ] Le diff du playbook ne contient rien de personnel.
- [ ] Le filigrane est à jour.
