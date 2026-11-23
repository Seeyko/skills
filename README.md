# Skills

Des skills pour construire des apps mobiles et des sites avec des agents Claude. Le dépôt est rangé comme un plugin : des **skills** (une tâche chacun, avec ses `references/`), des **agents** prêts à lancer, des **modèles** de départ et des **leçons** courtes pour une mémoire. Il se suffit à lui-même : clone-le et utilise-le tel quel.

## Pour démarrer
1. Copie les skills et les agents qui te servent dans le `.claude/` de ton projet, ou ajoute ce dépôt comme source de skills.
2. Pour une nouvelle app, lance [`new-mobile-app`](skills/new-mobile-app/SKILL.md). Pour un site, [`new-website`](skills/new-website/SKILL.md).
3. Si tu as une mémoire MCP qui garde des leçons, charge-y [`memory/lessons.json`](memory/lessons.json) avec [`sync-memory`](skills/sync-memory/SKILL.md).

## Les skills

**Pour tout projet**

| Skill | Quand |
|---|---|
| [`work-with-agents`](skills/work-with-agents/SKILL.md) | Au début de chaque tâche : quel agent pour quoi, l'accord, les PR, la preuve |
| [`present-work`](skills/present-work/SKILL.md) | Chaque fois qu'un travail est fini |
| [`write-copy`](skills/write-copy/SKILL.md) | Tout texte qu'une personne lira : la règle des 75 %, les mots de la personne, les promesses |
| [`design-interface`](skills/design-interface/SKILL.md) | Tout écran, toute animation, tout visuel |
| [`audience-study`](skills/audience-study/SKILL.md) | Avant d'écrire pour quelqu'un : un produit, un onboarding, une fiche, un site |
| [`pick-stack`](skills/pick-stack/SKILL.md) | Au démarrage d'un projet, ou avant d'ajouter un service |
| [`social-content`](skills/social-content/SKILL.md) | Les posts réseaux : slideshows, vidéos d'app, vidéos de jeu, UGC, musique, CTA, formats gagnants |
| [`seo-content`](skills/seo-content/SKILL.md) | Un article, un comparatif, le référencement un pas par jour, les citations par les IA |
| [`product-analytics`](skills/product-analytics/SKILL.md) | Ce qu'on trace : l'onboarding, le paywall, les abonnements, l'acquisition |
| [`beta-by-sharing`](skills/beta-by-sharing/SKILL.md) | Une fonction nouvelle sort en bêta et se diffuse par le partage |
| [`memory-first`](skills/memory-first/SKILL.md), [`sync-memory`](skills/sync-memory/SKILL.md) | Lire et tenir à jour les leçons d'une mémoire MCP |
| [`distill-practice`](skills/distill-practice/SKILL.md) | Chaque jour, extraire des fils ce qui a été demandé ou validé, et le ranger ici |

**Pour chaque étape d'une app**

| Étape | Skill |
|---|---|
| 1. Démarrer l'app | [`new-mobile-app`](skills/new-mobile-app/SKILL.md) |
| 2. L'onboarding | [`app-onboarding`](skills/app-onboarding/SKILL.md) |
| 3. Le paywall | [`app-paywall`](skills/app-paywall/SKILL.md) |
| 4. La fiche App Store | [`app-store-optimization`](skills/app-store-optimization/SKILL.md) |
| Le site de l'app | [`new-website`](skills/new-website/SKILL.md) |

## Les agents
- [`audience-researcher`](agents/audience-researcher.md) mène l'étude d'audience.
- [`copy-cutter`](agents/copy-cutter.md) et [`story-reviewer`](agents/story-reviewer.md) relisent un texte en parallèle, l'un par la grille de suppression, l'autre par le récit.

## Le reste
- [`templates/`](templates/README.md) : le `CLAUDE.md`, le `DESIGN.md` et les fichiers de départ d'une app et d'un site.
- [`memory/`](memory/README.md) : les leçons courtes, une par règle, qui renvoient au skill.
- [`CREDITS.md`](CREDITS.md) : les skills tiers et les créateurs.

## Améliorer ces skills
0. Vérifie que la règle a sa place ici : un savoir de métier qui dure, pas un contournement d'aujourd'hui ni la suite d'un incident ([`distill-practice`](skills/distill-practice/SKILL.md), « Ce qui mérite d'entrer »).
1. Écris la règle dans le skill du sujet, avec sa raison. Une règle qui vaut partout va dans un skill général, pas dans celui d'une étape.
2. Dans la même PR, ajoute, change ou retire la leçon qui correspond dans [`memory/lessons.json`](memory/lessons.json). `python3 scripts/check-lessons.py` vérifie le fichier (aussi en CI).
3. Après la fusion, lance [`sync-memory`](skills/sync-memory/SKILL.md).
