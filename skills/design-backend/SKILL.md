---
name: design-backend
description: Concevoir l'architecture d'un produit avant d'écrire du code - la vision, les questions à se poser sur la donnée, les écritures, les lectures, l'IA et la sécurité, puis un document court et un go. À utiliser au démarrage d'un back-end, avant une nouvelle brique (une table, un service, un agent, une dépendance), ou quand on demande « comment on architecture ça ? ».
---

# Concevoir un back-end

On discute l'architecture avant de coder. Le code d'un agent va vite ; ce qui coûte, c'est une mauvaise forme de la donnée. Ce skill donne les questions, pas les réponses : elles changent avec le produit. La stack est dans [`pick-stack`](../pick-stack/SKILL.md).

## L'ordre des documents
1. **La vision**, écrite avec le propriétaire, en une page : le produit en une phrase, ses couches, ce qui n'est pas négociable. Elle passe avant tout le reste.
2. **L'architecture** : la cible, le point de départ, le plan de construction. Elle commence par « en une page » avec un schéma, puis la liste courte des principes qui structurent tout.
3. **La spec** : le produit tel qu'il est en production.

Si le code, une règle ou une spec contredit la vision ou l'architecture, on s'arrête et on le dit. Un document dit l'état actuel ou la cible, jamais l'histoire.

## Avant de dessiner
- **Lis ce qui existe.** Les systèmes qui ont résolu le même problème, leurs articles, leurs mesures publiées, leurs points faibles avoués. Cite chaque source avec sa date.
- **Écris pourquoi ce modèle**, et ce qui est écarté avec sa raison. Sans la liste des écartés, la question reviendra.
- **Pars de ce qu'il y a.** Pour chaque pièce existante, un verdict : reprendre, adapter, jeter. Une pièce reprise est relue et mesurée dans l'étape qui en a besoin, jamais avant.

## Les questions

**La donnée**
- Qu'est-ce qui est la vérité, et qu'est-ce qui n'est qu'un cache qu'on peut recalculer ?
- Garde-t-on ce qui entre tel quel, pour le retraiter quand les modèles seront meilleurs ?
- À qui appartient une donnée ? Quand elle se partage, est-ce une copie, et qui garde le dernier mot ?
- Deux fois la même chose : on fusionne, ou on relie ? Peut-on revenir en arrière ?
- Comment efface-t-on vraiment la donnée d'une personne ?

**Les écritures et les lectures**
- Chaque type d'objet a-t-il ses propres champs ? Ce qui est commun reste commun, sinon un champ ajouté pour un type pollue tous les autres.
- Tout ce qui est fait se rattache-t-il à une vraie personne ? Pas de jeton personnel partagé : on doit savoir qui a fait quoi.
- Y a-t-il un seul chemin d'écriture, avec ses droits, sa trace et son annulation ?
- Que lit l'app : une vue déjà calculée, ou des tables qu'elle assemble ?
- Que voit la personne hors ligne, et que devient son geste ?
- Quel est le budget de chaque geste, en millisecondes, et qui le mesure ? Le banc de mesure existe dès la première table.

**L'IA**
- Le chemin d'un geste appelle-t-il un modèle ? Il ne devrait jamais : on répond tout de suite, le résultat arrive après.
- Quand le système ne sait pas, que montre-t-il ? « Inconnu », avec l'âge de la donnée. Jamais une valeur inventée.
- Une même exécution a-t-elle à la fois des données privées, du contenu qui vient d'ailleurs et une sortie vers l'extérieur ? Jamais les trois ensemble.
- Quelles actions demandent un « oui » humain ? Tout ce qui efface, partage, envoie, ou dont un argument vient d'une donnée non fiable.
- Change-t-on de fournisseur de modèle en une ligne ? Un modèle se choisit par un test sur de vraies phrases, pas par sa taille.
- Les assistants des gens peuvent-ils s'y brancher ? Les noms d'outils restent stables.

**Le périmètre**
- Peut-on tout faire tenir dans une seule base, sans service de plus ? L'option la plus simple est souvent celle qui n'ajoute aucun fournisseur.
- Si un fournisseur tombe, que se passe-t-il ? Le code ne connaît de lui qu'une adresse et une correspondance, pour pouvoir en changer ou en avoir deux.
- Si on repart de zéro, se limite-t-on à cause de l'existant ? Une refonte vise le plus propre, sans sur-construire. Ce qui est remplacé est supprimé, pas gardé à côté.
- Quel est le plus petit périmètre qu'on peut finir parfaitement ? On ne découpe pas en « version 1 » et « version 2 » : on construit moins.
- Qu'est-ce qui doit être là dès la première ligne, parce qu'on ne l'ajoute pas après ? La sécurité et le cloisonnement.

## La sécurité
Un tableau « menace, parade », écrit avec l'architecture. Chaque parade a son test.

## Le document, puis le go
- Un fichier court : le modèle de données, la vue, les gestes, les budgets.
- **Les questions ouvertes qui bloquent**, en tableau : la question, ce qu'elle bloque, la recommandation. Le propriétaire ne tranche que les vrais problèmes de produit ou d'architecture.
- Pas de code avant le go. Quand le dessin change, l'architecture est mise à jour dans la même tâche.

## Vérifier
- [ ] La vision tient en une page, et le propriétaire l'a écrite ou validée.
- [ ] Chaque choix dit pourquoi, et ce qui a été écarté.
- [ ] Chaque budget a sa mesure.
- [ ] Le tableau des menaces existe, avec un test par parade.
- [ ] Les questions ouvertes ont chacune une recommandation.
