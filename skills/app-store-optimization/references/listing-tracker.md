# La page de suivi de la fiche

Une page vivante (un document partagé ou une page HTML) que l'agent tient à jour, et un relevé automatique deux fois par semaine (un déclencheur planifié, par exemple le lundi et le jeudi matin). À chaque passage : lire les chiffres, ajuster, et dire en trois lignes ce qui a bougé et si l'humain a quelque chose à faire.

## Les sections
1. **Où on en est** : la version en ligne, la version en review, ce qui part avec la suivante. Une ligne « Tu as à faire : … » ou « Rien à faire ».
2. **Par langue** : nom, sous-titre, mots-clés, texte promotionnel, description, pour la version en ligne et la suivante, côte à côte.
3. **Les captures** : la série en ligne et la nouvelle, par langue, avec leurs légendes.
4. **L'en-tête et l'image de recherche** : ce qui est posé, ce qui est testé.
5. **Les pages produit personnalisées** : chaque page, ses mots-clés, son lien `ct=`, son état chez Apple.
6. **Les événements et les nominations** : dates, état.
7. **Les chiffres** : impressions, vues, conversion par source et par page, téléchargements, essais, payants, avis et note. Les objectifs à côté.
8. **Le journal** : une ligne datée par changement envoyé à Apple, et par décision.

## Les règles
- Chaque valeur vient de l'API ou du CLI, jamais d'une saisie à la main.
- Une valeur que l'agent ne connaît pas s'affiche comme inconnue, jamais devinée. L'âge de chaque chiffre est écrit (« lu il y a 2 h »).
- Le suivi s'arrête à une date fixée d'avance ; après quelques passages sans changement, l'agent dit ce qui bloque et s'arrête.
