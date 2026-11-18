---
name: write-copy
description: Écrire ou relire tout texte qu'une personne lira (écran d'app, bouton, onboarding, paywall, fiche App Store, site, e-mail, post). Retire ce qui sonne « IA », garde les mots de la personne, promet ce qui est vrai. À utiliser dès qu'on écrit ou change une seule chaîne visible, ou quand on entend « ça fait IA », « reformule », « trop de texte ».
---

# Écrire le texte

Ce skill vaut pour tous les projets et tous les écrans. Le skill de wording du projet, s'il existe, gagne sur le ton. Un exemple complet (une app de santé) est dans [`references/example-health-app.md`](references/example-health-app.md).

## Les outils
Passe chaque texte par :
- **`humanizer`**, qui retire les signes d'un texte écrit par une IA (d'après le guide « Signs of AI writing » de Wikipédia) ;
- les **marketingskills** de Corey Haines (`copywriting`, `copy-editing`, `marketing-psychology`, et `onboarding`, `paywalls`, `aso` selon l'écran) ;
- l'échelle de suppression ci-dessous.

S'ils ne sont pas dans le projet, télécharge-les (voir [`../../CREDITS.md`](../../CREDITS.md)).

## La règle des 75 %
Sur chaque écran, retire 75 % de ce qui fait que l'écran sonne « IA » : l'eyebrow, le sous-titre gris, le texte d'aide, le paragraphe qui explique, la légende qui répète l'image, l'emoji décoratif. Ce n'est pas le texte qui fait comprendre un écran. S'il ne se comprend pas sans texte, on corrige le dessin.

## L'échelle de suppression
Pour chaque texte, arrête-toi à la première question qui s'applique, et supprime :
1. **Doit-il apparaître ?** Coupe le texte qui répond à une question que la personne ne se serait jamais posée.
2. **Le libellé doit-il exister ?** Coupe la légende qui répète un libellé ou une valeur. Garde les unités.
3. **Anticipe-t-il une inquiétude ?** Coupe le texte qui écarte un échec, défend un choix de design ou décrit un bug corrigé.
4. **Réécris-le ou retire-le.** S'il ne reste rien, supprime l'élément.

Ce qui survit : une vraie conséquence au moment du choix, un fait invisible (compatibilité, portée), ce que veut dire un état vide et quoi faire ensuite, les unités.

## La charte
- Un écran porte **un titre** et, seulement si c'est indispensable, **une ligne courte**.
- Le détail existe, mais derrière un tap.
- Une consigne tient en quelques mots, à l'impératif, comme la dirait la personne du métier.
- Un bouton dit l'action et, s'il le faut, la durée : « Ma séance · 7 min ».
- **Les mots de la personne, pas les tiens.** Ne suppose jamais qu'elle connaît ton vocabulaire. Une image de l'univers de l'app se dit en clair la première fois.
- Dis pourquoi, en une phrase.
- Des phrases de 20 mots au plus, à l'actif, au présent. Le tutoiement, sauf si le projet en a décidé autrement. Relis à voix haute.
- **Une seule histoire** : les écrans d'un parcours s'enchaînent comme un récit. Aucun texte n'en répète un autre. Les titres se lisent à la suite.
- Toutes les langues du produit ensemble (FR et EN par défaut), dès le premier écran. Si une voix lit le texte, chaque changement oblige à re-rendre la voix : réutilise les phrases déjà enregistrées.
- Quand tu réécris le texte de quelqu'un, garde exactement son ton et change le contenu.
- **Le test du doigt** : cache chaque texte avec le doigt. Si l'écran se comprend encore, supprime ce texte.

## Vendre la personne d'après
**Un chat doit se sentir tigre.** Le texte montre la personne qu'elle va devenir, pas l'interface. Le tigre n'est pas un idéal inaccessible : c'est elle, en mieux, ou redevenue elle-même. L'étude d'audience dit qui est ce tigre (skill [`audience-study`](../audience-study/SKILL.md)).

Trois moments où le produit la nourrit :
1. **Elle est crue** : on reconnaît ce qu'elle vit, sans le minimiser.
2. **Elle réussit** : on nomme sa réussite, seulement après qu'elle l'a confirmée.
3. **Elle tient** : quelque chose de visible grandit avec elle.

On dit ce qu'elle a réussi, jamais ce qu'elle a manqué (« on y revient demain », pas « tu as oublié »). Pas de compliment gonflé.

## Promettre ce qui est vrai
Promets fort ce qu'elle vivra dans le produit (un ressenti, un accompagnement, une régularité, une réussite). Ne promets jamais un résultat que le produit ne peut pas garantir. Classe chaque promesse :
- **Vert** : on le dit partout.
- **Orange** : on le reformule, ou on l'ancre dans un fait du produit.
- **Rouge** : jamais. Un résultat chiffré, une caution d'un professionnel, « scientifiquement prouvé », un effet sur un symptôme.

Un bouton ne promet que ce que l'écran suivant donne.

## Avant de livrer
- [ ] Chaque écran a passé la règle des 75 % et l'échelle de suppression.
- [ ] Aucun texte n'en répète un autre, et les titres se lisent comme une histoire.
- [ ] Aucune promesse rouge.
- [ ] FR et EN, relus à voix haute.
- [ ] Relu par deux agents en parallèle qui ne voient que la matière brute ([`copy-cutter`](../../agents/copy-cutter.md) et [`story-reviewer`](../../agents/story-reviewer.md)). Tu arbitres quand ils divergent.
