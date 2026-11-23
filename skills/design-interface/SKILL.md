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
8. **Le minimum d'interface** : une vue, un geste, une entrée naturelle (voix, photo, texte). Voir plus bas.
9. **Natif.** Le composant de la plateforme avant tout contrôle maison. Sur iOS : SwiftUI, et Liquid Glass partout où c'est la couche flottante, jamais sur le contenu. Sur le web : shadcn.
10. **Un univers fort.** Une direction artistique qui se démarque (par exemple une aquarelle « faite main », jamais enfantine ni vectorielle plate). Les icônes et mascottes de l'auteur ne sont jamais redessinées sans qu'il le demande. Quand il le demande, le niveau à atteindre est celui d'un de ses dessins de référence.
11. **Les moments de réussite font « wow ».** C'est la seule exception au calme : voir plus bas.

## La méthode
- **Une maquette jouable avant le code.** Une page HTML avec les écrans en vrai format (393 × 852 pour un iPhone), côte à côte dans une rangée qui défile à l'horizontale. Sous chaque écran, hors du cadre, des repères « Haptique », « Animation », « Navigation ». On l'essaie sur un téléphone, on la valide, puis on code. L'app suit la maquette exactement.
- **Toujours un visuel avec une proposition** (une vidéo d'aperçu, une planche) : une description seule ne se valide pas. Un visuel validé se fusionne tout de suite.
- **Une référence (une vidéo, une app) se découpe image par image** pour en reprendre le rythme et le nombre de temps, jamais le dessin : on la repense dans l'univers de l'app. Elle s'analyse deux fois : par toi, et par un agent qui n'a que la matière brute. Garde ce qui converge.
- **Chaque correction du propriétaire devient une règle** dans `DESIGN.md`, avec sa raison, dans le même commit (skill `learn-taste`).

## Le minimum d'interface
Une app est une fenêtre sur sa donnée, si simple et si polie que personne n'a envie de la refaire. Chaque écran, onglet ou bouton en plus doit être une action, et se discute.
- **Pas de formulaire.** La personne parle, prend une photo ou écrit une phrase, et le produit comprend. Un seul bouton **+** ouvre les trois. Seule exception : corriger, qui ouvre les champs, parce qu'on corrige ce que la compréhension a raté.
- **Un écran quand c'est possible.** Pas d'onglet, d'écran de réglages ni d'écran de détail sans accord.
- **Montre le minimum.** Ce qui sert aux agents (le stock, le catalogue, les prix) ne s'affiche pas. Pour savoir ce qu'il y a dans le frigo, on ouvre le frigo.
- **Un geste par ligne**, et un toucher dans la poche ne fait jamais disparaître quelque chose : la ligne reste, barrée, et un second toucher la remet.
- **Annuler remonte plusieurs gestes**, comme ⌘Z. Un seul niveau ne suffit pas après deux touchers de trop.
- **La réponse est immédiate, en mots simples.** La phrase envoyée scintille tout de suite, puis le vrai changement vient se ranger à sa place (morph). Jamais « C'est noté » sans rien derrière, jamais une longue liste.
- **Derrière chaque phrase, un assistant**, jamais un routage figé : ce que dit la personne n'est pas toujours pour l'app ouverte. Il voit ce que l'écran montre (le jour affiché, la liste ouverte), et « Annuler » reprend la phrase entière.
- **L'âge, pas l'invention.** Une donnée qui peut être vieille montre son âge. Une valeur inconnue ne s'affiche pas.

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
