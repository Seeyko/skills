# Les secrets

Aucune valeur ici. Chaque ligne dit le nom, qui s'en sert, et où il vit.

| Nom | Qui s'en sert | Où il vit |
|---|---|---|
| `ANTHROPIC_API_KEY` | l'API | Dokploy, service `api`, onglet Environment |
| Clé App Store Connect (.p8), issuer | `asc`, l'envoi TestFlight | `~/.appstoreconnect` sur le Mac de build (`chmod 600`) |
| Clé PostHog `phc_…` | l'app | dans le code : elle est publique par nature |
