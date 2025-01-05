import random

print("Welcome to the Guess the Number game!")

while True:
    computer_guess = random.randint(1, 100)
    attempts = 0
    correct_guess = False

    print("The computer has chosen a number between 1 and 100. Can you guess it?")

    while not correct_guess:
        user_guess = int(input("Guess The Number: "))
        attempts += 1

        if user_guess > computer_guess:
            print("Too High to Guess")
        elif user_guess < computer_guess:
            print("Too Low to Guess")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")        
            correct_guess = True

    choice = input("Do you want to play again? (y/n): ").lower().strip()
    if choice != "y":
        print("Thanks for playing! Goodbye!")
        break