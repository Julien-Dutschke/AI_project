# Explication Simplifiée des Concepts Mathématiques

Ce document explique de manière simplifiée les concepts mathématiques utilisés dans le projet ft_linear_regression.

## Normalisation des Données

### Pourquoi Normaliser ?

La normalisation des données permet de mettre toutes les valeurs sur la même échelle, généralement entre 0 et 1. Cela aide les algorithmes à converger plus rapidement lors de l'entraînement du modèle.

TRES TRES RECOMMANDER EN MACHINE LEARNING

### Comment Normaliser ?

![Normalisation des Données](https://www.aquaportail.com/pictures2301/normalisation-formule.jpg)

### En savoir plus :
- [Introduction à la normalisation des données](https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/)

## Descente de Gradient

### Qu'est-ce que c'est ?

La descente de gradient est une méthode pour trouver les coefficients d'un modèle qui minimise l'erreur entre les prédictions et les valeurs réelles.

### Comment ça fonctionne ?

1. **Initialisation** : Démarrez avec des valeurs initiales pour les coefficients.
2. **Calcul de l'Erreur** : Mesurez la différence entre les prédictions du modèle et les valeurs réelles.
3. **Mise à Jour des Coefficients** : Ajustez les coefficients pour réduire l'erreur en utilisant des itérations répétées et une valeur de taux d'apprentissage alpha.

### En savoir plus :
- [Gradient Descent Explained Simply](https://towardsdatascience.com/gradient-descent-explained-simply-29b8dd9b4f75)

## Fonction de Coût

### Quelle est sa fonction ?

La fonction de coût mesure l'erreur entre les prédictions du modèle et les valeurs réelles. En minimisant cette fonction, on améliore la précision du modèle.

### Formule de la Fonction de Coût :

Pour la régression linéaire :
![Fonction de Coût](https://i.ytimg.com/vi/Hf2GEfAGnN4/maxresdefault.jpg)

### En savoir plus :
- [Understanding Cost Function in Machine Learning](https://www.geeksforgeeks.org/understanding-cost-function-machine-learning/)

## Symboles Mathématiques de Base

-  x  : variable indépendante (par exemple, kilométrage)
-  y : variable dépendante (par exemple, prix)
-  theta_0 : intercept (valeur de y quand x est egale a 0)
-  theta_1 : pente (montre comment y change avec x)
-  alpha : taux d'apprentissage (contrôle la taille des mises à jour des 	coefficients) ici 0.1
-  Σ (sigma) : symbole de somme (additionne une série de valeurs)

Ces ressources devraient fournir une base pour comprendre les concepts mathématiques utilisés dans le projet de régression linéaire. 