# <Nom du site>

<Une phrase : ce que fait le site.> En ligne sur `https://<sous-domaine>.<ton-domaine>`, servi par nginx sur Dokploy.

## Avant toute tâche
- Si une mémoire MCP est branchée, lis ses leçons `work.agents`, `copy`, `design` et `web.create`.

## Les règles
- `main` est la prod : une branche, une PR, jamais de push sur `main`.
- **Présente chaque travail fini** pour un non-technique : un titre humain, une description courte, des captures ou un diagramme, puis le lien vers le détail (skill `present-work`).
- Vérifie chaque changement dans un vrai navigateur, sur téléphone et sur ordinateur, et regarde la console.
- Le texte suit le skill `write-copy`, l'interface suit `design-interface`. Pas d'eyebrow, pas de phrases d'aide, un seul CTA par écran.
- Aucun secret dans le dépôt. Les variables vivent dans l'environnement du service Dokploy.
- DNS : le CLI ou l'API du registrar, après un instantané de la zone. Jamais à la main.

## Lancer en local
```bash
python3 -m http.server 8000 --directory www
```
