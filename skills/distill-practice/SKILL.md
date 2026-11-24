---
name: distill-practice
description: Extraire chaque jour, de toutes les sessions et de tous les fils d'agents, ce que la personne a demandé, partagé ou validé, et n'en garder que l'essentiel dans les skills et la mémoire. À lancer par une routine quotidienne, ou sur « reprends l'extraction », « mets à jour ma façon de travailler ».
---

# Distiller la façon de travailler

Le but : des skills qui s'améliorent tout seuls. Chaque nuit, un agent relit l'activité nouvelle et n'en garde que ce qui servira à un autre projet, dans un an. Pas un journal : le pur jus. La plupart des passages n'ajoutent rien, et c'est normal.

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

Jette ce qui ne sert qu'à la tâche du jour (un id, l'état d'une PR, un bug précis), ce qu'aucun signal ne valide, et ce que les skills ou la mémoire disent déjà.

## 4. Ce qui mérite d'entrer
Une consigne validée n'est pas encore une leçon. Ce dépôt garde un savoir de métier : le produit, le marketing, le texte, le design, le code, l'architecture, la façon de mener un travail. Une règle entre seulement si elle passe les quatre questions.

| Question | Si la réponse est non |
|---|---|
| Sera-t-elle encore vraie avec des modèles et des outils bien meilleurs ? | C'est un contournement d'aujourd'hui (« un dessin ne s'écrit pas en SVG », « écris ce nom en phonétique pour la voix »). Garde l'exigence qui est derrière (« le niveau du dessin de référence »), ou rien. |
| Servira-t-elle à un autre projet ? | C'est une règle du projet : une leçon de la mémoire, sous son sujet. |
| Dit-elle quelque chose du métier, et pas de la tuyauterie ? | Comment marche un fil, une tâche planifiée, une garde, un runner : ça change avec le produit. Dans la mémoire, ou rien. |
| Tient-elle sans l'incident qui l'a fait naître ? | Une erreur d'un jour se corrige, elle ne devient pas une règle. Attends qu'elle revienne. |

### Le principe, la mise en œuvre, le goût
Ce qu'on a fait dans un produit mélange trois choses. Sépare-les avant d'écrire.

| | Ce que c'est | Où ça va |
|---|---|---|
| **Le principe** | Le but et sa raison : « le moins de friction, parce que ce produit est une porte vers un système qui comprend » | Dans le skill, avec les questions qui permettent de trancher pour un autre produit |
| **La mise en œuvre** | La réponse d'un produit à ces questions : « un seul bouton + », « le aha à la 3e étape », « un essai de 7 jours » | Dans une étude de cas (`references/`), dite comme un exemple |
| **Le goût** | Ce que la personne aime et montre : une app, une animation, un créateur, un skill tiers | Dans `CREDITS.md`, avec ce qu'on en garde |

- Un skill qui ne donne que la mise en œuvre fait recopier. Un skill qui donne le principe et ses questions fait décider : l'agent doit pouvoir arriver à une autre réponse pour un autre produit.
- Cherche le « parce que » dans ce que la personne a dit. S'il manque, demande-le, ou range la règle en étude de cas.
- Un skill tiers dit déjà bien une chose ? Renvoie vers lui au lieu de le réécrire.
- Une règle qui dit seulement « fais ce que l'humain demande » n'apprend rien : jette-la.
- Un « jamais » vient souvent d'un seul refus. Écris ce que la personne voulait obtenir, pas le moyen qu'elle a refusé ce jour-là.
- Garde ce qui vient d'un humain : ce qu'il a dit, corrigé ou choisi, un article ou un skill qu'il a partagé. Jette ce qu'un agent a trouvé seul : le prochain modèle le refera pareil, ou mieux. Ce qui fait la qualité, c'est ce que l'humain apporte.
- Dans le doute, n'ajoute pas. Une règle faible coûte plus qu'une règle absente : chaque agent la lira à chaque tâche.

## 5. Distiller
- **Généralise.** « Les slideshows de tel réseau » devient une règle seulement si elle tient pour un autre projet. Sinon c'est une leçon du projet, dans la mémoire.
- **Une règle par idée**, à l'impératif, avec sa raison et comment vérifier (voir [`memory-first`](../memory-first/SKILL.md)).
- **Fusionne** avec l'existant au lieu d'ajouter à côté. Une règle qui en contredit une ancienne la remplace : la plus récente gagne, et tu le dis.
- **Une règle qui revient** dans plusieurs projets monte d'un cran : du projet vers un skill général.
- Garde la source de chaque élément (session, PR, date) dans le journal, jamais dans ce dépôt.

## 6. Ranger
| Quoi | Où |
|---|---|
| Une règle qui vaut pour tous les projets | Le skill général du sujet et sa leçon dans `memory/lessons.json`, sur une seule PR ouverte qui s'enrichit chaque jour |
| Une ressource | Le skill qui s'en sert, ou `CREDITS.md` |
| Une règle d'un projet, un contournement d'outil utile aujourd'hui | Une leçon de la mémoire, sous le sujet du projet |
| Un fait personnel | Une note de la mémoire, jamais ce dépôt |

- Le dépôt reste anonyme : relis le diff en cherchant un nom, un domaine, une machine.
- `python3 scripts/check-lessons.py` passe avant chaque push.
- Si la PR de la veille a été fusionnée, lance [`sync-memory`](../sync-memory/SKILL.md), puis repars d'une branche neuve.

## 7. Rendre
- Un journal du passage : chaque élément gardé (case, source, signal, où il est allé) et chaque élément jeté, avec la question qui l'a écarté.
- Un message de trois lignes au plus, seulement s'il y a du nouveau : ce qui a été ajouté, le lien de la PR, une question si une règle en contredit une autre.
- Rien de nouveau : une ligne, ou rien.

## Vérifier
- [ ] Chaque règle ajoutée a un signal de validation et passe les quatre questions.
- [ ] Le journal dit ce qui a été jeté, et à quelle question.
- [ ] Aucune règle n'existe deux fois.
- [ ] Le diff ne contient rien de personnel.
- [ ] Le filigrane est à jour.
