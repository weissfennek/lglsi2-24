import random

def jeu_devinette():
    nombre_a_deviner = random.randint(1, 100)  # Génère un nombre aléatoire entre 1 et 100
    nombre_dessaies = 0
    devine = False

    print("Bienvenue dans le jeu de devinette de nombre!")
    print("Je pense à un nombre entre 1 et 100. Devine quel est ce nombre!")

    while not devine:
        essai = int(input("Entrez votre devinette : "))

        nombre_dessaies += 1

        if essai < nombre_a_deviner:
            print("Le nombre que je pense est plus grand!")
        elif essai > nombre_a_deviner:
            print("Le nombre que je pense est plus petit!")
        else:
            devine = True
            print("Félicitations! Vous avez deviné le nombre en {} essais!".format(nombre_dessaies))

    rejouer = input("Voulez-vous jouer à nouveau? (Oui/Non) : ")
    if rejouer.lower() == "oui":
        jeu_devinette()
    else:
        print("Merci d'avoir joué!")
