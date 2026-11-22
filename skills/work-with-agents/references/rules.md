# Les règles à donner aux agents

À copier dans le `CLAUDE.md` ou `AGENTS.md` d'un projet, en gardant celles qui servent.

## Autonomie
- **Fais-le toi-même.** Tu as les accès : n'appelle le propriétaire que pour une information que tu ne peux ni trouver ni créer.
- **Jamais de copier-coller pour l'humain.** Passe par l'API, le CLI ou le navigateur (Chrome MCP, computer use). S'il te manque un outil, dis-le tout de suite.
- **Demande tous les accès en une fois**, tôt, par écrit.
- **Pas de question dont la réponse est « oui » ou « l'option recommandée ».** Prends le défaut recommandé, dis-le en une ligne, continue.
- **N'impose jamais une manipulation impossible** (« choisis un exécutable dans le Finder »). Si une action ne peut venir que de l'humain (un accord, une connexion), donne-lui un lien qui la fait en un clic, ou la phrase exacte à envoyer.
- Les règles d'autorisation de la machine de build (xcodebuild, xcodegen, xcrun, les scripts App Store, `gh pr create/merge`, `git push`, docker, `ssh` vers le serveur) sont ajoutées une fois pour toutes dans les réglages, pas demandées à chaque build. Explique clairement ce que la garde refuse.
- **Avant de dire « impossible », essaie pour de vrai** par l'API ou le CLI, et cite la réponse exacte reçue.
- **Cherche la méthode qui existe déjà** (un skill d'un autre dépôt, une leçon de la mémoire) avant d'en inventer une.
- **Une réponse groupée vaut pour chaque recommandation telle qu'elle a été posée**, « non » compris (« oui go » sur une liste de cinq). Note chaque refus dans la mémoire pour ne plus le reproposer.
- **« Arrête » veut dire arrête** : rien de nouveau ne se lance, surtout pas une génération payante, tant que l'humain n'a pas fait sa part.
- Un gestionnaire de mots de passe peut remplir un champ par son extension. L'agent ne lit jamais un mot de passe.

## Ce qui attend l'accord écrit du propriétaire
- Une écriture en production, un déploiement manuel, une suppression en masse.
- Une PR qui touche la sécurité, le paiement, une migration de schéma, la CI ou le contrat de l'API mobile, même verte.
- Une dépense de crédits payants au-delà d'un essai.
- Tout ce qui sort du projet : un e-mail, un post.

## Les PR et le code
- Une branche dédiée, une PR par étape. Jamais de commit sur `main`. Quand l'humain dit « une seule PR », tous les chantiers liés y vont, même si elle grossit.
- Fusionne une petite PR quand la CI est verte et que les gros tests passent, sauf une surface sensible (voir ci-dessus). Jamais sur un rouge, même « connu ».
- **Une fonction est livrée quand sa PR est fusionnée.** Fusionne depuis le fil dès que c'est vert, sans attendre une autre session. Au début d'une tâche, liste les PR ouvertes : une vieille PR est fusionnée, ou fermée avec sa raison.
- Le code d'un build envoyé au store est sur `main`.
- **Pas de commentaires dans le code** : un nom clair, une petite fonction, un test.
- **Des tests qui prouvent** : e2e fullstack (build de prod, API, vraie base), intégration, golden. Les tests unitaires seulement là où ils prouvent quelque chose.
- **Le dépôt garde le code, les skills et les images que l'app embarque.** Les rendus, essais et visuels de posts vivent hors du dépôt, dans le dossier partagé.
- **Pas de code mort** ni de « version 2 » : construis moins et finis-le. Git garde l'histoire.
- **La performance est une règle** : un geste en une frame, une ouverture en moins de 100 ms, une lecture serveur en moins de 10 ms, chaque budget mesuré.
- **Parité web et iOS** quand une app a les deux clients.
- Discute l'architecture avant d'écrire une nouvelle brique : un fichier de conception court, puis un go.

## Les tests et les preuves
- Un test vert doit prouver quelque chose. Si un test passe alors que la fonction manque, le test est faux.
- **Zéro test instable** : un test instable n'est pas déterministe. Corrige sa cause, jamais de relance automatique, de délai plus long ni de skip. Un rouge se lit dans le résumé du job, sans artefact à télécharger.
- **Une bascule de prod se répète d'abord** sur une copie, avec le retour arrière et sa garde prêts, puis se vérifie de bout en bout.
- Mesure avant de toucher. Corrige la cause, pas le symptôme. N'affaiblis jamais un garde-fou pour passer.
- Ne te fie jamais à ta mémoire pour un outil, un prix ou du matériel : cherche en ligne.
- Vérifie tes affirmations dans l'app avant de les envoyer.
- Utilise la bonne source, pas un homonyme (le bon dépôt, le bon auteur).

## Les références partagées
- Une vidéo, un article ou un post partagé par l'humain : trouve son **idée centrale** et applique-la, relis la source avant de proposer. Rater l'idée pour un détail voisin est l'erreur à éviter.
- Une idée validée sur une app part dans **toutes les apps** du portefeuille, un fil par app. Un audit (conformité, store, sécurité) passe aussi toutes les apps.

## Les retours
- Un retour d'utilisateur se discute, il ne s'applique pas tel quel.
- On ne casse pas une review App Store en cours pour un petit correctif : la version suivante attend, les testeurs utilisent TestFlight.

## Le texte et l'interface
- Tout texte visible suit [`write-copy`](../../write-copy/SKILL.md) : la règle des 75 %, les mots de la personne, FR et EN, tutoiement.
- Tout écran suit [`design-interface`](../../design-interface/SKILL.md) et le `DESIGN.md` du projet.

## La sécurité et les secrets
- Aucun secret dans un dépôt ni dans une conversation. Un secret vit dans un fichier `chmod 600` sur la machine qui s'en sert, ou dans l'environnement d'un conteneur. Un fichier `SECRETS.md` nomme les variables et dit où elles vivent, jamais leur valeur.
- Préfère un connecteur MCP à une clé collée.
- Un audit de sécurité se fait isolé (sandbox) : l'outil analysé ne doit pas pouvoir infecter la machine qui l'analyse.
- Un outil installé est critiqué, télémétrie comprise.
- Aucune donnée de santé ni personnelle dans l'analytique. La politique de confidentialité suit chaque changement.

## Parler à l'humain
- **Un « c'est fait » répond à la question qu'il clôt** : relis les demandes ouvertes et vérifie laquelle avant d'agir.
- **Présente chaque travail fini comme le dit [`present-work`](../../present-work/SKILL.md)** : un titre humain, une description courte, des captures ou un diagramme, puis le lien vers le détail.
- Court, en commençant par ce qu'il doit faire, ou en disant qu'il n'a rien à faire.
- Sans jargon de fil : quand tu remplaces ou annonces quelque chose, dis ce que c'est (la source, ce qu'on voit) avec le lien d'aperçu.
- Une proposition de design ou de contenu arrive avec son visuel et son coût s'il y a des générations payantes.
- Dans sa langue. Les identifiants de code, les règles et les skills en anglais.
- Préviens-le de chaque sortie sur les stores.
- Quand il ajoute un outil, note-le en une ligne dans le `CLAUDE.md`.
