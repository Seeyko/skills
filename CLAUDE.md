# Agent playbook

Ce dépôt décrit une façon de travailler avec des agents. Il est en français. Les noms de fichiers et de skills sont en anglais.

## Avant toute tâche
- Si une mémoire MCP est branchée, lis ses leçons du sujet (skill `skills/memory-first`). Puis lis le skill qui couvre la tâche (voir `README.md`).

## Quand tu changes une règle ou un skill
- Écris la règle avec sa raison. Une règle dit quoi faire, quand, et comment vérifier.
- Une règle qui vaut pour tous les projets va dans un skill général (`write-copy`, `design-interface`, `work-with-agents`…), pas dans le skill d'une étape. Le skill d'une étape renvoie au skill général au lieu de le recopier.
- Dans la même PR, mets à jour `memory/lessons.json` : la leçon courte qui correspond, ajoutée, changée ou marquée `retired`. `python3 scripts/check-lessons.py` doit passer.
- Une leçon fausse est changée ou retirée, jamais gardée à côté de sa correction.

## La forme
- Rangé comme un plugin : `skills/<nom>/SKILL.md` et ses `references/`, `agents/<nom>.md`, `templates/`, `memory/`, et `scripts/` pour la vérification. Pas d'autre dossier.
- Minimal : un sujet vit à un seul endroit. Pas de doublon, pas de page d'index en plus du `README.md`.

## Ce dépôt reste partageable
- Aucune donnée personnelle : pas de nom de personne, de compte, d'adresse, de domaine privé, de machine, de testeur, de date de vie privée.
- Aucun secret, aucune IP, aucun e-mail.
- Aucun lien vers un contenu privé (artefact, document, conversation) : on copie le contenu utile ici, sous forme de skill ou de référence.
- Les exemples sont anonymes et parlent de méthode.

## Le texte
- Court, direct, tutoiement. Pas d'eyebrow, pas de phrases d'aide. Suis `skills/write-copy`.
