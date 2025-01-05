import random

print("Welcome to the Guess the Number game!")
print("The computer has chosen a number between 1 and 100. Can you guess it?")

computer_guess = random.randint(1, 100)
attempts = 0
correct_guess = False

while correct_guess == False:
    user_guess = int(input("Guess The Number: "))
    attempts += 1

    if user_guess > computer_guess:
        print("Too High to guess")
    elif user_guess < computer_guess:
        print("Too Low to guess")                
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        correct_guess = True

