---
name: app-onboarding
description: Concevoir, écrire et livrer l'onboarding d'une app mobile (accueil, questions, moment aha, rappels, paywall, premier usage). À utiliser dès qu'on crée une app, qu'on touche à son accueil ou à son paywall, ou quand on parle d'« onboarding », d'« accueil », de « premier lancement », de « moment aha », de « paywall » ou d'un onboarding « trop long ».
---

# L'onboarding d'une app

Le cas complet d'une app de santé payante est dans [`references/etude-de-cas.md`](references/etude-de-cas.md). L'étude d'audience modèle est dans [`references/etude-audience.md`](references/etude-audience.md), le paywall détaillé dans [`references/paywall.md`](references/paywall.md), les études de cas du marché dans [`references/etudes.md`](references/etudes.md) et les règles de texte dans [`references/copy.md`](references/copy.md).

## Avant de commencer

1. Si une mémoire MCP est branchée, lis ses leçons `app.onboarding` et `app.create` (skill [`memory-first`](../memory-first/SKILL.md)). Une leçon plus récente que ce fichier gagne.
2. Lis le `CLAUDE.md` et le `DESIGN.md` de l'app. Leur charte gagne sur ce skill pour le style.
3. Si l'app n'a pas d'étude d'audience, fais-la d'abord (étape 1). Sans elle, on n'écrit pas une ligne.

## Les principes

