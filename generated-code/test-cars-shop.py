Kia = {"Sonet X": 53190,
       "Sonet GTX": 52485,
       "Sonet HTX": 48465,
       "Sonet HTK": 40614}

Audi = {"A1": 113000,
        "A3": 161000,
        "A4": 198000,
        "A5": 230000,
        "Q2": 166000,
        "Q3": 212000}

Fiat = {"Panda": 53000,
        "500": 67500,
        "Fiorino": 48500,
        "Ducato": 90400}

Jeep = {"Renegade": 126500,
        "Compass": 16800,   # Correction de la valeur de Compass
        "Wrangler": 327000}

Peugeot = {"208": 68500,
           "2008": 97900,
           "308": 108900,
           "3008": 146900}

Volkswagen = {"Amarok": 199980,
              "Tiguan": 156980,
              "Polo": 82980,
              "Golf 8": 120980}

def welcome():
    print("Welcome! These are the available Cars... What are you looking for?")
    print("1. Kia")
    print("2. Audi")
    print("3. Fiat")
    print("4. Jeep")
    print("5. Peugeot")
    print("6. Volkswagen")

def main():
    wallet = 200000  # Initialize wallet
    welcome()
    rep = input("Enter your choice: ")
    model = ""

    # Mapping user input to model
    if rep == "1":
        model = "Kia"
    elif rep == "2":
        model = "Audi"
    elif rep == "3":
        model = "Fiat"
    elif rep == "4":
        model = "Jeep"
    elif rep == "5":
        model = "Peugeot"
    elif rep == "6":
        model = "Volkswagen"
    else:
        print("Invalid choice!")
        return

    print("Great choice! Here are the available models of", model)

    # Selling logic based on the selected model
    if model == "Kia":
        print(Kia)
        print("What do you want to buy?")
        rep = input()
        if rep in Kia:
            if wallet < Kia[rep]:
                print("Sorry, we can't sell it for you below the shown price")
            else:
                wallet -= Kia[rep]
                print("Congratulations!")
        else:
            print("Invalid model!")
    elif model == "Audi":
        print(Audi)
        # Ajouter la logique pour Audi
    elif model == "Fiat":
        print(Fiat)
        # Ajouter la logique pour Fiat
    elif model == "Jeep":
        print(Jeep)
        # Ajouter la logique pour Jeep
    elif model == "Peugeot":
        print(Peugeot)
        # Ajouter la logique pour Peugeot
    elif model == "Volkswagen":
        print(Volkswagen)
        # Ajouter la logique pour Volkswagen
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()