# Agent playbook

Une façon de construire des apps mobiles et des sites avec des agents Claude (Claude Code, projets, sous-agents). Ce dépôt contient la méthode, les règles, la stack, des skills prêts à copier et des modèles de départ. Il se suffit à lui-même : tu peux le cloner et l'utiliser tel quel.

## Pour démarrer

1. Copie les skills qui te servent dans le `.claude/skills/` de ton projet, ou ajoute ce dépôt comme source de skills.
2. Pour une nouvelle app, pars de [`templates/mobile-app/`](templates/mobile-app/) et du skill [`new-mobile-app`](skills/new-mobile-app/SKILL.md). Pour un site, pars de [`templates/website/`](templates/website/) et du skill [`new-website`](skills/new-website/SKILL.md).
3. Si tu as un MCP de mémoire qui garde des leçons (des outils du type `lessons_read`, `lesson_add`), charge-y les leçons de [`memoire/lecons.json`](memoire/lecons.json) avec le skill [`sync-memory`](skills/sync-memory/SKILL.md). Tes agents les liront au début de chaque tâche ([`memory-first`](skills/memory-first/SKILL.md)).

## Ce qu'il y a dedans

| Tu veux… | Lis |
|---|---|
| Savoir quel agent lancer pour quelle tâche, et comment le piloter | [`methode/orchestration.md`](methode/orchestration.md) |
| Les règles à donner aux agents (autonomie, PR, tests, texte, sécurité) | [`methode/regles.md`](methode/regles.md) |
| Une stack simple et peu chère pour des apps et des sites | [`methode/stack.md`](methode/stack.md) |
| Les skills tiers utiles par tâche, et les créateurs à suivre | [`methode/skills-et-createurs.md`](methode/skills-et-createurs.md) |
| Les principes de design, de texte et de vidéo | [`methode/gout.md`](methode/gout.md) |
| Présenter un travail fini (PR, rapport) | skill [`present-work`](skills/present-work/SKILL.md) |
| Faire l'onboarding et le paywall d'une app | skill [`app-onboarding`](skills/app-onboarding/SKILL.md) |
| Faire la fiche App Store (ASO) | skill [`app-store-optimization`](skills/app-store-optimization/SKILL.md) |
| Démarrer une app mobile | skill [`new-mobile-app`](skills/new-mobile-app/SKILL.md) et [`templates/mobile-app/`](templates/mobile-app/) |
| Démarrer un site | skill [`new-website`](skills/new-website/SKILL.md) et [`templates/website/`](templates/website/) |
| Des références à regarder | [`exemples/`](exemples/README.md) |
| Garder les leçons dans une mémoire MCP | [`memoire/`](memoire/README.md) |

Les skills sont au format Claude Code (`skills/<nom>/SKILL.md`, avec leurs `references/`).

## Améliorer le playbook

Quand tu trouves une meilleure façon de faire :

1. Écris-la dans le skill ou la page du sujet, avec sa raison.
2. Dans la même PR, ajoute, change ou retire la leçon courte qui correspond dans [`memoire/lecons.json`](memoire/lecons.json). `python3 scripts/check-lecons.py` vérifie le fichier (aussi en CI).
3. Après la fusion, lance [`sync-memory`](skills/sync-memory/SKILL.md) pour que ta mémoire MCP suive.
