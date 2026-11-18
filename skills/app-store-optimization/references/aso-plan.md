# Un plan ASO et d'acquisition complet

L'exemple d'une app de santé payante en FR et EN, au lancement. À reprendre section par section pour une autre app.

## Le résumé
Le plus gros gain tient en trois changements : des captures qui disent le mot cherché dès la première, un sous-titre qui ne répète plus un mot du nom, et des pages produit dédiées par recherche et par canal. Le reste du plan sert à faire venir des utilisatrices sans pub et à mesurer ce qui marche.

## Le diagnostic de la fiche

| Point | Constat | Effet | Correction |
|---|---|---|---|
| Captures | Aucune légende ne dit « périnée », « grossesse » ni « bébé ». La 1re dit « Un jardin qui pousse avec toi ». | Apple lit les légendes pour la recherche, et 90 % des gens ne dépassent pas la 3e capture. | Nouvelles légendes avec le mot cherché en premier. |
| Sous-titre | « Renforcement du périnée » répète « périnée », déjà dans le nom. | Apple ne compte un mot qu'une fois : la moitié des 30 caractères ne rapporte rien. | « Grossesse et post-partum » ; le mot réglementé passe dans le champ caché. |
| Langues | FR + une seule fiche anglaise. | En France, Apple lit aussi la fiche Anglais (R.-U.) : 100 octets de mots-clés inutilisés. | Mots français dans en-GB, anglais dans en-AU, en-US, et fr-CA en plus. |
| Avis | Zéro au lancement, le concurrent principal affiche 4,8 sur environ 1 500 notes. | Passer de 0 avis à 4,5 étoiles est le levier de conversion le plus fort. | Les premières utilisatrices, dès la 1re semaine. |
| Description | Claire et complète. | Pas lue par la recherche, juste par les curieuses. | Rien à changer. |

La concurrence en français est mince : les deux leaders vendent d'abord un objet connecté, les autres sont des apps de sport avec un module. L'angle se défend seul : sans matériel, chaque muscle, une voix qui guide, un pro qui a relu.

## À qui on parle
Elle arrive sur la fiche le soir, souvent d'une main, juste après un moment gênant ou après qu'on lui a dit « faites vos exercices ». Elle est gênée et fatiguée, et ne sait pas si elle fait bien. La fiche doit lui montrer la femme qu'elle va devenir, pas l'interface.

| Qui | Qui elle veut devenir | La phrase qui accroche |
|---|---|---|
| Enceinte | Celle qui arrive prête | Enceinte ? Prépare ton périnée pour la naissance |
| Jeune maman, 0 à 3 mois | Celle qui reprend la main sur son corps | Sens ton périnée. Enfin. |
| En séances ou juste après | Celle qui sait qu'elle le fait bien | Entre deux séances, garde le rythme |
| Reprise du sport | Celle qui court et saute sans y penser | Prépare ton retour au sport, 7 minutes par jour |
| Fuites qui durent | Celle qui décide que ça ne durera pas | Des fuites depuis bébé ? Ce soir, tu t'occupes de ton périnée. |

On promet de l'émotion, en invitation (sens enfin ton périnée, tu seras accompagnée, tu vas y arriver), jamais la fin d'un symptôme ni un délai.

## Les nouveautés d'App Store Connect

