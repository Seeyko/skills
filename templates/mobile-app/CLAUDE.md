# <Nom de l'app>

<Une phrase : ce que fait l'app, pour qui, payante ou non.> FR + EN. Bundle `<app.nom.ios>`, équipe `<team id>`. Dépôt privé `<owner/repo>`.

## Avant toute tâche
- Si une mémoire MCP est branchée, lis ses leçons `work.agents`, `copy`, `design`, `app.create` et celles du sujet de la tâche (`app.onboarding`, `app.paywall`, `app.aso`, `app.store-release`).

## Le dépôt

| Dossier | Contenu |
|---|---|
| `ios/` | l'app (SwiftUI, Swift 6, XcodeGen : `cd ios && xcodegen generate -q`). Tests dans `ios/<App>Tests`. |
| `api/` | l'API minimale (Bun + Hono), déployée sur Dokploy |
| `web/` | le site de l'app : présentation, confidentialité, support |
| `DESIGN.md`, `.claude/` | le système de design, la règle qui le charge pour le front, les skills |

## Les règles
- **Mac de build partagé** : on code à l'aveugle. Un seul build et un seul simulateur à la fois, à la fin, avec `nice`, sur le disque externe.
- **Aucun secret dans le dépôt.** `SECRETS.md` dit où vit chaque clé.
- **Confidentialité** : <ce que promet la politique>. Aucune donnée de santé ou personnelle dans PostHog. Toute évolution qui y touche se répercute dans `web/www/confidentialite`.
- **Une PR par étape**, merge quand la CI est verte, sauf une PR qui touche la sécurité, le paiement, une migration, la CI ou le contrat d'API : elle attend l'accord écrit. Le code d'un build envoyé au store est sur `main`.
- **Présente chaque travail fini** pour un non-technique : un titre humain, une description courte, des captures ou un diagramme, puis le lien vers le détail (skill `present-work`).
- **Pas de commentaire dans le code, pas de code mort.**
- **Outils** : le CLI `asc` pour App Store Connect, le MCP Moonjar pour les captures, PostHog EU.

## Charte de design
**L'écran parle tout seul.** Si on doit l'expliquer avec une phrase, on corrige le dessin, pas la phrase.
- Un écran = un titre et, seulement si c'est indispensable, une ligne courte. Jamais d'eyebrow, de sous-titre gris, de paragraphe d'aide.
- Le détail existe, mais derrière un tap.
- Un bouton dit l'action, et s'il le faut la durée.
- Les mots de la personne, pas ceux de l'app. Tutoiement, phrases de 20 mots au plus.
- Une seule chose mise en avant par écran. Un seul CTA.
- Chaque bouton et chaque choix se sent (haptique).
- Avant de livrer un écran : cacher chaque texte avec le doigt ; regarder en vraie taille en FR et en EN ; vérifier les cibles de 44 pt et VoiceOver.
