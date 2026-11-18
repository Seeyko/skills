---
name: new-website
description: Démarrer un nouveau site (site d'app, landing page, page statique, outil web) jusqu'à sa mise en ligne sur un sous-domaine. À utiliser pour un site, une landing, une page de confidentialité ou de support d'app, ou pour migrer un site depuis Vercel ou Supabase.
---

# Un nouveau site

Avant tout : skill [`memory-first`](../memory-first/SKILL.md) (sujets `work.agents`, `web.create`).

## 1. Choisir le plus simple
- **Statique d'abord** : du HTML et du CSS, sans build si possible. GSAP pour l'animation quand il le faut.
- Une app web : React + Vite + Tailwind 4 + shadcn. Une API Bun + Hono + Drizzle + Postgres.
- Un VPS avec Dokploy plutôt que Vercel et Supabase : moins cher, tout au même endroit.
- Une phrase fixe souvent tout (où héberger, quoi réécrire, le domaine). Si une pièce manque, demande tout en une fois.

## 2. Le dépôt
Pars de [`../../templates/website/`](../../templates/website/) : un `Dockerfile` nginx, une conf nginx, un `CLAUDE.md`.
- Une branche, une PR. Une fusion sur `main` déploie en prod.
- Le design suit l'univers de l'app (son `DESIGN.md`) ou un thème fort. Pas de « site IA » : pas d'eyebrow, pas de cartes partout, un seul CTA par écran.
- Le texte passe par `humanizer` (ou le skill de wording du projet), FR et EN.
- Vérifie dans un vrai navigateur (Playwright, Chrome MCP), sur téléphone et sur ordinateur, avec des captures avant et après.

## 3. Mettre en ligne
- Dokploy sur le VPS : une application par site, le domaine branché dans Dokploy, HTTPS par Let's Encrypt.
- DNS : un sous-domaine du domaine principal, changé par le CLI ou l'API du registrar après un instantané de la zone. Jamais à la main.
- Cloudflare : R2 pour les médias lourds, Turnstile pour un formulaire.
- PostHog EU pour l'analytique, sans donnée personnelle dans les URL.
- Une page de confidentialité qui dit exactement ce que fait le site ou l'app, mise à jour à chaque changement. Une page de support pour une app iOS (l'App Store la demande).
- Une session cloud n'atteint pas la prod : le déploiement passe par la machine qui a les accès, ou par un runbook écrit dans la PR qu'un agent du serveur exécute.

## 4. Après
- SEO : `seo-audit`, `ai-seo` (Corey Haines), un `sitemap.xml`, des balises Open Graph avec une image de la marque.
- Si tu as un portfolio, ajoutes-y le site, ou marque « archivé » celui qu'on remplace.
