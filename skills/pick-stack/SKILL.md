---
name: pick-stack
description: Choisir la stack, l'hébergement et les services d'un nouveau projet (app iOS, app iOS + web, plateforme, site), et savoir quelle machine fait quoi. À utiliser au démarrage d'un projet, avant d'ajouter un service, ou pour migrer depuis Vercel ou Supabase.
---

# La stack

Une stack de développeur solo : peu chère, auto-hébergée quand c'est simple, et que les agents savent piloter par API ou CLI. Aucun secret ici : ils vivent sur les machines (fichiers `chmod 600`) ou dans l'environnement des services.

## Les machines

| Machine | Rôle |
|---|---|
| **Un Mac toujours allumé** (un Mac mini suffit) | Builds iOS, Xcode, simulateur, App Store Connect (CLI et API), runners GitHub Actions auto-hébergés, session à distance permanente, navigateur connecté. **Un seul build et un seul simulateur à la fois**, avec `nice`, quand la charge est basse. |
| **Un SSD externe** sur le Mac | Tout ce qui est lourd : VM docker, caches (go, bun, npm, gradle, cocoapods, swiftpm, playwright), DerivedData, worktrees, résultats de tests, médias générés. Le disque interne se remplit vite. |
| **Un VPS avec Dokploy** | Les side-projects : API, sites statiques, page de statut, outils auto-hébergés (planification de posts, mail, wiki). Lire est libre, écrire en prod demande l'accord écrit. |
| **Un VPS dédié à la prod** d'un projet qui compte | Son runner de déploiement non-root, ses sauvegardes sur un stockage objet. |
| **Tailscale** | Tous les accès d'administration. |

## Les services

| Besoin | Outil |
|---|---|
| Hébergement | Dokploy sur un VPS (plutôt que Vercel et Supabase : moins cher, tout au même endroit) |
| DNS, domaines | Le registrar, piloté par son CLI ou son API après un instantané de la zone, jamais à la main. Un sous-domaine par app. |
| CDN, stockage, sécurité | Cloudflare : R2 (médias, sauvegardes), Turnstile (formulaires), AI Gateway (devant les fournisseurs d'IA), Workers AI |
| Paiement | Stripe (Connect pour une place de marché) ; StoreKit 2 et abonnements App Store pour iOS |
| Analytique, erreurs, drapeaux | PostHog (région EU), un projet pour toutes les apps d'un compte, aucune donnée de santé |
| E-mails transactionnels | Resend |
| IA | Anthropic (Claude) ; Mistral pour l'OCR, la vision, la modération et la dictée (Voxtral) ; fal pour les images (par MCP, un essai d'abord) |
| Réseaux sociaux | Une file de posts branchée en MCP (brouillon par défaut) pour programmer ; construire en public sur X |
| Captures et vidéos App Store | Moonjar (MCP), Playwright, Cap à 60 fps pour les vidéos d'écran |
| App Store Connect | Le CLI `asc` de rudrank, l'API (clé `.p8` dans un fichier local), le navigateur en dernier recours |
| La mémoire des agents | Un MCP de mémoire qui garde des leçons par sujet (voir [`../../memory/`](../../memory/README.md)) |

## Les stacks par type de projet

| Projet | Stack |
|---|---|
| App iOS | SwiftUI (iOS 17 au moins, iOS 26 et Liquid Glass si possible), Swift 6, XcodeGen. Une API minimale si besoin. |
| App iOS + web | Monorepo Bun : API Hono + Drizzle + Postgres (PGlite en test), PWA Vite + React + shadcn, client iOS SwiftUI, logique partagée sur le serveur ou dans un moteur commun avec son port Swift. |
| Plateforme web + mobile | API Go, web React + Vite + Tailwind 4 + shadcn, mobile Flutter, Postgres. Tests e2e Playwright fullstack, intégration, golden. Lint Oxlint (avec anti-slop), oxfmt, tsgo. |
| Site vitrine | HTML et CSS statiques sans build, GSAP si besoin, nginx en Docker. |

## Les conventions de déploiement
- Une fusion sur `main` déploie en prod. Le code d'un build envoyé au store est sur `main`.
- Une branche `experimentation` qui se déploie seule sur une copie isolée et anonymisée de la prod, pour tester en ligne.
- CI sur les runners auto-hébergés, workflows découpés par chemins. Une PR reste rapide (une dizaine de minutes). La CI se traite comme un produit : on mesure sur des centaines de runs, on retire du travail (cache, doublons) avant d'ajouter des machines, et on ne desserre jamais le contrôle pour aller plus vite.
- TestFlight : un groupe interne (toi), un groupe externe (tes proches), un lien public limité si besoin. Les proches testent pendant la review d'Apple.
- Plusieurs comptes Apple (perso, société) peuvent cohabiter sur le Mac, chacun avec ses certificats.
