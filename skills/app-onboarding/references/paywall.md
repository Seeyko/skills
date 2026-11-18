# Le paywall et les écrans qui l'entourent

Les écrans validés de l'étude de cas, de l'expérience du aha jusqu'au premier usage. Chaque écran est décrit avec son haptique et son animation : c'est le niveau de précision à donner à l'agent qui code.

## Valider avant de coder : la maquette HTML
Fais une page HTML jouable avec les écrans en vrai format iPhone (393 × 852), côte à côte dans une rangée qui défile à l'horizontale (en colonne sur téléphone). Sous chaque téléphone, des repères étiquetés « Haptique », « Animation », « Navigation », hors de l'écran. Les paywalls sont cliquables (annuel ou mensuel), la démo tourne en boucle, « Réduire les animations » est respecté. On valide cette page, puis on code.

## Les écrans

### 8a · L'expérience, avant
- Titre « Sens ton périnée », une fleur fermée qui respire à peine (échelle 1 → 1,035 sur 5 s), un bouton « Je suis prête ».
- Haptique : impact moyen sur « Je suis prête ». La voix choisie démarre.

### 8b · L'expérience, pendant (45 s)
- Inspire : la fleur s'ouvre (4 s). En soufflant : elle se resserre et remonte de 16 pt (5,5 s). Relâche : retour au repos (2,5 s). Deux cycles.
- La phrase de la voix en cours s'affiche en fondu (0,3 s), calée sur l'audio : « Inspire, et laisse tout se relâcher. » · « En soufflant, serre comme pour retenir un pipi, et remonte doucement. » · « Relâche. » Une barre se remplit sur toute la démo.
- Haptique, si les vibrations sont actives : une montée douce continue pendant le serrage, rien à l'inspire.

### 8c · L'expérience, fin
- Titre « Tu l'as senti ? », fleur ouverte, deux boutons « Oui » et « Pas vraiment ».
- « Oui » : notification success, écran suivant. « Pas vraiment » : impact léger, les boutons laissent place en fondu à « C'est fréquent au début. On y revient à chaque séance. », puis l'écran suivant après 2,5 s.

### 10 · Le plan est prêt
- Titre « Ton jardin est prêt », une pousse qui sort de terre, trois lignes de plan avec une pastille de couleur chacune (« 7 minutes par jour », « On commence par l'avant », une ligne qui reprend une réponse de l'accueil).
- Animation : la pousse sort (ressort, 0,6 s), puis les trois lignes arrivent l'une après l'autre (décalage 0,15 s). Un papillon flotte en boucle.
- Haptique : notification success quand la pousse apparaît. Le bouton du bas mène au paywall sans promettre autre chose.

### 11 · Le paywall, annuel sélectionné (par défaut)
- Titre « Retrouve ton périnée, 7 minutes par jour », l'univers de l'app en haut qui se fond dans le papier.
- La frise de l'essai : « Aujourd'hui · Tout est ouvert », « Jour 5 · On te rappelle la fin de l'essai », « Jour 7 · Premier paiement, sauf si tu annules ».
- Deux offres : « 1 an · 49,99 € · 4,17 €/mois » avec la pastille « 7 jours offerts », et « 1 mois · 12,99 € ».
- Bouton « Essayer 7 jours gratuits », puis « Puis 49,99 € par an. Annulable à tout moment. »
- Pied : « Restaurer · J'ai un code · Conditions · Confidentialité ».
- Haptique : impact léger à la sélection d'une offre, moyen sur le bouton, notification success quand l'achat est confirmé.
- Animation : la coche de l'offre choisie rebondit (ressort 0,25 s), son bord passe au vert.
- Navigation : pas de croix. « J'ai un code » ouvre la feuille Apple des codes d'offre.

### 11 · Le paywall, mensuel sélectionné
- Pas de frise : il n'y a pas d'essai sur le mensuel. Elle se replie en 0,45 s et l'image prend la place.
- Le bouton devient « Continuer », la ligne « 12,99 € par mois. Annulable à tout moment. » Le texte change en fondu (0,2 s), sans saut de mise en page.

### 12 · Après un code valide (premières utilisatrices)
- Titre « Merci d'être là depuis le début », ligne « Ton jardin est à toi, pour toujours. », bouton « Entrer dans mon jardin ».
- Le jardin s'ouvre en tache d'aquarelle (échelle 0,8 → 1, 0,6 s), quelques pétales tombent, les mascottes flottent. Notification success à l'arrivée.

### 12 · Après le lancement de l'essai
- Titre « C'est parti », ligne « On te prévient 2 jours avant la fin de l'essai. », bouton « Ma première séance ».
- Un arrosoir se penche en boucle (3,2 s), les gouttes tombent sur la pousse. Notification success à l'arrivée.

## Les règles du paywall
- Paywall dur à la fin de l'onboarding, sans croix, sans freemium.
- L'annuel présélectionné avec l'essai ; le mensuel sans essai, plus cher par mois.
- La frise de l'essai sur l'annuel seulement. Elle répond à la peur du « piège à abonnement ».
- Des codes à vie pour les premières utilisatrices (« J'ai un code »), qui donnent les premiers avis.
- La demande d'avis seulement aux abonnées, après le premier paiement et une séance réussie (« Tu aimes ton jardin ? » → Oui / Pas encore), 3 fois par an au plus.
- Le fichier de configuration StoreKit a un pays fixé, sinon les prix passent de € à $ sur les captures.
