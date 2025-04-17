# visualisations-de-s-ries-chronologiques
visualisations de séries chronologiques en utilisant Pandas, Matplotlib et Seaborn.
# Analyse des Données du Forum FreeCodeCamp

Ce projet vise à analyser les données de visites sur le forum FreeCodeCamp. Le fichier de données contient le nombre de pages vues chaque jour sur le forum entre le **9 mai 2016** et le **3 décembre 2019**. Nous allons explorer ces données à l'aide de visualisations pour comprendre les tendances de trafic, la croissance annuelle, mensuelle et les schémas saisonniers.

## Structure du Projet

Ce projet est structuré autour des étapes suivantes :

1. **Chargement et nettoyage des données** : Importation du fichier CSV et nettoyage des anomalies (valeurs extrêmes et données aberrantes).
2. **Visualisation des données** : Création de trois types de graphiques pour analyser les données :
    - Un **graphique linéaire** pour visualiser l'évolution quotidienne des pages vues.
    - Un **graphique à barres** pour montrer les moyennes mensuelles des pages vues.
    - Un **graphique en boîte** pour observer la distribution des pages vues sur une base annuelle et mensuelle.

## Prérequis

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Installation des Dépendances

Pour installer les dépendances nécessaires, utilise la commande suivante :

```bash
pip install pandas matplotlib seaborn
