---
name: app-onboarding
description: Concevoir et livrer l'onboarding d'une app mobile, du premier écran au premier usage (accueil, questions, moment aha, rappels, plan, compte). Le paywall a son propre skill, app-paywall. À utiliser dès qu'on crée une app, qu'on touche à son accueil ou à son premier lancement, ou quand on parle d'« onboarding », de « moment aha » ou d'un onboarding « trop long ».
---

# L'onboarding d'une app

Ce skill ne dit que ce qui est propre à l'onboarding. Le texte suit [`write-copy`](../write-copy/SKILL.md), l'interface suit [`design-interface`](../design-interface/SKILL.md), le paywall suit [`app-paywall`](../app-paywall/SKILL.md). Le cas complet d'une app de santé payante est dans [`references/case-study.md`](references/case-study.md), les études du marché dans [`references/market-studies.md`](references/market-studies.md).

## Avant de commencer
1. Lis les leçons `app.onboarding`, `copy` et `design` de la mémoire, s'il y en a une ([`memory-first`](../memory-first/SKILL.md)).
2. Lis le `CLAUDE.md` et le `DESIGN.md` de l'app.
3. Pas d'étude d'audience ? Fais-la d'abord ([`audience-study`](../audience-study/SKILL.md)).

## Le but
Un onboarding n'est pas une visite. Il amène la personne, le plus vite possible, à sentir ce que le produit change pour elle. Tout le reste (questions, rappels, compte, paiement) se range autour de ce moment.

## Les principes
1. **Un moment aha qui fait « waouh ».** Le plus petit geste qui fait sentir la valeur, avec un vrai résultat pour elle. Personne ne retient une liste de fonctions, tout le monde retient une réussite. Le geste est petit, la fête est grande.
2. **Le paiement vient après le waouh.** On ne paie pas une promesse, on paie pour garder ce qu'on vient de vivre. Le paywall suit [`app-paywall`](../app-paywall/SKILL.md).
3. **On accompagne jusqu'à la première action qui lui apporte de la valeur.** L'onboarding finit quand elle a fait cette action, pas quand elle a vu le dernier écran. Après le paiement, le bouton ouvre vraiment l'usage.
4. **La longueur se décide, elle ne se recopie pas.** Elle dépend de qui arrive et de ce qu'il faut pour que le moment magique marche. Voir les questions ci-dessous.
5. **Chaque étape sert le aha, la personnalisation réelle ou la suite.** Une question qui ne change rien à ce qu'elle va vivre sort du chemin. Une question qui change son plan reste, et dit pourquoi : la couper pour faire court fait baisser la conversion.
6. **Demander au bon moment.** Une permission (rappels, micro, photos) se demande quand elle vient de comprendre à quoi elle sert, en montrant le vrai résultat. Le compte arrive le plus tard possible, ou jamais. Avant lui, on voit déjà la vie publique du produit (ce que font les autres), partout où elle apparaît, jamais le privé : c'est ce qui donne envie d'entrer.

## Les questions à te poser avant de dessiner
Réponds par écrit, à partir de l'étude d'audience. Ce sont elles qui donnent la séquence, pas un gabarit.
- **Qui arrive, et dans quel état ?** Pressée ou curieuse, méfiante ou convaincue, seule chez elle ou dans le métro. Vient-elle d'une recommandation ou d'une pub vue trois secondes ?
- **Quel est le moment magique de ce produit ?** L'instant où elle se dit « ah, c'est pour moi ». Si tu ne sais pas le dire en une phrase, tu n'es pas prête à dessiner.
- **De quoi le produit a-t-il besoin pour que ce moment marche ?** Rien (on le fait vivre tout de suite), une réponse ou deux (on les pose avant), une donnée à elle (une photo, une liste : on l'aide à l'apporter). C'est ça qui fixe la longueur avant le aha.
- **Où et comment le vivra-t-elle ?** S'il faut du son, du calme ou du matériel, beaucoup ne le vivront pas : trouve une version qui marche partout.
- **Combien d'engagement demande le produit ensuite ?** Un produit cher ou exigeant (santé, apprentissage) gagne à un parcours plus long qui construit la confiance et le plan. Un outil simple gagne à ouvrir tout de suite.
- **Qu'est-ce qui la ferait partir ?** Un compte demandé trop tôt, une question indiscrète, un prix qui tombe avant la valeur.

Si tu hésites entre court et long : livre la version la plus défendable, mesure étape par étape ([`product-analytics`](../product-analytics/SKILL.md)), et laisse les chiffres trancher.

## La méthode
1. **L'étude d'audience** dans un fil à part ([`audience-study`](../audience-study/SKILL.md)).
2. **Trouver le aha.** Fais étudier les meilleurs onboardings de la catégorie par un agent dédié, qui revient avec ce qu'on garde, ce qu'on retire et ce qu'on améliore. Le skill `onboarding` des marketingskills et les exemples des créateurs cités dans [`CREDITS.md`](../../CREDITS.md) servent de base.
3. **Répondre aux questions ci-dessus**, puis dessiner la séquence et la maquette jouable ([`design-interface`](../design-interface/SKILL.md)).
4. **Écrire le texte** comme une seule histoire ([`write-copy`](../write-copy/SKILL.md)).
5. **Mesurer** chaque étape, puis relire les chiffres une semaine après ([`product-analytics`](../product-analytics/SKILL.md)).
6. **Montrer** : une vidéo du parcours complet à vitesse réelle.

## Un exemple, pas un gabarit
Dans une app de santé payante, pour une personne fatiguée et méfiante, le aha était un geste guidé de 40 secondes, sans le son. Il est passé de la 9e à la 3e étape, les questions de personnalisation venaient après, puis les rappels, le plan et le paywall. Le détail et ses raisons sont dans [`references/case-study.md`](references/case-study.md). C'est la réponse d'un produit à ses propres questions : un autre produit en aura une autre.

## Avant de livrer
- [ ] Tu sais dire le moment magique en une phrase, et il arrive avant le paiement.
- [ ] La longueur est justifiée par écrit : qui arrive, et ce qu'il faut pour le aha.
- [ ] Chaque question change ce qu'elle va vivre, et dit pourquoi.
- [ ] À la fin, elle a fait une première action utile, pas seulement vu des écrans.
- [ ] Chaque étape est mesurée, et une date de relecture des chiffres est posée.
- [ ] Les checklists de [`write-copy`](../write-copy/SKILL.md) et [`design-interface`](../design-interface/SKILL.md) sont passées.

## À éviter
- La visite des fonctions, et le tour complet avant le paywall.
- Un aha qui demande du son, du temps ou du matériel pour marcher.
- Recopier la séquence d'une autre app sans s'être posé ses questions.
- Optimiser les seuls débuts d'essai : regarde ce que les abonnés paient vraiment.
- Prendre les chiffres des vendeurs (RevenueCat, Superwall…) pour des causes.
