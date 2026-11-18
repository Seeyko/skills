---
name: sync-memory
description: Mettre les leçons d'une mémoire MCP au niveau de memoire/lecons.json (ajouter, réviser, retirer). À lancer après la fusion d'une PR qui touche memoire/lecons.json, la première fois qu'on branche une mémoire, ou sur « synchronise la mémoire ».
---

# Synchroniser la mémoire

`memoire/lecons.json` est la source. La mémoire MCP en garde une copie que tous les agents lisent.

## Étapes
1. Lis `memoire/lecons.json` sur `main`.
2. Choisis l'espace de la mémoire (celui de la personne ou du projet).
3. Pour chaque sujet du fichier, lis les leçons de la mémoire. Repère celles dont le `source` commence par `playbook:` : leur clé suit, jusqu'au premier espace.
4. Pour chaque leçon du fichier :
   - `status: "retired"` et une leçon de même clé dans la mémoire : retire-la.
   - une leçon de même clé : compare rule, when, why, check, topic. Révise ce qui a changé.
   - aucune leçon de même clé : ajoute-la, avec `source` = `playbook:<clé> · <page>`.
5. Ne touche jamais une leçon de la mémoire sans clé `playbook:` : d'autres agents en écrivent.
6. Relis chaque sujet : chaque règle du fichier y est, une seule fois.

## Quand la mémoire a une leçon que le dépôt n'a pas
Un agent l'a apprise en route. Si elle vaut pour tout le monde (pas un fait personnel), ajoute-la au fichier et à la page du sujet dans une PR. Sinon laisse-la dans la mémoire.
