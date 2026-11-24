# Portfolio 3.0 — version initiale

## Installation GitHub Pages
1. Téléversez le contenu de ce dossier à la racine de votre dépôt GitHub (remplacez les fichiers existants après sauvegarde).
2. Dans Settings > Pages, choisissez Deploy from branch, `main`, dossier `/ (root)`.
3. Dans Actions > General, autorisez les permissions de lecture/écriture si vous utilisez le workflow de cours.
4. Actions > Mise à jour des cours > Run workflow pour lancer une première mise à jour.

## Données et sauvegardes
- Les données de départ viennent de `data/portfolio.json`.
- Les changements saisis dans le site sont stockés dans LocalStorage du navigateur.
- Utilisez régulièrement « Sauvegarder JSON » et conservez ce fichier ailleurs.
- LocalStorage ne synchronise pas entre appareils.
- Les cours manuels peuvent être renseignés par ticker.
- La mise à jour Yahoo Finance est un indicateur et peut échouer, manquer des actifs ou fournir des données incorrectes. Vérifiez les cours.
- Les anciens articles ont été retirés de la présentation comme actualités courantes car ils n'ont pas été vérifiés.

## Limites de cette première version
- L'import automatique du CSV Trade Republic est temporairement non réactivé : le format exact doit être validé avec un export récent.
- Aucune API d'actualité n'est intégrée.
- Castor Vinci est un espace de suivi et de notes, sans règles officielles intégrées.
- Ce site statique ne contient ni authentification ni synchronisation serveur. Ne publiez pas de données sensibles dans un dépôt public.
