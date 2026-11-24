# Portfolio 3.0 automatisé

## Installation
1. Sauvegarde ton dépôt GitHub actuel.
2. Remplace le contenu du dépôt `portefeuille3.0` par le contenu de cette archive (inclure `.github`).
3. Commit/push sur la branche configurée pour GitHub Pages.
4. Dans GitHub, vérifie Settings > Pages, puis Actions pour voir le workflow `Automatisation portefeuille`.
5. Lance une fois le workflow depuis Actions > Automatisation portefeuille > Run workflow pour initialiser les données.

## Automatismes
- Prix : Yahoo Finance/yfinance via GitHub Actions, jours ouvrés à 18:30 UTC.
- Actualités : Google News RSS via GitHub Actions, chaque jour à 07:15 UTC (collecte, liens sources; pas d'analyse IA).
- Les données générées sont `data/prices.json` et `data/news.json` et sont commitées dans le dépôt.
- L'estimation par ligne utilise quantité × cours lorsque le cours est disponible. Valeur Trade Republic 2 990,47 € reste une référence manuelle, aucune connexion TR.
- L'estimation calculée n'est que la somme des positions dont le symbole a un cours. Certains symboles peuvent être manquants ou incorrects; vérifier `failed` dans prices.json.
- SpaceX est non cotée et ne dispose pas d'un cours public fiable dans ce script.

## Limites et sécurité
GitHub Pages est statique. Aucun accès à Trade Republic, aucune synchronisation LocalStorage multi-appareils, aucune notification push au téléphone, ni interprétation automatique des news par IA sans service/API supplémentaire. RSS est susceptible d'être indisponible; Yahoo Finance n'est pas une API garantie. GitHub Actions peut être retardé. La veille, notes et réglages locaux restent dans LocalStorage. Export JSON depuis le site pour sauvegarder.
