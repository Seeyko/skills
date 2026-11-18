---
name: work-with-agents
description: Comment travailler en agent autonome - quel modèle et quel agent pour quelle tâche, quand demander l'accord, comment mener une PR, prouver et rendre son travail. À lire au début de chaque tâche, dans tout projet, et quand on orchestre plusieurs agents ou fils.
---

# Travailler avec des agents

Le but : des agents autonomes. On lance la tâche depuis son téléphone, les agents font le reste et ne demandent que ce qu'ils ne peuvent ni trouver ni créer.

- Quel modèle, quel agent, quel découpage pour chaque type de tâche : [`references/orchestration.md`](references/orchestration.md).
- Les règles à copier dans le `CLAUDE.md` d'un projet : [`references/rules.md`](references/rules.md).

## L'essentiel
1. **Fais-le toi-même.** Par l'API, le CLI ou le navigateur. Jamais de copier-coller pour l'humain. Demande tous les accès en une fois, tôt.
2. **Pas de question dont la réponse est « l'option recommandée ».** Prends le défaut, dis-le en une ligne, continue.
3. **Le modèle le plus fort analyse, relit et tranche.** Un modèle de code code. Un petit modèle sert pour les sous-agents nombreux. Les noms des modèles changent : prends les plus récents.
4. **Un gros chantier, un projet** : un coordinateur, un fil par chantier.
5. **Attends l'accord écrit** pour une écriture en production, une suppression en masse, une dépense, tout ce qui sort du projet, et la fusion d'une PR qui touche la sécurité, le paiement, une migration, la CI ou un contrat d'API.
6. **Une PR par étape**, suivie jusqu'à un état final : fusionnée, verte et laissée au propriétaire, ou rouge avec un verdict. Jamais de fusion sur un rouge.
7. **Prouve** : des captures avant et après, une vidéo à vitesse réelle, des tests qui échoueraient sans la fonction.
8. **Rends ton travail** comme le dit [`present-work`](../present-work/SKILL.md).
9. **Garde ce que tu apprends** : chaque correction devient une règle dans le skill du sujet, avec sa raison, dans la même PR ([`memory-first`](../memory-first/SKILL.md)).
