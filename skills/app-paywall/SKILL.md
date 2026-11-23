---
name: app-paywall
description: Concevoir le paywall d'une app payante et ses abonnements (offres, essai, frise, codes d'offre, demande d'avis, StoreKit). À utiliser quand on crée une app payante, qu'on touche à son paywall, à ses prix ou à ses abonnements, ou qu'on demande « dur ou freemium ? ».
---

# Le paywall

Le texte suit [`write-copy`](../write-copy/SKILL.md), l'interface suit [`design-interface`](../design-interface/SKILL.md). Les écrans d'une étude de cas, avec leur haptique et leur animation, sont dans [`references/case-study-screens.md`](references/case-study-screens.md).

## Le but
Le paywall demande de l'argent au moment où la personne sait pourquoi elle paierait, et sans rien lui cacher. Le reste (dur ou freemium, essai, prix) est une décision par produit, qu'on prend puis qu'on mesure.

## Les principes
1. **La valeur d'abord, le prix ensuite.** Le paywall vient après le moment où elle a senti ce que le produit lui apporte ([`app-onboarding`](../app-onboarding/SKILL.md)). Un prix qui tombe avant est un prix refusé.
2. **Honnête.** Le montant vraiment débité est le prix le plus visible, la date du premier paiement est écrite, annuler est simple et c'est dit. La peur du piège à abonnement est la première raison de partir : on y répond en montrant, pas en rassurant. (Les stores refusent d'ailleurs un prix « par mois » mis en avant sur une offre annuelle.)
3. **Le bouton juste avant ne promet rien que le paywall ne donne.** Un bouton « Voir mon plan » qui ouvre un prix, c'est une confiance perdue.
4. **Après l'achat, l'action.** L'écran suivant ouvre le premier usage, pas un tour.
5. **On juge sur ce que les gens paient vraiment**, après l'essai et au renouvellement, jamais sur les débuts d'essai. Les chiffres des vendeurs d'outils sont des pistes, pas des causes.
6. **Un paywall se teste.** L'offre, le prix, l'essai et l'endroit où il s'ouvre sont des paris. Pose de quoi les comparer dès le premier jour ([`product-analytics`](../product-analytics/SKILL.md)), pour qu'un agent puisse changer une chose, relire une semaine après et garder ce qui gagne.

## Les questions à te poser
- **Qu'est-ce qu'elle a déjà reçu au moment où le prix arrive ?** Si la réponse est « rien encore », le paywall est trop tôt ou le aha manque.
- **Dur ou freemium ?** Un paywall dur (rien sans essai ou achat) convertit bien plus quand la valeur se sent dès l'onboarding et que le produit coûte à faire tourner. Une part gratuite se défend quand la valeur vient avec l'usage répété, le réseau ou le contenu que les gens créent. Écris ton choix et sa raison.
- **Quel engagement demande le produit ?** Un résultat qui prend des semaines pousse vers l'annuel ; un besoin ponctuel vers une offre courte ou un achat unique.
- **De quoi a-t-elle peur ?** D'oublier d'annuler, de payer pour rien, de ne pas réussir. Chaque peur a sa réponse sur l'écran (la frise de l'essai, le rappel avant le débit, le prix écrit).
- **Qui sont tes premières utilisatrices ?** Un accès offert aux toutes premières donne les premiers avis et les premiers retours.

## Un exemple, pas un gabarit
Une app de santé payante a choisi : un paywall dur à la fin de l'onboarding, l'annuel présélectionné avec un essai de 7 jours, un mensuel sans essai, une frise « aujourd'hui, jour 5, jour 7 » qui dit quand on prévient et quand on débite, le choix entre un essai gratuit court et un premier mois à petit prix, des codes à vie pour les premières, et la demande d'avis seulement après un paiement et une réussite. Les écrans sont dans [`references/case-study-screens.md`](references/case-study-screens.md). Le skill `paywalls` des marketingskills ([`CREDITS.md`](../../CREDITS.md)) donne d'autres schémas.

## À éviter
- Optimiser les seuls débuts d'essai : la plupart démarrent et s'annulent le premier jour.
- Recopier le paywall d'une autre app sans s'être posé ses questions.
- Un prix ou un paywall sur une capture de la fiche du store.

## Avant de livrer
- [ ] Le choix (dur ou freemium, offres, essai) est écrit avec sa raison.
- [ ] Le prix débité, la date du premier paiement et la façon d'annuler se lisent sans chercher.
- [ ] Restaurer, les conditions et la confidentialité sont là.
- [ ] Les événements sont posés, et une date de relecture des chiffres aussi.
