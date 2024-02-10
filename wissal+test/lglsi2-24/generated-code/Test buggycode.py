wallet = 100000  # Initialize wallet with a specific amount

def welcome():
    print("Welcome! These are the available Cars... What are you looking for?")
    print("1. Kia")
    print("2. Audi")
    print("3. Fiat")
    print("4. Jeep")
    print("5. Peugeot")
    print("6. Volkswagen")

welcome()
rep = input()
model = ""

match rep:
    case "1":
        model = "Kia"
    case "2":
        model = "Audi"
    case "3":
        model = "Fiat"
    case "4":
        model = "Jeep"
    case "5":
        model = "Peugeot"
    case "6":
        model = "Volkswagen"

print("Great choice! Here are the available models of", model)

match model:
    case "Kia":
        print(Kia)
        print("What do you want to buy?")
        rep = input()
        match rep:
            case "Sonet X":
                if wallet < Kia["Sonet X"]:
                    print("Sorry, we can't sell it for you below the shown price")
                else:
                    wallet -= Kia["Sonet X"]
                    print("Congratulations! Purchase successful. Remaining amount in wallet:", wallet)
            case "Sonet HTX":
                # (Repeat the same structure for other models)
    case "Audi":
        # (Repeat the same structure for other brands)
    case "Fiat":
        # (Repeat the same structure for other brands)
    case "Jeep":
        # (Repeat the same structure for other brands)
    case "Peugeot":
        # (Repeat the same structure for other brands)
    case "Volkswagen":
        # (Repeat the same structure for other brands)
