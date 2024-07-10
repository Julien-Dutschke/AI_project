# prediction.py

from ia_learning import predict_price

if __name__ == "__main__":
	theta0 = 0
	theta1 = 0

	# Lecture des valeurs de theta0 et theta1 depuis le fichier thetas.txt
	with open('thetas.txt', 'r') as file:
		lines = file.readlines()
		if len(lines) == 2:
			try:
				theta0 = float(lines[0])
				theta1 = float(lines[1])
			except ValueError:
				print("Erreur de conversion")

	# Lecture d'une entrée depuis le terminal
	try:
		distance = float(input("Entrez un kilométrage: "))
	except ValueError:
		print("Erreur de conversion")
		exit(1)

	# Utilisation de la fonction predict_price pour prédire le prix
	predicted_price = predict_price(distance, theta1, theta0)
	print(f"Le prix estimé pour un véhicule de {distance} km est de {predicted_price} €")
