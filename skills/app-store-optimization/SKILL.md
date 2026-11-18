---
name: app-store-optimization
description: Écrire et optimiser la fiche App Store d'une app (nom, sous-titre, mots-clés, captures et légendes, en-tête, description, pages produit personnalisées, événements, codes d'offre), trouver les premiers utilisateurs sans pub, puis suivre la fiche après la sortie. À utiliser pour « ASO », « fiche App Store », « captures », « mots-clés », « en-tête », « conversion de la fiche », ou avant la première soumission d'une app.
---

# La fiche App Store (ASO)

Un plan complet, avec ses tableaux de mots-clés et son calendrier, est dans [`references/plan-aso.md`](references/plan-aso.md). Le gabarit de la page de suivi est dans [`references/suivi-fiche.md`](references/suivi-fiche.md).

## Avant de commencer
1. Si une mémoire MCP est branchée, lis ses leçons `app.aso` et `app.store-release` (skill [`memory-first`](../memory-first/SKILL.md)).
2. Lis l'étude d'audience de l'app (skill [`app-onboarding`](../app-onboarding/SKILL.md), étape 1) : la fiche parle avec ses mots.
3. Les skills de copy : `humanizer`, les marketingskills de Corey Haines (`aso`, `copywriting`, `marketing-psychology`), les règles de [`../app-onboarding/references/copy.md`](../app-onboarding/references/copy.md).

## Les principes
1. **La fiche fait vivre le moment aha avant le téléchargement.** La personne doit s'y voir en train de réussir, en mieux. Un chat doit se sentir tigre. La fiche montre la personne qu'elle va devenir, pas l'interface.
2. **Quatre leviers ensemble** : la fiche qui fait se voir réussir, une direction artistique qui se démarque, des mots-clés qui font remonter dans la recherche, et un onboarding réussi derrière.
3. **Tout par l'API ou le CLI.** Le CLI `asc` de rudrank et l'API App Store Connect, depuis la machine qui a la clé. Jamais de « colle ça dans App Store Connect » pour l'humain.
4. **Utilise les nouveautés d'App Store Connect** : en-tête image ou vidéo 21:9, image des résultats de recherche, bibliothèque d'éléments, pages produit personnalisées liées à des mots-clés, tests de page produit, événements in-app, codes d'offre, nominations, messages de rétention. Va voir ce qui est sorti depuis la dernière fois (WWDC, notes d'Apple) et suis-le.
5. **Une promesse vraie.** Les légendes et la description promettent le ressenti et l'accompagnement, jamais un résultat médical. Elles ne promettent que ce que le build fait (Apple refuse pour 2.3.1 sinon).
6. **Suis la fiche dans une page tenue à jour** : une colonne par version et par langue, les captures, l'en-tête, les pages perso, les chiffres, un journal. Un relevé automatique deux fois par semaine ([`references/suivi-fiche.md`](references/suivi-fiche.md)).
7. **Préviens à chaque sortie**, et dis clairement à l'humain s'il a quelque chose à faire, ou qu'il n'a rien à faire.

## Les champs (limites Apple)
Nom 30, sous-titre 30, texte promotionnel 170, mots-clés 100 octets (virgules, sans espace, un accent compte 2 octets), description 4 000.
- **Nom** : le mot cherché + la marque (« Périnée - <Marque> », « <Brand>: Pelvic Floor »).
- **Sous-titre** : à qui et quand, pas un slogan (« Grossesse et post-partum »). Ne répète pas un mot du nom : Apple ne compte un mot qu'une fois. Un mot réglementé sort du texte visible et reste dans les mots-clés cachés.
- **Mots-clés** : aucun mot déjà dans le nom ou le sous-titre, aucun concurrent, le singulier ou le pluriel mais pas les deux. **Chaque pays lit d'autres langues que la sienne** : la France lit aussi la fiche anglaise (Royaume-Uni). Écris ses mots-clés **en français** pour gagner 100 octets. Crée en-GB, en-AU, en-US et fr-CA même sans traduction complète.
- **Texte promotionnel** : part de son doute. « Tu serres sans savoir si c'est le bon muscle ? Une voix douce te guide, 7 minutes par jour, pendant la grossesse et après bébé. Essaie 7 jours. » Il change sans nouvelle version.
- **Description** : la première phrase dit quoi, pour qui, comment. La dernière garde la mention bien-être si l'app touche à la santé. La recherche ne la lit pas.
- La popularité d'un mot se lit dans Apple Ads (de 5 à 100), même sans lancer de campagne. Sans ce compte, juge sur les impressions réelles dans App Store Connect.