1. **Amène au premier moment aha le plus vite possible.** Pas de visite des fonctions. Un peu de personnalisation, puis la personne comprend ce qu'elle gagne, par un vrai ressenti de satisfaction. Dans l'étude de cas, le aha est passé de la 9e à la **3e étape**.
2. **Le aha se fait partout, en moins d'une minute.** Elle est peut-être dans le métro. Le aha dure 20 à 40 s, marche sans le son (le texte et les vibrations guident, la voix se coupe d'un geste) et ne demande pas d'être chez soi. Il donne une réussite réelle, dite seulement après qu'elle a confirmé (« Tu l'as trouvé »).
3. **Un chat doit se sentir tigre.** L'onboarding et la fiche App Store font le même travail : elle se voit déjà réussir, en mieux. Au paywall, elle veut tellement devenir la personne « d'après » qu'elle paie. Le tigre n'est pas une athlète : c'est elle, redevenue elle-même.
4. **Promets le ressenti, jamais un résultat médical.** On promet fort ce qu'elle vivra dans l'app (ressenti, accompagnement, régularité, réussite). On ne promet jamais un effet sur un symptôme. Listes verte, orange et rouge dans [`references/copy.md`](references/copy.md).
5. **Une seule histoire.** Les écrans s'enchaînent comme un récit, sans texte répété, avec des encouragements. Cinq étapes avec cinq textes qui se répètent, c'est raté. Exemple de récit : trouver le geste, l'avoir trouvé, puis voir l'univers de l'app se préparer autour d'elle.
6. **Retire 75 % du slop, écran par écran.** Un titre et, au plus, une ligne courte. Pas d'eyebrow, pas de sous-titre gris, pas de paragraphe. Le détail va derrière un tap.
7. **L'écran ne change jamais vraiment.** Le bouton reste fixe et seul le contenu se transforme. Les étapes ne glissent pas : le contenu s'efface dans un flou et le suivant arrive sur place. Le libellé du bouton se fond sur place, un temps après. Peu de cartes : le texte est posé sur le fond.
8. **Montre au lieu d'expliquer.** Une notification qui fait défiler les vrais rappels remplace la phrase qui les décrit. Une graine qui pousse remplace « ton plan est prêt ». Chaque étape a son retour haptique.
9. **Pas de réglage lourd dans un écran d'expérience.** Pas d'interrupteur sur l'écran du aha : un petit bouton rond (un haut-parleur) suffit.
10. **Un paywall dur, honnête, à la fin.** Juste après la réussite et le plan. L'annuel est présélectionné, avec un essai de 7 jours et la frise de l'essai (aujourd'hui, jour 5 on te rappelle, jour 7 premier paiement). La frise répond à la peur de l'abonnement caché. Le bouton juste avant ne promet rien que le paywall ne donne. Détail : [`references/paywall.md`](references/paywall.md).
11. **Après le paywall, l'action, pas un tour.** « Ma première séance » ouvre vraiment l'usage. Sinon, « Rappelle-moi ce soir » ou « Rappelle-moi demain » programme **un seul** rappel, choisi selon l'heure : après 17 h, on continue demain. Le reste (le tour complet, les explications) vit dans l'app.
12. **Le compte, le plus tard possible.** À la fin de l'onboarding, ou jamais si l'app n'en a pas besoin. Duolingo gagne environ 20 % d'utilisateurs actifs en repoussant l'inscription. Sur iOS, « Continuer avec Apple » d'abord.
13. **La V1 au mieux, puis l'analytique décide.** Chaque étape envoie un événement. Aucune donnée de santé ne part.

## La méthode

### 1. Étudier pour qui on écrit (agent dédié)
- Pose la question : à quel problème répond l'app, dans quel état d'esprit arrivent les personnes, et quels sont leurs profils ?
- Lance l'étude dans un agent ou un fil à part (le modèle le plus fort), pas dans celui qui code.
- Livrables : l'état d'esprit à l'arrivée (honte, doute, fatigue…), les profils (pour chacun : qui elle veut devenir, ce qu'on lui dit, ce qu'on ne dit pas, ce que dit la science), ses mots à elle (et les mots interdits), les méfiances avant de payer et la réponse de l'app, les promesses vertes, orange et rouges, ce que ça change dans l'onboarding et sur la fiche.
- Gabarit et exemple complet : [`references/etude-audience.md`](references/etude-audience.md).

### 2. Trouver le moment aha
- Quel est le plus petit geste qui fait sentir la valeur de l'app, en moins d'une minute et sans matériel ? Pour une app d'exercices, une contraction guidée de 40 s. Pour Photoroom, le premier détourage. Pour Calm, la première respiration.
- Si tu ne sais pas, fais étudier les meilleurs onboardings de la catégorie par un agent dédié. Il revient avec ce qu'on garde, ce qu'on retire et ce qu'on améliore.

### 3. Dessiner la séquence
Gabarit de départ :

| # | Écran | Rôle |
|---|---|---|
| 1 | Bienvenue | Une promesse qui parle d'elle (« pour te sentir à nouveau toi »), un bouton |
| 2 | Où en es-tu ? | 1 ou 2 choix qui personnalisent la suite |
| 3 | **Le aha** | Le geste guidé, court, partout, puis « Tu l'as senti ? » et la réussite |
| 4-6 | Personnalisation | Seulement les questions qui changent le plan, chacune dit pourquoi en une ligne |
| 7 | Comment nous as-tu connus ? | Pour l'acquisition (choix + « Autre ») |
| 8 | Préférences | Voix, vibrations… en montrant, pas en expliquant |
| 9 | Rappels | La notification réelle qui défile, « Activer mes rappels » / « Continuer sans rappel » |
| 10 | Le plan est prêt | Qui elle devient (« Aujourd'hui, tu deviens celle qui s'en occupe »), une animation qui pousse |
| 11 | Paywall | Annuel présélectionné, essai, frise, « J'ai un code » |
| 12 | C'est parti | « Ma première séance » ou un seul rappel |

Une étape qui n'aide ni le aha, ni le plan, ni le paywall sort du chemin.

### 4. Écrire le texte
- Passe chaque texte par `humanizer`, les marketingskills de Corey Haines (`onboarding`, `paywalls`, `copywriting`, `copy-editing`, `marketing-psychology`) et les règles de [`references/copy.md`](references/copy.md). Télécharge-les s'ils ne sont pas dans le projet.
- Puis fais relire par **deux agents en parallèle** qui ne voient que la matière brute. Le premier applique la grille de suppression. Le second relit le récit et le ressenti avec l'étude d'audience. Chacun critique la proposition autant que l'existant et tranche les questions ouvertes. Tu arbitres quand ils divergent.
- FR et EN ensemble. Si une voix pré-enregistrée lit le texte, chaque changement oblige à re-rendre la voix : réutilise les phrases déjà enregistrées.

### 5. Le mouvement et le style
- Suis le `DESIGN.md` de l'app. Pour la méthode : `emil-design-eng`, `choreograph`, `review-animations`, `apple-design`, `swiftui-expert-skill` (voir [`../../methode/skills-et-createurs.md`](../../methode/skills-et-createurs.md)).
- Pour une vidéo de référence, fais deux analyses : la tienne, et celle d'un agent qui n'a **que la vidéo**. Garde ce qui converge.
- Chaque mouvement a sa version « Réduire les animations » (un simple fondu). Chaque contrôle a son haptique, sa cible de 44 pt et son libellé VoiceOver.

### 6. Mesurer
- Un événement par étape (`onboarding_step_completed` avec `step` et `action`), puis `onboarding_completed` avec ce qui s'est passé à la fin (première séance tout de suite ou non). Une réponse qui est une donnée de santé ne part pas.
- Un funnel « écran par écran » dans l'ordre réel des étapes. Remets-le à jour quand l'ordre change.

### 7. Montrer
- Des captures, puis une **vidéo du parcours complet à vitesse réelle**, en FR et en EN, avec des données réalistes.
- Une maquette HTML jouable des écrans clés (téléphones côte à côte, repères d'haptique et d'animation sous chacun) aide à valider avant de coder. Voir [`references/paywall.md`](references/paywall.md).

## Avant de livrer
- [ ] Le aha arrive avant le 4e écran, dure moins d'une minute et marche sans le son.
- [ ] Aucun écran ne répète le texte d'un autre. Les titres se lisent à la suite comme une histoire.
- [ ] Chaque écran a passé la règle des 75 % et l'échelle de suppression.
- [ ] Aucune promesse rouge (résultat médical, chiffre, caution d'un pro, « scientifiquement prouvé »).
- [ ] Ni interrupteur ni formulaire sur l'écran du aha. Peu de cartes.
- [ ] Le paywall montre l'essai et sa fin, et l'annuel est présélectionné. Rien n'est caché.
- [ ] Après le paywall, l'action principale ouvre vraiment l'usage.
- [ ] Les événements sont posés, le funnel suit l'ordre réel, aucune donnée de santé.
- [ ] FR et EN, VoiceOver, 44 pt, haptique, « Réduire les animations ».
- [ ] La vidéo du parcours est envoyée.

## À éviter
- La visite des fonctions et le tour complet avant le paywall : personne ne retient les fonctions montrées à l'accueil.
- Un exercice long et sonore obligatoire avant le paywall.
- Couper les questions pour faire court : celles qui personnalisent font monter la conversion (Headspace +10 %).
- Optimiser les seuls débuts d'essai : regarde ce que les abonnés paient vraiment.
- Prendre les chiffres des vendeurs (RevenueCat, Superwall…) pour des causes.
- « Fini les fuites », « Bravo championne », « c'est normal », « tu as oublié ».
