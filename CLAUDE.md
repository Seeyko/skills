# Agent playbook

Ce dépôt décrit une façon de travailler avec des agents. Il est en français. Les noms de fichiers et de skills sont en anglais.

## Avant toute tâche
- Si une mémoire MCP est branchée, lis ses leçons du sujet (skill `skills/memory-first`). Puis lis la page de ce dépôt qui couvre la tâche (voir `README.md`).

## Quand tu changes une règle ou un skill
- Écris la règle avec sa raison. Une règle dit quoi faire, quand, et comment vérifier.
- Dans la même PR, mets à jour `memoire/lecons.json` : la leçon courte qui correspond, ajoutée, changée ou marquée `retired`. `python3 scripts/check-lecons.py` doit passer.
- Une leçon fausse est changée ou retirée, jamais gardée à côté de sa correction.

## Ce dépôt reste partageable
- Aucune donnée personnelle : pas de nom de personne, de compte, d'adresse, de domaine privé, de machine, de testeur, de date de vie privée.
- Aucun secret, aucune IP, aucun e-mail.
- Aucun lien vers un contenu privé (artefact, document, conversation) : on copie le contenu utile ici, sous forme de skill ou de référence.
- Les exemples sont anonymes et parlent de méthode.

## Le texte
- Court, direct, tutoiement. Pas d'eyebrow, pas de phrases d'aide. Passe le texte par `humanizer` avant de le publier.
