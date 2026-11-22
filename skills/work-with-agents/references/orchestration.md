# Orchestrer les agents

Le but : des agents autonomes. Tu lances la tâche depuis ton téléphone ou ton ordinateur, les agents font tout le reste et ne te demandent que ce qu'ils ne peuvent pas trouver ou créer eux-mêmes.

## Quel modèle pour quoi
Les noms ci-dessous sont ceux d'aujourd'hui. Quand une nouvelle famille sort, garde les rôles et change les noms.
- **Le modèle le plus fort (Fable)** analyse, cherche, relit, conçoit et **tranche** les questions ouvertes. Un premier agent écrit le besoin en termes purement fonctionnels, puis un agent Fable conçoit la solution.
- **Opus** code, et fait les audits en parallèle (effort élevé).
- **Sonnet** sert pour les sous-agents nombreux et répétitifs (essayer de casser une app, trier une liste).

## Par type de tâche

| Tâche | Comment l'orchestrer |
|---|---|
| Un gros chantier produit (une app, un onboarding, l'ASO) | Un **projet Claude** : un coordinateur dans le chat, **un fil par chantier** (étude d'audience, onboarding, ASO, vidéo, TestFlight). Les fils se passent leurs résultats. Le fil qui code renvoie une étude au coordinateur, qui ouvre un fil dédié. |
| Une étude (audience, études de cas, concurrents) | Un agent Fable dédié ([`audience-researcher`](../../../agents/audience-researcher.md) pour l'audience), qui revient avec « ce qu'on garde, ce qu'on retire, ce qu'on améliore ». |
| Un regard neuf sur une référence (une vidéo, une app) | Deux analyses : la tienne, et un Fable qui n'a **que la matière brute**. Garde ce qui converge. |
| Relire un texte | Deux relecteurs Fable en parallèle, un par angle : [`copy-cutter`](../../../agents/copy-cutter.md) (la grille de suppression) et [`story-reviewer`](../../../agents/story-reviewer.md) (le récit et le ressenti). L'agent principal arbitre. |
| Une liste d'erreurs ou de bugs (analytique, issues) | Un sous-agent par erreur pour trier (vraie ou non, fermée avec un commentaire), puis un sous-agent par erreur pour corriger, le tout en workflow. |
| Plusieurs PR rouges | Un sous-agent Opus par PR pour la rendre verte. |
| Accélérer une CI, une migration technique | Un agent par techno, puis un autre agent relit chaque branche en cherchant ce qui casse. Petites PR, chiffres avant et après. |
| Un audit de design | Le skill `impeccable`, un agent Opus en lecture seule par écran, puis une PR présentée sans fusion. |
| Les annonces d'un fournisseur | Une session lit tout, puis lance une session et une PR par sujet utile. |
| Chercher les bugs chaque jour | Une routine quotidienne : des Sonnet tentent de casser l'app sur une pile complète (build de prod, API, vraie base), des Opus écrivent le correctif et le test, une PR par bug, lisible en une minute (titre qui dit le bug, captures, preuve). |
| Une infra qu'une session ne peut pas atteindre | Écrire un **runbook** dans la PR, puis le passer à un agent qui a les accès. |
| Un refus d'App Review | Une réponse point par point, par le CLI ou le navigateur, avec une vidéo de l'app en usage, ou des captures de l'appareil demandé et la liste des appareils testés. |
| Une tâche récurrente | Un projet Claude avec un déclencheur planifié (chaque semaine, chaque jour), ou une routine. Une veille tourne au plus toutes les 3 h : plus souvent, elle dérange. Elle ne parle que s'il y a du nouveau. |
| Veiller sur la branche principale | « Vert » veut dire **déployé** : la routine juge le run du commit de tête **et** le deploy. Un e2e annulé ou un vieux run vert ne compte pas. |
| Un nouveau format vu ailleurs (un post, une pub) | Un fil d'exploration autonome qui cherche, prototype seul et montre tout avant de publier ([`social-content`](../../social-content/SKILL.md)). |
| Garder la méthode à jour | Une routine quotidienne [`distill-practice`](../../distill-practice/SKILL.md) relit les fils et range ce qui a été demandé ou validé. |
| Une analyse sans action | Seulement un document d'analyse. Pas de PR. Un plan ou une analyse ne se fusionne jamais tout seul. |

## Le suivi d'une PR
- Le titre et la description suivent [`present-work`](../../present-work/SKILL.md) : lisibles par un chef de produit, captures d'abord.
- L'agent qui ouvre une PR la suit jusqu'à un état final : **fusionnée**, **verte et laissée au propriétaire**, ou **rouge avec un verdict**. Puis il se désabonne et s'arrête.
- Petite PR verte : l'agent la fusionne (squash). Une surface sensible (paiement, sécurité, migration, CI, contrat d'API mobile) ou un plan : « prête pour relecture ».
- **Une PR en cours par auteur.** Les branches finies pendant ce temps attendent, puis partent ensemble en lot dès qu'elle passe, automatiquement.
- Une relance par panne d'infra. Deuxième panne : un verdict, pas de boucle.

## Les machines
- Une machine toujours allumée (un Mac pour iOS) fait les builds, le simulateur, App Store Connect et les runners de CI. Une session à distance y tourne en permanence, pour lui parler depuis le téléphone.
- Les sessions cloud codent. Elles n'écrivent jamais en production : une écriture en prod passe par la machine qui a les accès, avec l'accord écrit du propriétaire.
- Une étape d'installation de la CI a un plafond court (quelques minutes) : un runner bloqué échoue vite au lieu d'attendre une heure. Sur un runner macOS sans écran, les caches restent sur le disque interne : une autorisation système jamais validée bloque un job en silence.
- Une consigne nouvelle part à tous les fils qu'elle touche, routines comprises, et chaque fil met à jour ses tâches planifiées lui-même. Si la mise à jour est refusée, recrée la tâche sous le même nom ; ne la supprime jamais sans le dire, son historique part avec.
- Un fil ne peut pas changer une tâche planifiée qu'il n'a pas créée : il écrit le nouveau texte dans un fichier partagé et le demande au coordinateur.
- Un fil reçoit ses connecteurs avant sa tâche.
- Tous les accès d'administration passent par un réseau privé (Tailscale ou équivalent).

## La preuve
Des captures avant et après, une vidéo à vitesse réelle, un seul essai d'abord pour un travail payant : voir [`design-interface`](../../design-interface/SKILL.md) et [`present-work`](../../present-work/SKILL.md).

## Garder ce qu'on apprend
- Chaque correction devient une règle dans le skill, la règle ou le `DESIGN.md` du sujet, avec sa raison, dans la même PR.
- Les fils d'un projet déposent leurs leçons en cours dans un fichier partagé par sujet, puis les rangent dans le skill à la fin de la PR.
- Une mémoire MCP garde les leçons courtes (voir [`../../../memory/`](../../../memory/README.md)).