| Nouveauté | Ce qu'on en fait |
|---|---|
| En-tête (image ou vidéo 21:9) et bibliothèque d'éléments | Les vidéos d'en-tête après la validation de la 1re version ; les visuels des résultats de recherche. |
| Test A/B de l'en-tête | En-tête sans texte contre une ligne courte. |
| Aperçu de la fiche (iPhone, iPad, sombre, langues) | Vérifier chaque capture et page perso avant la soumission. |
| Pages produit personnalisées liées à des mots-clés (jusqu'à 70) | Une page par intention et par canal. |
| Liens profonds des pages perso | La version suivante ouvre l'écran promis par la page. |
| Légendes des captures lues par la recherche | Les mots-clés dans les légendes. |
| Nominations pour la mise en avant | Une nomination pour chaque vraie nouveauté. |
| Événements in-app, listés dans la recherche | Un défi de 21 jours en janvier. |
| Analytique (100+ mesures, cohortes, comparaison aux apps similaires) | Suivre la conversion téléchargement → payant face à la catégorie. |
| Codes d'offre, offres de reconquête, message d'annulation | Un mois offert par partenaire ; une offre au moment de l'annulation. |
| Mensuel avec engagement 12 mois | À tester plus tard contre le mensuel, une fois qu'on a des chiffres. |

Ces nouveautés et leurs limites changent vite : vérifie-les dans les notes d'Apple avant de t'en servir.

## Les mots-clés par langue

| Fiche | Lue par | Sous-titre | Mots-clés (≤ 100 octets) |
|---|---|---|---|
| Français (France) | France, Belgique, Suisse | Grossesse et post-partum | kegel, enceinte, accouchement, fuites, urinaires, incontinence, plancher, pelvien, exercice, rééducation |
| Anglais (R.-U.) | France, Belgique, R.-U. | Postpartum & pregnancy Kegels | en français : kiné, césarienne, épisiotomie, vessie, muscler, renforcer, sage-femme, sport, maternité, bébé, maman |
| Anglais (Australie) | R.-U., Australie | Postpartum & pregnancy Kegels | postnatal, antenatal, exercise, trainer, incontinence, bladder, leaks, mum, midwife, physio, women, core, birth |
| Anglais (É.-U.) | États-Unis | Postpartum & pregnancy Kegels | prenatal, postnatal, exercise, trainer, incontinence, bladder, leaks, mom, midwife, core, birth, c-section |
| Français (Canada) | Canada | Grossesse et post-partum | comme la France |

## Les pages produit personnalisées
1. Grossesse : grossesse, enceinte, accouchement, naissance.
2. Fuites : fuites, urinaires, incontinence, vessie, pipi.
3. Exercices : kegel, exercice, muscler, renforcer, plancher, pelvien.
4. Pros : aucun mot-clé, c'est le QR code de l'affiche des cabinets.
5. Réseaux : aucun mot-clé, c'est le lien de la bio.

Chaque canal a son lien `ct=`, donc App Store Connect dit d'où vient chaque installation.

## Les tests, l'événement, les avis
- **Tests A/B** (un seul à la fois) : d'abord les anciennes captures contre les nouvelles, puis l'en-tête sans texte contre avec texte.
- **Événement in-app** : « Défi de janvier : 21 jours », visible deux semaines avant. Il faut une vraie nouveauté dans l'app (une récompense rare qui arrive en 21 séances).
- **Avis** : les premières utilisatrices d'abord, avec un message une semaine après leur code. Ensuite la demande d'avis d'Apple, après le 1er paiement, 3 fois par an au plus.

## Trouver des utilisatrices sans pub

| Canal | Pourquoi ça marche | Première action | Ce qu'on mesure |
|---|---|---|---|
| Les premières utilisatrices (une cinquantaine de codes à vie) | Premiers avis et bouche-à-oreille | Les codes dès la validation d'Apple, le message d'avis à J7 | Nombre d'avis, note, `ct=premieres` |
| Les professionnels du domaine | Ils voient chaque jour des personnes qui ont le problème, et l'app prend le relais à la maison | Un premier cabinet, puis une vingtaine autour : un mail, une affiche A5 avec QR code, un code « 1 mois offert » par cabinet | Codes utilisés par cabinet, `ct=pro` |
| Instagram et TikTok | Un univers visuel et des mini-jeux se partagent bien | 3 posts par semaine : un geste expliqué en dessin, un mini-jeu filmé, les coulisses | Visites du profil, `ct=insta` |
| Le site et la recherche Google ou IA | Les gens cherchent leur problème en toutes lettres, sur Google comme dans les assistants IA | Des articles tirés des fiches relues par le pro, avec FAQ | `app_store_clicked` dans l'analytique |
| Groupes et forums | Les questions y reviennent chaque jour | Une personne de l'équipe répond en son nom, sans lien sauf si on le demande | Mentions, `ct=communaute` |
| Presse, podcasts, newsletters | Une histoire vraie derrière l'app | Une dizaine de médias ciblés, après les 10 premiers avis | Retombées, `ct=presse` |
| Parrainage | On en parle à une amie | « Offre un mois à une amie » avec un code d'offre | Codes utilisés |

Rien n'est publié ni envoyé sans l'accord du propriétaire.

## Le calendrier
1. **Semaine 1** : valider mots-clés et légendes, peindre les nouvelles captures et les visuels des pages perso. À la validation d'Apple : en-tête, codes des premières utilisatrices, texte promotionnel, sortie. Premier contact avec un pro.
2. **Semaine 2** : les pages perso en review (sans nouvelle version), le test A/B 1, le message d'avis, les mails aux cabinets, les premiers articles.
3. **Semaine 3** : premiers chiffres par canal, on coupe ce qui ne marche pas. Sous-titre et mots-clés partent avec la version suivante. La nomination de l'événement de janvier part avant mi-décembre.
4. **Après** : l'événement in-app, puis le test A/B 2 sur l'en-tête.

## Les chiffres qu'on suit
Dans App Store Connect : impressions, vues de la fiche, conversion par source, par page perso et par `ct`, comparaison aux apps similaires. Dans l'analytique : installation → fin de l'accueil → paywall → essai → payant.

| Mesure | Objectif à 3 semaines |
|---|---|
| Vue de la fiche → téléchargement (recherche) | 30 % ou plus |
| Téléchargement → essai | 15 % ou plus |
| Essai → payant | 35 % ou plus (lu à partir de J+7) |
| Avis | 15 ou plus, note ≥ 4,5 |

## Sources
- [Apple Newsroom, WWDC26 : nouvelles capacités de l'App Store](https://www.apple.com/newsroom/2026/06/apple-expands-app-store-capabilities-to-help-developers-grow-and-reach-new-users/)
- [Phiture, récap WWDC26 pour la croissance](https://phiture.com/blog/wwdc26-updates/)
- [Appbot, découverte sur l'App Store après la WWDC26](https://appbot.co/blog/apple-wwdc-2026-app-discovery-updates/)
- [AppTweak, langues lues par pays](https://www.apptweak.com/en/aso-blog/how-to-benefit-from-cross-localization-on-the-app-store)
- [Stora, pages perso liées aux mots-clés](https://stora.sh/blog/2026-05-13-custom-product-pages-70-keyword-linking-aso-guide)
- [iClarified, analytique App Store Connect de mars 2026](https://www.iclarified.com/100333/apple-updates-app-store-connect-analytics-with-100-new-metrics-cohorts-and-benchmarks)
- [Guide des nominations 2026](https://appscreenshotstudio.com/blog/get-featured-on-the-app-store-2026-nominations-guide)
- Le skill `aso` des marketingskills de Corey Haines (specs Apple et repères de conversion).
