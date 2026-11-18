---
name: app-onboarding
description: Concevoir et livrer l'onboarding d'une app mobile, du premier écran au premier usage (accueil, questions, moment aha, rappels, plan, compte). Le paywall a son propre skill, app-paywall. À utiliser dès qu'on crée une app, qu'on touche à son accueil ou à son premier lancement, ou quand on parle d'« onboarding », de « moment aha » ou d'un onboarding « trop long ».
---

# L'onboarding d'une app

Ce skill ne dit que ce qui est propre à l'onboarding. Le texte suit [`write-copy`](../write-copy/SKILL.md), l'interface suit [`design-interface`](../design-interface/SKILL.md), le paywall suit [`app-paywall`](../app-paywall/SKILL.md). Le cas complet d'une app de santé payante est dans [`references/case-study.md`](references/case-study.md), les études du marché dans [`references/market-studies.md`](references/market-studies.md).

## Avant de commencer
1. Lis les leçons `app.onboarding`, `copy` et `design` de la mémoire, s'il y en a une ([`memory-first`](../memory-first/SKILL.md)).
2. Lis le `CLAUDE.md` et le `DESIGN.md` de l'app.
3. Pas d'étude d'audience ? Fais-la d'abord ([`audience-study`](../audience-study/SKILL.md)).

## Les principes
1. **Amène au premier moment aha le plus vite possible.** Pas de visite des fonctions : personne ne les retient. Un peu de personnalisation, puis la personne sent ce qu'elle gagne. Dans l'étude de cas, le aha est passé de la 9e à la **3e étape**.
2. **Le aha marche partout, en moins d'une minute.** Elle est peut-être dans le métro. Il dure 20 à 40 s, marche sans le son (le texte et les vibrations guident, la voix se coupe d'un geste) et ne demande pas d'être chez soi. Il donne une réussite réelle, dite seulement après qu'elle l'a confirmée (« Tu l'as trouvé »).
3. **Le aha se sent énorme.** Le geste est petit, la fête est grande : le dessin, l'haptique de réussite, une phrase qui la nomme. C'est là que le chat se sent tigre.
4. **Garde les questions qui personnalisent.** Seulement celles qui changent le plan, chacune dit pourquoi en une ligne. Les couper pour faire court fait baisser la conversion (Headspace : +10 % avec plusieurs objectifs).
5. **Les rappels juste après une petite réussite**, en montrant la vraie notification, avec « Continuer sans rappel ».
6. **Le plan montre qui elle devient** (« Aujourd'hui, tu deviens celle qui s'en occupe »), juste avant le paywall.
7. **Après le paywall, l'action, pas un tour.** « Ma première séance » ouvre vraiment l'usage. Sinon, « Rappelle-moi ce soir » ou « Rappelle-moi demain » programme **un seul** rappel, choisi selon l'heure : après 17 h, on continue demain. Le tour complet et les explications vivent dans l'app.
8. **Le compte, le plus tard possible**, ou jamais si l'app n'en a pas besoin. Duolingo gagne environ 20 % d'utilisateurs actifs en repoussant l'inscription. Sur iOS, « Continuer avec Apple » d'abord.

## La séquence de départ

| # | Écran | Rôle |
|---|---|---|
| 1 | Bienvenue | Une promesse qui parle d'elle, un bouton |
| 2 | Où en es-tu ? | 1 ou 2 choix qui personnalisent la suite |
| 3 | **Le aha** | Le geste guidé, court, partout, puis « Tu l'as senti ? » et la réussite |
| 4-6 | Personnalisation | Seulement les questions qui changent le plan |
| 7 | Comment nous as-tu connus ? | Pour l'acquisition (choix + « Autre ») |
| 8 | Préférences | Voix, vibrations, en montrant |
| 9 | Rappels | La vraie notification qui défile |
| 10 | Le plan est prêt | Qui elle devient, une animation qui pousse |
| 11 | Paywall | Voir [`app-paywall`](../app-paywall/SKILL.md) |
| 12 | C'est parti | « Ma première séance » ou un seul rappel |

Une étape qui n'aide ni le aha, ni le plan, ni le paywall sort du chemin.

## La méthode
1. **L'étude d'audience** dans un fil à part ([`audience-study`](../audience-study/SKILL.md)).
2. **Trouver le aha** : le plus petit geste qui fait sentir la valeur de l'app, en moins d'une minute et sans matériel. Pour une app d'exercices, une contraction guidée de 40 s. Pour Photoroom, le premier détourage. Pour Calm, la première respiration. Si tu ne sais pas, fais étudier les meilleurs onboardings de la catégorie par un agent dédié, qui revient avec ce qu'on garde, ce qu'on retire et ce qu'on améliore.
3. **Dessiner la séquence** à partir du gabarit, puis la maquette jouable ([`design-interface`](../design-interface/SKILL.md)).
4. **Écrire le texte** comme une seule histoire, puis le faire relire par les deux agents de [`write-copy`](../write-copy/SKILL.md).
5. **Le mouvement** : un seul décor qui se transforme, le bouton fixe, une haptique par étape.
6. **Mesurer** : un événement `onboarding_step_completed` (`step`, `action`) à chaque étape, puis `onboarding_completed` avec ce qui s'est passé à la fin (première séance tout de suite ou non). Une réponse qui est une donnée de santé ne part pas. Un funnel écran par écran, dans l'ordre réel des étapes, remis à jour quand l'ordre change.
7. **Montrer** : des captures, puis une vidéo du parcours complet à vitesse réelle, en FR et en EN.

Livre la V1 au mieux, puis l'analytique décide de la suite.

## Avant de livrer
- [ ] Le aha arrive avant le 4e écran, dure moins d'une minute et marche sans le son.
- [ ] Ni interrupteur ni formulaire sur l'écran du aha.
- [ ] Chaque question change le plan, et dit pourquoi.
- [ ] Après le paywall, l'action principale ouvre vraiment l'usage.
- [ ] Le compte arrive à la fin, ou pas du tout.
- [ ] Les événements sont posés, le funnel suit l'ordre réel, aucune donnée de santé.
- [ ] Les checklists de [`write-copy`](../write-copy/SKILL.md) et [`design-interface`](../design-interface/SKILL.md) sont passées.
- [ ] La vidéo du parcours est envoyée.

## À éviter
- La visite des fonctions, et le tour complet avant le paywall.
- Un exercice long et sonore obligatoire avant le paywall.
- Optimiser les seuls débuts d'essai : regarde ce que les abonnés paient vraiment.
- Prendre les chiffres des vendeurs (RevenueCat, Superwall…) pour des causes.
