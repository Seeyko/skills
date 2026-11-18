---
paths:
  - "ios/<App>/**"
  - "web/www/**"
  - "DESIGN.md"
---

# Travail front : lire DESIGN.md d'abord

Avant d'écrire ou de modifier un écran, un composant, une animation ou le site :

1. Lis `DESIGN.md` en entier, même pour une petite tâche.
2. Relis la « Charte de design » de `CLAUDE.md` pour le texte. Si les deux se contredisent, la charte gagne.
3. Réutilise les composants de `ios/<App>/Design/` avant d'en créer un.

Les points qu'on oublie le plus :
- Pas de carte, de cadre ni de séparateur par défaut.
- Pas de couleur ni de police hors du thème.
- Un contenu en remplace un autre par fondu flou. Rien ne glisse sur le côté.
- Chaque contrôle a son haptique, sa cible de 44 pt, son libellé VoiceOver.
- Ce qui défile horizontalement ne défile qu'horizontalement.

## Les skills du dépôt
`swiftui-expert-skill`, `emil-design-eng`, `choreograph`, `review-animations`, `apple-design`, `learn-taste`. Ils donnent la méthode ; `DESIGN.md` donne le style et gagne en cas de désaccord.

## Quand le design change
Mets `DESIGN.md` à jour dans le même commit. Une correction du propriétaire devient une règle dans `DESIGN.md`, avec sa raison.
