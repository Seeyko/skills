---
name: product-analytics
description: Décider quoi tracer dans un produit (onboarding, paywall, abonnements, acquisition) et comment compter les personnes sans données sensibles. À utiliser quand on branche l'analytique d'une app ou d'un site, qu'on ajoute un parcours, un paywall ou une campagne, ou qu'on demande « qu'est-ce qu'on trace ? », « d'où viennent les téléchargements ? ».
---

# Ce qu'on trace

Le but : savoir, sans rien redemander, où les personnes s'arrêtent, ce qu'elles paient vraiment et d'où elles viennent. On trace les parcours, jamais les personnes. L'outil est dans [`pick-stack`](../pick-stack/SKILL.md).

## Les règles
1. **On envoie qu'un écran a été vu, puis comment il a été quitté.** Jamais la réponse choisie quand elle dit quelque chose de sensible (santé, situation de famille, argent).
2. **Une personne se compte une fois.** Un seul identifiant par humain, de la même forme sur le site, le serveur et l'app. Un test verrouille cette forme : si une surface la change seule, les personnes se dédoublent sans que rien ne le dise.
3. **Un identifiant tiré au hasard**, jamais un e-mail, un prénom ni un id de session. Le même identifiant sert aux achats, pour relier un paiement à un parcours.
4. **Faire marcher le service n'est pas mesurer l'audience.** Les erreurs, la modération et les enquêtes dans l'app se passent du consentement. Les pages vues et l'identification du navigateur l'attendent.
5. **Une tâche sans humain a son propre acteur, nommé et filtrable.** Sinon chaque appel compte comme un visiteur de plus.
6. **Chaque événement dit d'où il vient** : `debug`, `testflight` ou `app_store`. Les tableaux de bord écartent `debug`.
7. **La mesure ne coûte rien à l'app.** L'outil se charge après la première image, n'attend jamais et ne fait jamais planter : un envoi raté se perd en silence.
8. **L'équipe ne se mesure pas.** Les comptes internes et le back-office sortent des chiffres.
9. **Pas d'enregistrement de session** quand l'écran montre la vie des gens.
10. **Un réglage coupe les statistiques**, et « Effacer mes données » remet l'identifiant à zéro. La page de confidentialité dit exactement ce qui part.

## L'onboarding

| Événement | Quand | Propriétés |
|---|---|---|
| `onboarding_started` | le premier écran, une fois | |
| `onboarding_step_viewed` | chaque écran | `step` |
| `onboarding_step_completed` | l'écran est quitté | `step`, `action` (continuer, passer, retour, plus tard) |
| `onboarding_completed` | la fin | `first_session_now`, `duration_s` |
| `first_session_completed` | le premier vrai usage | |

- Le funnel suit l'ordre réel des écrans. Quand l'ordre change, le funnel change dans la même PR.
- Le moment aha se mesure sur son écran : allée au bout, contre passée ([`app-onboarding`](../app-onboarding/SKILL.md)).
- Après le paywall, `first_session_now` puis `first_session_completed` disent si l'usage a commencé tout de suite ou plus tard.

## Le paywall et l'abonnement

| Moment | Événements |
|---|---|
| Le paywall | `paywall_viewed` (`placement`, `variant`, `products`), `paywall_plan_selected`, `paywall_dismissed` (`reason`) |
| L'achat | `purchase_started`, puis `purchase_cancelled`, `purchase_pending` ou `purchase_failed` (`error`), `purchase_restored` |
| Le début | `trial_started` (`trial_type` : gratuit ou payé) ou `subscription_purchased` (`revenue`, `currency`) |
| La suite | `trial_converted`, `subscription_renewed`, `trial_cancelled`, `subscription_cancelled`, `subscription_reactivated` |
| La fin | `trial_expired`, `subscription_expired`, `subscription_billing_issue`, `subscription_refunded` |

- Chaque événement d'achat porte `product_id` et `placement` : on compare les offres et les endroits où le paywall s'ouvre.
- Un premier mois payé n'est pas un essai gratuit : `trial_type` les sépare ([`app-paywall`](../app-paywall/SKILL.md)).
- On juge une offre sur ce que les abonnés paient après l'essai, pas sur les débuts d'essai.
- Lus dans l'app, les événements d'abonnement n'arrivent qu'à la prochaine ouverture. Pour voir une résiliation le jour même, branche les notifications serveur du store.

C'est le cycle de vie complet d'un abonnement. Sans lui, on voit des débuts d'essai et on rate ce qui compte : qui paie après l'essai, qui part, et pourquoi (résiliation, échec de paiement, remboursement).

## Un parcours qui n'est pas un abonnement
Une place de marché, une inscription de professionnel, une réservation : le même schéma. Un événement par étape du parcours (`<parcours>_step_completed`, avec `step`), un à la fin, puis les événements d'argent venus du serveur (`payment_succeeded`, `payment_failed`), jamais du seul navigateur.

## Les erreurs et l'IA
- **Une erreur remonte toujours**, rattachée à la personne quand on la connaît.
- **Un événement par appel à un modèle** : le chemin (`import`, `assistant`, `dictation`…), le modèle, les jetons, la latence, l'erreur et le coût calculé. Le coût se lit par jour, par chemin et par personne active : c'est lui qui dit si un abonnement paie ses appels.

## D'où viennent les personnes
- **La question « Comment nous as-tu connus ? »** dans l'onboarding. C'est le seul lien par personne pour les réseaux, le bouche-à-oreille et les professionnels.
- **Un lien de campagne par canal** : le site transforme `utm_source` et `utm_campaign` en lien de campagne du store (`ct=`). Sur le site, un événement au clic vers le store.
- **Les pubs du store** donnent la campagne et le mot-clé exacts par personne, sans demande de suivi.
- **Les autres régies ne se lisent qu'en agrégé.** L'app envoie une valeur de conversion qui ne fait que monter : onboarding fini, paywall vu, premier usage, essai, achat.
- On ne relie jamais une visite du site à une installation par empreinte de l'appareil : c'est interdit par le store.

## Les tableaux de bord
Un par question : l'onboarding et le paywall ; les abonnements, les revenus et le départ ; l'usage et la rétention ; le site ; l'acquisition.

## Vérifier
- [ ] Aucune réponse sensible ne part, et aucun e-mail.
- [ ] Une personne de test donne une seule ligne, sur le site comme dans l'app.
- [ ] Le funnel de l'onboarding suit l'ordre réel des écrans.
- [ ] Un achat de test se retrouve du paywall au renouvellement, avec son `placement`.
- [ ] Chaque canal a son lien de campagne.
