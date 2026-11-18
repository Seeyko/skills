---
name: present-work
description: Présenter un travail fini de façon simple et lisible par un non-technique : un titre humain, une description courte, des captures ou un diagramme, puis le lien vers le détail. À utiliser chaque fois qu'un agent finit une tâche, ouvre ou met à jour une PR, ou rend un résultat (« c'est fait », « voici la PR », un rapport de fin).
---

# Présenter son travail

Chaque fois que tu finis un travail, présente-le pour qu'un chef de produit le comprenne en une minute, même si la personne qui relit est technique : c'est elle qui décide de la suite.

## Le format, dans cet ordre
1. **Un titre humain.** Il dit ce qui change pour la personne qui utilise le produit, pas comment c'est codé. « Le paywall montre la date du premier paiement », pas « feat(paywall): add TrialTimeline view ». Pas de jargon, pas de nom de fichier, pas de préfixe technique.
2. **Une description lisible.** Trois à cinq phrases ou puces : ce qui a changé, pourquoi, ce qu'il reste à faire (ou « rien à faire »). Ce que la personne doit faire vient en premier.
3. **Des images.** Des captures avant et après de chaque écran touché, ou un diagramme pour un changement sans écran (architecture, flux de données, CI). Quand il y a un écran ou un flux à montrer, l'image passe avant le texte. Une vidéo à vitesse réelle pour un parcours.
4. **Le lien vers le détail**, à la fin : la session de l'agent, un document de conception ou d'analyse. Pour un chantier technique avec des phases de conception, lie aussi ces documents. Le détail est là pour qui le veut, jamais dans le chemin.

## Sur une PR
- Le titre de la PR suit la règle 1. Le corps suit 2, 3, 4, avec les captures dans la description (envoyées dans la PR, jamais commitées).
- Ce qui est technique (fichiers touchés, tests lancés, chiffres de performance) va dans une section repliée en bas, ou dans le lien.

## Dans une réponse de fin
- La même chose, en plus court : le résultat, l'image s'il y a quelque chose à voir, le lien. Pas de récit de ce que tu as fait.

## Vérifier
- [ ] Le titre se comprend sans connaître le code.
- [ ] Une personne qui ne lit que le titre et regarde les images sait ce qui a changé.
- [ ] Ce que la personne doit faire (ou « rien à faire ») est dit en premier.
- [ ] Le lien vers le détail est là.
