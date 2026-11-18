---
name: new-mobile-app
description: Démarrer une nouvelle app iOS, de l'idée à la première version sur l'App Store, avec un onboarding et une fiche de première classe. À utiliser pour « crée une app », « fais une app avec un onboarding », « nouvelle app mobile », ou quand on ajoute un client iOS à un projet.
---

# Une nouvelle app mobile

Avant tout : skill [`memory-first`](../memory-first/SKILL.md) (sujets `work.agents`, `app.create`, puis celui de chaque étape). Lis aussi [`work-with-agents`](../work-with-agents/SKILL.md) et [`pick-stack`](../pick-stack/SKILL.md).

## 1. Décider vite
- **Une phrase fixe tout** : l'app, le public, la stack, l'hébergement. Pose seulement les questions dont tu ne peux pas trouver la réponse, toutes ensemble, au début.
- **Une maquette d'abord** : une page HTML jouable, essayée sur un téléphone. L'app suit la maquette exactement.
- **Une conception courte, puis un go** : le modèle de données, l'écran, le geste, les budgets de performance, les questions ouvertes. Pas de code avant le go.
- **Pour qui ?** L'étude d'audience d'abord ([`audience-study`](../audience-study/SKILL.md)).
- **L'interface** suit [`design-interface`](../design-interface/SKILL.md) (une app minimale, le design par le modèle le plus fort), **le texte** suit [`write-copy`](../write-copy/SKILL.md).

## 2. Le dépôt
Pars de [`../../templates/mobile-app/`](../../templates/mobile-app/) : `CLAUDE.md`, `DESIGN.md`, `.claude/rules/front.md`, `SECRETS.md`.
- SwiftUI (iOS 17 au moins, iOS 26 et Liquid Glass si possible), Swift 6, XcodeGen. Le `.xcodeproj` regénéré est commité avec le `project.yml`.
- Une API minimale (Bun + Hono, Postgres si besoin) sur un VPS. Les clés d'IA restent sur le serveur, derrière une passerelle (Cloudflare AI Gateway).
- PostHog EU, un projet pour toutes les apps du compte, avec une propriété `app`. Aucune donnée de santé.
- Pas de commentaire dans le code, pas de code mort, pas de « version 2 ». Une seule branche `main` égale à la prod.
- Les budgets : ouverture en moins de 100 ms, un geste en une frame. Mesurés par des signposts.
- Aucun secret dans le dépôt : `SECRETS.md` nomme les variables et dit où elles vivent.

## 3. Construire
- Une PR par étape. Fusion quand la CI est verte, sauf une surface sensible ([`work-with-agents`](../work-with-agents/SKILL.md), point 5).
- Les builds iOS se font sur le Mac de build, un seul à la fois, avec `nice`, sur le disque externe. Une session cloud code à l'aveugle et passe la main au Mac.
- Installe l'app sur un vrai iPhone dès le premier build (Wi-Fi, puis TestFlight). On la juge sur l'usage réel, l'entrée naturelle d'abord.
- La suppression du compte et la déconnexion sont prévues dès la première conception (Apple 5.1.1(v)).
- **L'onboarding** : skill [`app-onboarding`](../app-onboarding/SKILL.md), en entier. Il passe avant la première review.
- **Le paywall** (app payante) : skill [`app-paywall`](../app-paywall/SKILL.md).

## 4. Sortir
- Avant le premier envoi, relis les raisons de refus déjà vues (garde-les dans un skill `app-store-release` du projet, et ajoutes-y chaque nouveau refus).
- La fiche : skill [`app-store-optimization`](../app-store-optimization/SKILL.md). Les captures, l'en-tête et l'image de recherche sont prêts avant la review.
- Tout passe par le CLI `asc` ou l'API App Store Connect, en dernier recours par le navigateur. Jamais un copier-coller pour l'humain.
- TestFlight : un groupe interne, un groupe externe de proches. Les proches testent pendant la review. On ne casse pas une review en cours pour un petit correctif.
- Un refus d'App Review : réponds point par point, par le CLI ou le navigateur, avec une vidéo de l'app en usage ou des captures de l'appareil demandé (iPad), et dis sur quoi tu as testé.
- Le code d'un build envoyé au store est sur `main`. Préviens à chaque sortie.

## 5. Après la sortie
- Les retours des testeurs se discutent, ils ne s'appliquent pas tels quels.
- L'analytique décide de la suite de l'onboarding (le funnel écran par écran).
- Ce que l'app t'a appris va dans le skill du sujet et dans `memory/lessons.json`, dans la même PR.
