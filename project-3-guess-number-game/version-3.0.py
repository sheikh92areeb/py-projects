import random

print("Welcome to the Guess the Number game!")

while True:
    print("Choose your Difficulty Level")
    print("1. Easy (1 - 25)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    difficulty = input("Enter your choice: ").lower().strip()

    match difficulty:
        case "easy":
            max_range = 25
            attempts = 5
        case "medium":
            max_range = 50
            attempts = 7
        case "hard":
            max_range = 100
            attempts = 10
        case _:
            print("Invalid choice.")
            continue

    computer_choice = random.randint(1, max_range)
    user_attempt = 1

    print(f"You selected: {difficulty.capitalize()} mode.")
    print(f"Great! You have {attempts} attempts to guess a number between 1 and {max_range}.")

    while attempts > 0:
        print(f"Attempts: {attempts}")
        guess = int(input(f"Attempt {user_attempt}: Enter your Guess: "))

        if guess < 1 or guess > max_range:
            print(f"Please enter a number between 1 and {max_range}.")
            continue

        if guess > computer_choice:
            print("Too High! Try again")
            attempts -= 1
            user_attempt +=1
        elif guess < computer_choice:
            print("Too Low! Try again")
            attempts -= 1
            user_attempt +=1
        else:
            print(f"Correct! 🎉 You guessed the number in {user_attempt} attempts!")
            break
    else:
        print(f"Out of attempts! The correct number was {computer_choice}. Better luck next time!")        

    choice = input("Do you want to play again? (y/n): ").lower().strip()
    if choice != "y":
        print("Thanks for playing! Goodbye!")
        break