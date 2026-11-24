# Portfolio 3.0 — refonte

## Installation GitHub Pages
1. Sauvegardez l'ancien dépôt.
2. Remplacez le contenu du dépôt `portefeuille3.0` par le contenu de ce dossier (y compris `.github`).
3. Commit/push. Dans GitHub : Settings > Pages, branche `main` / dossier `/root` (selon configuration).

## Valeur de référence
La valeur totale de référence initiale est réglée à **2 990,47 €**, d'après le montant donné par l'utilisateur. Ce total n'est pas synchronisé à Trade Republic; il est distinct du total de montants investis des positions (3 373,19 € dans le fichier d'origine, soit une différence de -382,72 € avec la référence). Le site l'affiche explicitement.

## Cours
Le workflow GitHub Actions et `fetch.py` restent en place. Les cours sont susceptibles de manquer pour certains actifs/tickers et ne sont pas une connexion Trade Republic. Vérifiez les correspondances symboles et la conversion EUR avant d'utiliser les chiffres.

## Données locales
Veille, notes et actualités ajoutées manuellement sont sauvegardées dans le LocalStorage de ce navigateur. Export JSON régulier recommandé. L'export JSON conserve une copie de portfolio et de cours. Pas de synchronisation entre appareils.
