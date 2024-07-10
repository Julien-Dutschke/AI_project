# ft_linear_regression || Machine Learning project

Ce projet implémente une régression linéaire simple pour prédire le prix d'une voiture en fonction de son kilométrage. Il est divisé en deux parties : l'entraînement du modèle (`ia_learning.py`) et l'utilisation du modèle entraîné pour faire des prédictions (`prediction.py`).

## Table des matières

- [Mathématiques Simplifiées](MATH_README.md)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Détails du Code](#détails-du-code)
- [ia_learning.py](#ia_learningpy)
- [prediction.py](#predictionpy)
- [Sources](#sources)
- [Auteur](#auteur)

## Mathématiques Simplifiées

Consultez le document [Mathématiques Simplifiées](MATH_README.md) pour une explication détaillée des concepts mathématiques utilisés dans ce projet.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votreutilisateur/ft_linear_regression.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd ft_linear_regression
    ```
3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Entraînement du Modèle

Pour entraîner le modèle et obtenir les coefficients `theta0` et `theta1` :
```bash
python ia_learning.py
```
Ce script lit les données à partir d'un fichier data.csv, entraîne le modèle de régression linéaire, et enregistre les coefficients dans un fichier thetas.txt.


### Prédiction avec le Modèle

Pour utiliser le modèle entraîné et prédire le prix d'une voiture en fonction de son kilométrage :
```bash
python prediction.py
```
Ce script lit les coefficients depuis thetas.txt, demande à l'utilisateur de saisir un kilométrage, et retourne le prix estimé.


## Détails du Code

### ia_learning.py

Ce script est responsable de l'entraînement du modèle de régression linéaire.

- **Lecture des Données** : Lit le fichier CSV `data.csv` contenant les données de kilométrage et de prix.
- **Normalisation des Données** : Normalise les données pour améliorer l'efficacité de la descente de gradient. (Pour éviter les erreurs de type NAN, etc.)
- **Descente de Gradient** : Utilise l'algorithme de descente de gradient pour trouver les coefficients `theta0` et `theta1` minimisant la fonction de coût (plus la fonction de coût diminue, plus le résultat sera intéressant).
- **Affichage et Sauvega## Mathématiques Simplifiées

Consultez le document [Mathématiques Simplifiées](MATH_README.md) pour une explication détaillée des concepts mathématiques utilisés dans ce projet.
Ce script utilise les coefficients entraînés pour faire des prédictions.

- **Lecture des Coefficients** : Lit les coefficients `theta0` et `theta1` depuis `thetas.txt`.
- **Prédiction** : Utilise ces coefficients pour prédire le prix d'une voiture en fonction du kilométrage fourni par l'utilisateur.

## Sources

- [Machine Learnia - Chaîne YouTube](https://www.youtube.com/channel/UCkccyEb2IY5Xno8z-2iHoSw)
- [LA RÉGRESSION LINÉAIRE (partie 1/2) - ML#3](https://www.youtube.com/watch?v=wg7-roETbbM)
- [DESCENTE DE GRADIENT (GRADIENT DESCENT) - ML#4](https://www.youtube.com/watch?v=rcl_YRyoLIY&list=PLO_fdPEVlfKqUF5BPKjGSh7aV9aBshrpY&index=4)


## Auteur

Projet réalisé par [Julien Dutschke](https://github.com/Julien-Dutschke)🍻🪓