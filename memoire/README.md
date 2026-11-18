# Les leçons pour une mémoire MCP

Si tes agents ont un MCP de mémoire qui garde des leçons par sujet (des outils du type `lessons_read`, `lesson_add`, `lesson_revise`, `lesson_retire`), ce dossier lui donne les règles courtes du playbook. Chaque leçon renvoie à la page qui a le détail.

`lecons.json` est la source de vérité de ces leçons. Un champ par leçon :

| Champ | Contenu |
|---|---|
| `key` | un nom stable, `sujet/nom-court` |
| `topic`, `rule`, `when`, `why`, `check`, `source` | les champs d'une leçon (limites : 60, 1000, 200, 400, 300, 200 caractères). `source` commence par `playbook:<key>`, pour retrouver la leçon dans la mémoire. |
| `status` | `retired` pour retirer la leçon ; absent sinon |

Changer une leçon : modifie la page du sujet et la leçon dans la même PR. `scripts/check-lecons.py` vérifie le fichier (aussi en CI). Après la fusion, le skill [`sync-memory`](../skills/sync-memory/SKILL.md) met la mémoire à jour.

Ce qui est personnel (tes machines, tes comptes, tes projets) va dans des notes de ta mémoire, pas ici.
