---
name: app-paywall
description: Concevoir le paywall d'une app payante et ses abonnements (offres, essai, frise, codes d'offre, demande d'avis, StoreKit). À utiliser quand on crée une app payante, qu'on touche à son paywall, à ses prix ou à ses abonnements, ou qu'on demande « dur ou freemium ? ».
---

# Le paywall

Le texte suit [`write-copy`](../write-copy/SKILL.md), l'interface suit [`design-interface`](../design-interface/SKILL.md). Les écrans d'une étude de cas, avec leur haptique et leur animation, sont dans [`references/case-study-screens.md`](references/case-study-screens.md).

## Les principes
1. **Un paywall dur, honnête, à la fin de l'onboarding.** Juste après la réussite du aha et le plan. Sans croix, sans freemium. Un paywall dur convertit bien plus (RevenueCat : 10,7 % de téléchargements payants contre 2,1 %), à rétention annuelle à peu près égale.
2. **L'annuel est présélectionné**, avec un essai de 7 jours. Le mensuel n'a pas d'essai et coûte plus cher par mois.
3. **La frise de l'essai** sur l'annuel : « Aujourd'hui · Tout est ouvert », « Jour 5 · On te rappelle la fin de l'essai », « Jour 7 · Premier paiement, sauf si tu annules ». Elle répond à la peur de l'abonnement caché. Elle se replie quand on choisit le mensuel.
4. **Rien n'est caché** : le prix après l'essai et « Annulable à tout moment » sous le bouton. En pied : Restaurer, J'ai un code, Conditions, Confidentialité.
5. **Le bouton juste avant ne promet rien que le paywall ne donne.** « Voir mon jardin » qui ouvre un paywall, c'est raté.
6. **Le titre reprend la promesse verte**, et le décor de l'app reste en haut.
7. **Des codes à vie pour les premières utilisatrices** (« J'ai un code » ouvre la feuille Apple des codes d'offre). Elles donnent les premiers avis.
8. **La demande d'avis seulement aux abonnées**, après le premier paiement et une séance réussie (« Tu aimes … ? » → Oui / Pas encore), 3 fois par an au plus.
9. **Après l'achat, l'action** : l'écran suivant ouvre le premier usage ([`app-onboarding`](../app-onboarding/SKILL.md)).

## Le code
- StoreKit 2, abonnements App Store. Le fichier de configuration StoreKit a un pays fixé, sinon les prix passent de € à $ sur les captures.
- Les codes promo ne se créent qu'une fois l'achat intégré validé par Apple.
- Haptique : impact léger à la sélection d'une offre, moyen sur le bouton, notification de réussite quand l'achat est confirmé.

## À éviter
- Optimiser les seuls débuts d'essai : 82 % des essais démarrent le jour 0, et 55 % des annulations d'un essai de 3 jours aussi. Regarde ce que les abonnés paient vraiment.
- Prendre les chiffres des vendeurs pour des causes.
- Un prix ou un paywall sur une capture de la fiche App Store.

## Avant de livrer
- [ ] L'annuel est présélectionné, l'essai et sa fin se voient, le prix après l'essai est écrit.
- [ ] Pas de croix, mais Restaurer, J'ai un code, Conditions et Confidentialité sont là.
- [ ] Le fichier StoreKit a un pays fixé.
- [ ] Les deux états (annuel, mensuel) sont capturés en FR et en EN.
