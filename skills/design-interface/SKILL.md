---
name: design-interface
description: Concevoir, animer ou relire une interface (écran d'app, parcours, site, composant, capture, vidéo de démo) pour qu'elle parle toute seule, se sente au toucher et ne fasse pas « IA ». À utiliser avant tout travail d'interface, dans une app comme sur un site, et pour relire un diff qui touche au visuel.
---

# Concevoir l'interface

Ce skill vaut pour tous les projets. Le `DESIGN.md` du projet donne le style (couleurs, polices, composants, durées) et gagne sur ce skill. Pour le texte, voir [`write-copy`](../write-copy/SKILL.md).

## Avant de commencer
1. Lis le `DESIGN.md` du projet en entier, même pour une petite tâche. S'il n'existe pas, écris-le d'abord (format `DESIGN.md` de Google Labs), puis une règle qui le charge pour chaque fichier front.
2. Pour la méthode, charge les skills de finition : `emil-design-eng`, `choreograph`, `review-animations`, `apple-design`, `animate-text`, `impeccable`, et `swiftui-expert-skill` sur iOS (voir [`../../CREDITS.md`](../../CREDITS.md)).
3. Fais concevoir les écrans et les dessins par le modèle le plus fort. Chaque brief rappelle la charte du projet.

## Les principes
1. **L'écran parle tout seul.** Si on doit l'expliquer avec une phrase, on corrige le dessin, la couleur ou le geste. On n'ajoute pas la phrase.
2. **Une seule chose mise en avant par écran, un seul CTA.** Ce qui n'est pas le sujet se fond dans le fond.
3. **Peu de cartes, pas de bordures.** Le texte est posé sur le fond, ou sur des cartes qui ont la matière de l'univers de l'app.
4. **L'écran ne change jamais vraiment.** Dans un parcours, le bouton reste fixe et seul le contenu se transforme. Un contenu en remplace un autre sur place, par un fondu flou. Le libellé du bouton se fond sur place, un temps après. Rien ne glisse sur le côté sans raison.
5. **Montre au lieu d'expliquer.** Une notification qui fait défiler les vrais rappels remplace la phrase qui les décrit. Une graine qui pousse remplace « ton plan est prêt ». Une couleur reconnaît une zone mieux qu'une étiquette.
6. **Pas de réglage lourd sur un écran d'expérience.** Ni interrupteur ni formulaire là où la personne vit le produit : un petit bouton rond (un haut-parleur) suffit. Les réglages vivent ailleurs.
7. **Chaque geste se sent.** Haptique sur chaque bouton, chaque choix, chaque temps d'un rythme.
8. **La friction se décide.** Le moins possible quand le produit est une porte vers un système qui comprend, exprès là où elle protège ou engage. Voir plus bas.
9. **Natif.** Le composant de la plateforme avant tout contrôle maison : la personne le connaît déjà, il suit le système (accessibilité, gestes, mises à jour) et il coûte moins à tenir. Sur iOS aujourd'hui : SwiftUI, et le verre du système pour ce qui flotte au-dessus du contenu, jamais pour le contenu lui-même.
10. **Un univers fort.** Une direction artistique qui se démarque (par exemple une aquarelle « faite main », jamais enfantine ni vectorielle plate). Les icônes et mascottes de l'auteur ne sont jamais redessinées sans qu'il le demande. Quand il le demande, le niveau à atteindre est celui d'un de ses dessins de référence.
11. **Les moments de réussite font « wow ».** C'est la seule exception au calme : voir plus bas.

12. **La même chose a le même visage partout.** Une carte, une icône, une couleur par type de contenu, d'un écran à l'autre. Dans le code aussi : un seul composant.
13. **Le contenu avant les contrôles.** Si les boutons posés sur une image la cachent, il y en a trop. On montre ce qui change, pas tout.
14. **Ça se juge au ressenti, sur le vrai rendu.** L'agent regarde l'écran qui tourne et recommence jusqu'à ce que ce soit beau, pas jusqu'à ce que la liste soit cochée. « Presque » la référence, ce n'est pas fini. Un rendu correct mais générique est refusé : on doit reconnaître la marque.

## La méthode
- **Une maquette jouable avant le code.** Une page HTML avec les écrans en vrai format (393 × 852 pour un iPhone), côte à côte dans une rangée qui défile à l'horizontale. Sous chaque écran, hors du cadre, des repères « Haptique », « Animation », « Navigation ». On l'essaie sur un téléphone, on la valide, puis on code. L'app suit la maquette exactement.
- **Toujours un visuel avec une proposition** (une vidéo d'aperçu, une planche) : une description seule ne se valide pas. Un visuel validé se fusionne tout de suite.
- **Une référence (une vidéo, une app) se découpe image par image** pour en reprendre le rythme et le nombre de temps, jamais le dessin : on la repense dans l'univers de l'app. Elle s'analyse deux fois : par toi, et par un agent qui n'a que la matière brute. Garde ce qui converge.
- **Chaque correction du propriétaire devient une règle** dans `DESIGN.md`, avec sa raison, dans le même commit (skill `learn-taste`).

## Combien d'interface ? La friction se décide
Avant de dessiner, écris en une phrase à quoi sert l'interface de ce produit. La quantité d'écrans, de champs et de boutons en découle. Elle ne se recopie pas d'un produit à l'autre.

- **Quand le produit est une porte vers un système qui comprend** (un assistant, des agents, une mémoire), l'interface sert à deux choses : dire et voir. Le but est alors le moins de friction possible. La personne dit ce qu'elle veut comme elle le dirait à quelqu'un (voix, photo, une phrase), le système range, et l'écran montre seulement ce qui lui sert maintenant. Chaque champ à remplir est un travail qu'on lui rend alors que le système pouvait le faire.
- **Quand la friction protège ou engage**, on la garde, exprès. Confirmer avant un geste qu'on ne peut pas défaire, un paiement, un choix médical. Un parcours plus long quand il construit la confiance ou le plan ([`app-onboarding`](../app-onboarding/SKILL.md)). Un outil d'expert où tout voir d'un coup fait gagner du temps.

Les questions à te poser :
- **Qu'est-ce que la personne vient faire, et combien de fois par jour ?** Un geste fait dix fois par jour ne supporte aucune étape de trop.
- **Qu'est-ce que le produit peut comprendre ou deviner seul ?** Tout ce qu'il peut deviner, il ne le demande pas.
- **Qu'est-ce qui sert à la personne, et qu'est-ce qui ne sert qu'à la machine ?** Ce qui ne sert qu'à la machine ne s'affiche pas.
- **Qu'est-ce qui se passe si elle se trompe ?** Si l'erreur se défait d'un geste, on ne confirme pas : on laisse faire et on donne « Annuler ». Si elle ne se défait pas, on ralentit.
- **Où la lenteur aide-t-elle ?** Nomme les endroits où tu gardes de la friction, et pourquoi.

Ce qui reste vrai dans les deux cas :
- **Chaque écran, onglet ou bouton en plus se justifie** par une action que la personne fait vraiment.
- **Le produit répond tout de suite, et montre ce qu'il a fait.** Jamais un « C'est noté » sans rien derrière.
- **Une erreur se rattrape.** Annuler remonte plusieurs gestes, et un toucher par mégarde ne fait rien disparaître.
- **On ne montre pas ce qu'on ne sait pas.** Une donnée qui peut être vieille montre son âge.

Exemple : une liste de courses reliée à un assistant a fini avec un seul écran, une seule entrée (parler, photographier ou écrire) et un toucher par ligne, parce que son but était d'être la porte la plus courte vers le système. Un produit avec un autre but aurait une autre réponse.

## L'attente et le mouvement
- **Rapide, on ne montre rien.** Sous une demi-seconde, pas d'indicateur. S'il apparaît, il finit son cycle, et il est très léger : il s'affiche justement quand le réseau est mauvais.
- **Jamais un écran faux pendant l'attente** (un écran de connexion le temps qu'on connecte). Puis un seul écran de réussite, qui dit clairement l'état.
- **On anime l'apparition, pas le repos.** Rien ne bouge en boucle. Entre deux états, jamais de coupure : le survol, l'appui et le retour s'enchaînent.
- **Ce qui suit le doigt ou le curseur ne rebondit pas** : on doit pouvoir viser. Le ressort est pour ce qui arrive ou repart.
- **Sur téléphone, un site se comporte comme une app** : pas de zoom au double toucher, les zones sûres respectées, rien de fixe qui mange l'écran.
- **Une démo montre le vrai produit**, jamais une maquette de l'interface.

## Les moments de réussite
Une réussite (une série, une chose gagnée, la fin d'un effort) a le droit de claquer, et elle seule. Une première version qui suit les règles calmes du reste de l'app est trop molle.
- **Beaucoup de temps courts**, un toutes les 0,3 s environ, chacun avec son image, un ressort plus vif que d'habitude et sa frappe haptique.
- **Anticiper, frapper, laisser retomber** : avant le coup final, ça plane, grossit, tremble ; le coup dure deux images ; après, un flash, des ondes, une gerbe, puis tout se calme.
- **Écraser et étirer** : ce qui tombe s'étire, ce qui touche s'écrase et rebondit, ce qui surgit dépasse sa taille.
- **L'haptique part en une seule séquence** calée sur l'animation, pour que chaque coup tombe sur son image.
- **Rien ne se touche pendant la fête**, aucune question ni bouton à l'écran. Un toucher la passe, jamais dans sa première seconde.
- **Jamais de jour manqué** : un compteur qui ne peut que monter, pas de rouge, pas de croix.
- **Peu de mots** : un chiffre, pas de « Bravo ».
- **La collection se voit** : ce qui est gagné en couleur, les 2 ou 3 suivants en esquisse, le tout derrière un dézoom. Ça donne envie, sans jamais décourager.
- **Une chose nouvelle s'apprend avant de servir** : un mini-tuto avec ce seul geste, puis sa fête quand il est réussi.
- La partition est une fonction pure du temps, testée (l'ordre des poses, le repos à la fin, l'haptique sur les mêmes temps).

## Les visuels et les vidéos
- Courts, nerveux, 60 fps, sans texte qui décrit et sans intro.
- À vitesse réelle, pas en accéléré, dans un vrai mock, avec des données réalistes et assez nombreuses. Pour un post réseau, le parcours peut s'accélérer : voir [`social-content`](../social-content/SKILL.md).
- Parfaitement fluide : une vidéo qui saccade ne sort pas.
- Le fond de la marque derrière une vidéo ou une capture.
- Un détourage propre, ou rien.
- Fidèle au réel : une image générée ne change pas la forme d'un objet réel, n'ajoute pas un détail qui n'existe pas et garde les proportions. Pas de vraie marque dans un visuel.
- Pour un travail payant (génération d'images), un seul essai d'abord. Tout ce qui est généré est gardé sur un disque durable.

## Avant de livrer un écran
- [ ] Le test du doigt est passé ([`write-copy`](../write-copy/SKILL.md)).
- [ ] Regardé en vraie taille, en FR et en EN, sur téléphone (et sur ordinateur pour un site).
- [ ] Chaque contrôle a son haptique, sa cible de 44 pt et son libellé VoiceOver (il porte ce que le dessin ne dit pas).
- [ ] Chaque mouvement a sa version « Réduire les animations » (un simple fondu).
- [ ] N'anime que la transformation et l'opacité. 120 Hz tenus sur le plus vieil appareil supporté.
- [ ] Captures avant et après envoyées (jamais commitées), et une vidéo à vitesse réelle pour un parcours.
