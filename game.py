import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try guessing higher.")
        elif guess > target_number:
            print("Too high! Try guessing lower.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            break
def main():
    play_again = True
    
    while play_again:
        guess_number()
        play_again = input("Do you want to play again? (yes/no): ").lower().startswith('y')

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
