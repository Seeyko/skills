---
name: beta-by-sharing
description: Sortir une fonction nouvelle en bêta derrière un drapeau, et la laisser se diffuser par le partage - celui qui reçoit une invitation ou un lien entre dans la bêta à son tour. À utiliser quand on crée une fonction en bêta, qu'on demande « cache-la derrière un feature flag », ou qu'on ajoute un lien de partage ou une invitation à une fonction encore fermée.
---

# Une bêta qui se partage

Toute fonction nouvelle sort cachée derrière un drapeau, et se diffuse de bouche à oreille. Celle qui l'a peut inviter, défier ou partager un lien. Celle qui reçoit entre dans la bêta, et peut partager à son tour. La bêta grandit là où la fonction sert, sans campagne.

## Le modèle
1. **Visible veut dire : le drapeau est ouvert pour ce compte.** Le nom du drapeau est une constante du code. Aucune variable d'environnement n'ouvre une bêta.
2. **Ta base fait foi pour l'inscription.** Une ligne dit qui est entré, par quel geste, par quel objet et grâce à qui. C'est elle que l'on passe à l'outil de drapeaux, jamais une propriété stockée chez lui : n'importe qui peut l'écrire avec la clé publique.
3. **Le geste de partage inscrit.** Accepter un lien, être invitée, être défiée : le serveur écrit la ligne, et la fonction s'ouvre à la requête suivante.
4. **Un lien qui ouvre un droit porte un jeton aléatoire**, jamais le seul identifiant de l'objet. Un jeton absent ou faux répond comme un objet inconnu. Le jeton ne se donne qu'aux comptes qui peuvent déjà partager.
5. **Un coupe-circuit à toi**, qui ne dépend d'aucun service tiers, ferme la fonction pour tout le monde.

## À la sortie
Le drapeau et son code partent quand la fonction est ouverte à tous. Rien n'est gardé « au cas où ».

## Vérifier
- [ ] Sans inscription, la fonction ne se voit nulle part : ni écran, ni route, ni lien.
- [ ] Un lien partagé inscrit un compte neuf, qui peut partager à son tour.
- [ ] Un jeton faux et un objet inconnu donnent la même réponse.
- [ ] Le coupe-circuit ferme tout.