## Les captures
- Générées par un script, jamais à la main : des données de démonstration, un gabarit, un titre par capture (Playwright sur une page HTML sans build, ou des tests UI et un gabarit).
- **Un seul titre par capture**, avec un mot mis en valeur. L'univers de l'app en plein cadre, le téléphone petit et incliné. **Jamais de paywall ni de prix.**
- Apple lit les légendes pour la recherche, et la plupart des gens ne dépassent pas la 3e capture : les trois premières portent les mots qu'on veut indexer. Exemple : 1 « Sens ton périnée. *Enfin.* » 2 « *7 minutes* par jour. Une voix te guide, tu suis. » 3 « Pendant la grossesse ou après bébé, *à ton rythme* » 4 « Tu vois quel muscle serrer. *Sans sonde.* » 5 « Tu serres vite, la grenouille *saute* » 6 « Tu vas y arriver, *un jour après l'autre* » 7 « Pour te sentir à nouveau *toi* ».
- Retire ce qui se lit comme une promesse de résultat (une courbe « les fuites » qui baisse, par exemple).
- Envoi par l'API : `appScreenshotSets`, réservation, envoi des parts, validation MD5.

## L'en-tête et l'image de recherche
- En-tête 3840 × 1646 (21:9), image ou vidéo muette en boucle de 5 à 30 s ; résultat de recherche 3840 × 2560 (3:2). Par l'API : la bibliothèque d'éléments, puis les placements `PRODUCT_PAGE_HEADER_ASSET` et `APP_STORE_SEARCH_RESULTS_ASSET`. Mets-les sur **chaque** app.
- La plupart des en-têtes connus sont de l'image pure. Fais une version sans texte et une avec une ligne courte, puis teste-les une fois la version validée.

## Les pages produit personnalisées et la suite
- Une page par intention ou par canal, chacune avec sa 1re capture, son texte promotionnel, ses mots-clés liés et son lien direct dans l'app. Exemple : Grossesse « Enceinte ? Prépare ton périnée pour la naissance », Fuites « Sens ton périnée. Enfin. », Exercices « 32 exercices, muscle par muscle, sans sonde », Pros « Entre deux séances, garde le rythme » (le QR code des cabinets), Réseaux (le lien de la bio), Sport « Prépare ton retour au sport, 7 minutes par jour ».
- Un lien de campagne (`ct=`) par canal pour savoir d'où viennent les téléchargements, et la question « Comment nous as-tu connus ? » dans l'onboarding.
- Un seul test A/B à la fois chez Apple. Avec quelques centaines de visites par semaine, un test met 3 à 6 semaines : au début, les pages par canal apprennent plus vite.
- Une vraie nouveauté dans l'app (un défi de 21 jours en janvier, le pic des résolutions) donne un **événement** in-app et une **nomination** pour la mise en avant. Apple refuse un événement qui n'est qu'une promo.
- Des codes d'offre (un mois offert par cabinet partenaire, un parrainage « Offre un mois à une amie »), et une offre au moment de l'annulation.
- Les codes promo ne se créent qu'une fois l'achat intégré validé par Apple.

## Trouver les premiers utilisateurs sans pub
Voir le tableau des canaux de [`references/plan-aso.md`](references/plan-aso.md) : les premières utilisatrices (avis et bouche-à-oreille), les professionnels du domaine, les réseaux, le site et la recherche Google ou IA, les communautés, la presse, le parrainage. Chaque canal a sa première action et sa mesure. Rien n'est publié ni envoyé sans accord.

## Avant de soumettre
- [ ] Toutes les langues créées (dont en-GB, en-AU, en-US, fr-CA), mots-clés sans doublon, ≤ 100 octets.
- [ ] Captures sans paywall ni prix, les 3 premières avec les mots-clés, aucune promesse rouge.
- [ ] En-tête et image de recherche posés.
- [ ] Le fichier StoreKit a un pays fixé (sinon les prix passent de € à $ sur les captures).
- [ ] Chaque valeur envoyée est écrite dans un fichier de la fiche dans le dépôt (`fiche/version-x.md`).
- [ ] La page de suivi est à jour, et l'humain sait ce qu'il doit faire (ou qu'il n'a rien à faire).
