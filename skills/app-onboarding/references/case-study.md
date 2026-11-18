# Étude de cas : l'onboarding d'une app de santé payante

Une app iOS payante d'exercices du périnée pour la grossesse et le post-partum, dans un univers de jardin peint à l'aquarelle, en FR et en EN. Ce fichier dit ce qui a mené à l'onboarding final, dans l'ordre, et pourquoi.

## Le déclic
Le premier onboarding faisait découvrir tous les muscles avant le paywall : trop long. Une vidéo de Chris Raroque rappelle le but : amener le plus vite possible au premier moment aha, pour que la personne comprenne la valeur de l'app. Pas besoin de montrer toutes les fonctions : un peu de personnalisation, ce qu'elle va en tirer, et le ressenti de satisfaction.

Deuxième étape : faire étudier les meilleurs onboardings du fitness et de la santé par un agent dédié, qui revient avec ce qu'on garde, ce qu'on retire et ce qu'on améliore ([`market-studies.md`](market-studies.md)).

## Les étapes du travail

| Étape | Quoi |
|---|---|
| 1 | Copy et paywall de départ validés. |
| 2 | Une vidéo de référence (la fin d'un onboarding de banque, 21 s) est analysée deux fois : par l'agent principal, puis par un agent qui n'a que la vidéo. Les deux convergent : l'écran ne change jamais vraiment. |
| 3 | Une seule scène qui se fond (flou), un libellé de bouton qui se fond sur place, un lavis qui prend la teinte de l'étape, une notification qui fait défiler les vrais rappels, une graine qui pousse avec un toucher par étape, moins de cartes. |
| 4 | Un `DESIGN.md` (format Google Labs), chargé par une règle à chaque fichier front, et les skills d'Emil Kowalski et SwiftUI. |
| 5 | L'étude d'audience dans un fil dédié ([`../../audience-study/references/example.md`](../../audience-study/references/example.md)) et un guide de langage. |
| 6 | Le aha passe de la 9e à la 3e étape. Le tour des muscles et le bilan de 10 minutes sortent du chemin. « Ma première séance » ouvre la séance, sinon un seul rappel. |
| 7 | Le texte est réécrit en une histoire, puis relu par deux agents en parallèle. |
| 8 | L'interrupteur « La voix » sur l'écran du aha est remplacé par un haut-parleur rond. |
| 9 | Fusion, funnel réordonné, build TestFlight. |

## La séquence finale

| # | Étape (`step`) | Titre | Ligne | Bouton |
|---|---|---|---|---|
| 1 | `welcome` | Le nom peint, avec les mascottes | « 7 minutes par jour pour te sentir à nouveau toi. » + « Ne remplace ni ta sage-femme ni ton kiné. » | « Commencer » |
| 2 | `situation` | « Où en es-tu ? » | « Bébé est né » / « Je suis enceinte » + date | « Continuer » |
| 3 | **`feel_demo`** | « Trouve ton périnée » | « 40 secondes, là où tu es. » + haut-parleur rond | « Je suis prête » → 3-2-1 → rythme |
| 3b | le rythme, 2 tours | | « Inspire, et laisse tout se relâcher. » / « En soufflant, serre comme pour retenir un pipi, et remonte doucement. » / « Relâche » | |
| 3c | la question | « Tu l'as senti ? » | | « Oui » / « Pas vraiment » |
| 3d | oui | « Tu l'as trouvé » (haptique de réussite, 3,5 s) | « C'est ce geste-là. Tu sais le faire. » | |
| 3e | pas vraiment | « On le cherche ensemble » | « Au début, beaucoup de femmes le sentent à peine. » | |
| 4 | `birth` | « Comment s'est passé ton accouchement ? » | « Pour choisir tes exercices. » | « Continuer » / « Passer » |
| 5 | `postnatal_visit` | « Ta visite post-natale est faite ? » | « Le rendez-vous des 6 à 8 semaines… » | « Oui » / « Pas encore » |
| 6 | `acquisition_source` | « Comment nous as-tu connus ? » | réseaux, une amie, un pro de santé, recherche, autre | « Continuer » |
| 7 | `voice` | « Choisis la voix qui te guide » | + « Des vibrations » | « Continuer » |
| 8 | `reminders` | « On y pense pour toi » | la notification qui défile ; matin, après-midi | « Activer mes rappels » / « Continuer sans rappel » |
| 9 | `plan` | « Ton jardin est prêt » (la graine pousse) | « Aujourd'hui, tu deviens celle qui s'en occupe. » + les lignes du plan | « Continuer » |
| 10 | `paywall` | « Retrouve ton périnée, 7 minutes par jour » | frise de l'essai, annuel présélectionné | essai |
| 11 | `thanks` | « Ça y est, tu as commencé » | « On te prévient 2 jours avant la fin de l'essai. » | « Ma première séance » + « Rappelle-moi ce soir » ou « Rappelle-moi demain » selon l'heure |

Enceinte : sans les étapes 4 et 5.

## Le paywall
Voir [`../../app-paywall/references/case-study-screens.md`](../../app-paywall/references/case-study-screens.md). En bref : paywall dur, sans croix ni freemium, annuel présélectionné avec 7 jours d'essai, mensuel sans essai, frise de l'essai, « J'ai un code » pour les premières utilisatrices, demande d'avis seulement aux abonnées après le premier paiement et une séance réussie.

## La mesure
- `onboarding_step_completed` (`step`, `action` = `answered` ou `skip`) à chaque étape. La réponse au aha (oui ou non) ne part pas : c'est une donnée de santé.
- `onboarding_completed.first_session_now` : la première séance a-t-elle été faite tout de suite ?
- Un funnel « écran par écran », remis dans l'ordre après chaque changement.

## Ce qui a été refusé en route
- Le tour des muscles de 10 minutes avant le paywall : trop long, il reste dans l'app.
- Les cartes blanches partout : le texte posé sur le fond, ou des cartes qui ont la matière de l'aquarelle.
- L'interrupteur « La voix » sur l'écran du aha.
- Cinq textes qui se répètent toutes les cinq secondes.
- Un bouton « Voir mon jardin » qui ouvrait le paywall : il promettait ce qu'il ne donnait pas.
- Les promesses « pour les fuites » dans le plan.
