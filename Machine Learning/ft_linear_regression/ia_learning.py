import csv
import matplotlib.pyplot as plt

price,kilométrage



# Prédiction pour un kilométrage donné avec les coefficients convertis
def predict_price(distance, a, b):
    return a * distance + b

# Normalisation des données
def normalize_list(lst):
    min_val = min(lst)
    max_val = max(lst)
    normalized_lst = [(x - min_val) / (max_val - min_val) for x in lst]
    return normalized_lst, min_val, max_val



# Fonction qui retourne f(x) = a*x + b
def prediction_function(x: float, a: float , b: float) -> float:
    return a * x + b



# Fonction de coût
def CostFunction(theta0: float, theta1: float, mileage: list, price: list) -> float:
    totalError = 0
    m = len(mileage)  # Nombre d'échantillons

    for i in range(m):
        prediction = theta1 * mileage[i] + theta0
        error = prediction - price[i]
        totalError += error * error

    return totalError / (2 * m)




# Fonction de descente de gradient
def gradientDescent(theta0: float, theta1: float, learningRate: float, iterations: int, mileage: list, price: list):
    m = len(mileage)

    print(f"Initial Cost: {CostFunction(theta0, theta1, mileage, price):.4f}")
    print(f"Theta0 before update: {theta0:.10f}")
    print(f"Theta1 before update: {theta1:.10f}")

    for iter in range(iterations):
        sumErrorTheta1 = 0
        sumErrorTheta0 = 0

        for i in range(m):
            prediction = theta1 * mileage[i] + theta0
            error = prediction - price[i]
            sumErrorTheta1 += error * mileage[i]
            sumErrorTheta0 += error

        theta1 -= (learningRate / m) * sumErrorTheta1
        theta0 -= (learningRate / m) * sumErrorTheta0

    # Affichage des paramètres mis à jour après toutes les itérations
    print(f"Final Cost: {CostFunction(theta0, theta1, mileage, price):.4f}")
    print(f"Theta0 after update: {theta0:.10f}")
    print(f"Theta1 after update: {theta1:.10f}")
    print("\n\n")
    return theta0, theta1  # Retourner les nouvelles valeurs de theta0 et theta1



if __name__ == '__main__':
    # Définition des noms de fichier et des listes
    filename = 'data.csv'
    mileage = []
    price = []

    # Lecture du fichier CSV
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pour sauter l'en-tête s'il y en a un
        for row in reader:
            if len(row) == 2:  # S'assure qu'il y a exactement deux colonnes par ligne
                try:
                    # Conversion des valeurs en float et ajout aux listes correspondantes
                    mileage.append(float(row[0].strip()))
                    price.append(float(row[1].strip()))
                except ValueError as e:
                    print(f"Erreur de conversion: {e}")
                    continue
            else:
                print(f"Ignorer la ligne mal formatée: {row}")
    # Affichage des listes remplies
    print("Mileage:", mileage)
    print("Price:", price)
    print("\n\n")


    # Normalisation des listes de kilométrage et de prix a l'aide de la formule mathematique suivante : 
    # x = (x - min) / (max - min)
    normalized_mileage, min_mileage, max_mileage = normalize_list(mileage)
    normalized_price, min_price, max_price = normalize_list(price)

    # Les valeurs initiales de theta0, theta1, learningRate et iterations
    theta0 = 0
    theta1 = 0
    learningRate = 0.1
    iterations = 1000


    # Utilisation de la descente de gradient sur les données normalisées
    # je recupere les valeurs de theta0 et theta1
    theta0_normalized, theta1_normalized = gradientDescent(theta0, theta1, learningRate, iterations, normalized_mileage, normalized_price)



    # Conversion des coefficients normalisés vers non normalisés
    theta1 = theta1_normalized * (max_price - min_price) / (max_mileage - min_mileage)
    theta0 = theta0_normalized * (max_price - min_price) + min_price - theta1 * min_mileage

    print("Converted Coefficients (non-normalized):")
    print("a (pente):", theta1)
    print("b (intercept):", theta0)

    # Affichage des données et de la droite de régression
    plt.scatter(mileage, price, color='blue', label='Data', marker='+',s=100)

    predict_price_List = [predict_price(x, theta1, theta0) for x in mileage]

    # print data with + symbol
    plt.plot(mileage, predict_price_List, color='red', label='Regression Line', linewidth=3, linestyle='-')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Linear Regression')
    plt.legend()
    plt.show()





    # Exemple de prédiction
    distance_example = 74001
    predicted_price = predict_price(distance_example, theta1, theta0)
    print(f"Price predicted for mileage {distance_example}: {predicted_price:.2f}")

    # create and print thetha0 and thetha1 in file for an other program
    with open('thetas.txt', 'w') as file:
        file.write(f"{theta0}\n{theta1}")