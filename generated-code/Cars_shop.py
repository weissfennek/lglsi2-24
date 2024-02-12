
Kia ={"Sonet X":53190,
      "Sonet GTX":52485,
      "Sonet HTX":48465,
      "Sonet HTK":40614
      }
Audi ={"A1":113000,
       "A3":161000,
       "A4":198000,
       "A5":230000,
       "Q2":166000,
        "Q3":212000,}

Fiat ={"Panda":53000,
       "500":67500,
       "Fiorino":48500,
       "Ducato":90400}
Jeep ={"Renegade":126500,
       "Compass":16800,
       "Wrangler":327000}
Peugeot ={"208":68500,
          "2008":97900,
          "308":108900,
          "3008":146900}
Volkswagen ={"Amarok":199980,
             "Tiguan":156980,
             "Polo":82980,
             "Golf 8":120980}
def welcome():
    print("Welcome ! These are the available Cars ... What are you looking for ?")
    print("1.Kia")
    print("2.Audi")
    print("3.Fiat")
    print("4.Jeep")
    print("5.Peugeot")
    print("6.Volkswagen")


welcome()   
rep=input()
model=""
  
match rep:
    case "1":
        model="Kia"
        
    case "2" :
        model="Audi"
    case "3":
        model="Fiat"
    case "4" :
        model="Jeep"
    case "5":
        model="Peugeot"
    case "6" :
        model="Volkswagen"
print("Great choice !... here is the available models of ", model)  


match model :
    case "Kia" :
        print(Kia)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "Sonet X":
                 if(wallet < Kia["Sonet X"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Kia["Sonet X"]
                     print("Congratulations !")
            case "Sonet HTX":
                 if(wallet < Kia["Sonet HTX"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Kia["Sonet HTX"]
                     print("Congratulations !")
            case "Sonet GTX":
                 if(wallet < Kia["Sonet GTX"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Kia["Sonet GTX"]
                     print("Congratulations !")
            case "Sonet HTK":
                 if(wallet < Kia["Sonet HTK"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Kia["Sonet HTK"]
                     print("Congratulations !")
    case "Audi" :
        print(Audi)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "A1":
                 if(wallet < Audi["A1"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["A1"]
                     print("Congratulations !")
            case "A3":
                 if(wallet < Audi["A3"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["A3"]
                     print("Congratulations !")
            case "A4":
                 if(wallet < Audi["A4"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["A4"]
                     print("Congratulations !")
            case "A5":
                 if(wallet < Audi["A5"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["A5"]
                     print("Congratulations !")
            case "Q2":
                 if(wallet < Audi["Q2"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["Q2"]
                     print("Congratulations !")
            case "Q3":
                 if(wallet < Audi["Q3"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Audi["Q3"]
                     print("Congratulations !")
    case "Fiat" :
        print(Fiat)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "Panda":
                 if(wallet < Fiat["Panda"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Fiat["Panda"]
                     print("Congratulations !")
            case "500":
                 if(wallet < Fiat["500"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Fiat["500"]
                     print("Congratulations !")
            case "Fiorino":
                 if(wallet < Fiat["Fiorino"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Fiat["Fiorino"]
                     print("Congratulations !")
            case "Ducato":
                 if(wallet < Fiat["Ducato"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Fiat["Ducato"]
                     print("Congratulations !")        
    case "Jeep" :
        print(Jeep)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "Renegade":
                 if(wallet < Jeep["Renegade"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Jeep["Renegade"]
                     print("Congratulations !")
            case "Compass":
                 if(wallet < Jeep["Compass"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Jeep["Compass"]
                     print("Congratulations !")
            case "Wrangler":
                 if(wallet < Jeep["Wrangler"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Jeep["Wrangler"]
                     print("Congratulations !")
    case "Peugeot" :
        print(Peugeot)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "208":
                 if(wallet < Peugeot["208"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Peugeot["208"]
                     print("Congratulations !")
            case "2008":
                 if(wallet < Peugeot["2008"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Peugeot["2008"]
                     print("Congratulations !")
            case "308":
                 if(wallet < Peugeot["308"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Peugeot["308"]
                     print("Congratulations !")
            case "3008":
                 if(wallet < Peugeot["3008"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Peugeot["3008"]
                     print("Congratulations !")
    case "Volkswagen" :
        print(Volkswagen)
        print("what do you want to buy ?")
        rep=input()
        match rep :
            case "Amarok":
                 if(wallet < Volkswagen["Amarok"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Volkswagen["Amarok"]
                     print("Congratulations !")
            case "Tiguan":
                 if(wallet < Volkswagen["Tiguan"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Volkswagen["Tiguan"]
                     print("Congratulations !")
            case "Polo":
                 if(wallet < Volkswagen["Polo"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Volkswagen["Polo"]
                     print("Congratulations !")
            case "Golf 8":
                 if(wallet < Volkswagen["Golf 8"]):
                     print("Sorry we can't sell it for you below the shown price")
                 else :
                     wallet=wallet-Volkswagen["Golf 8"]
                     print("Congratulations !")
