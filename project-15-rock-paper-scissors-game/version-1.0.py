import random

print("Welcome to Rock, Paper, Scissors!")
print("Rules to Play:")
print("Rock beats Scissors")
print("Scissors beats Paper.")
print("Paper beats Rock.")
print("Let's Play!\n")

choices = { 1:'rock', 2:'paper', 3:'scissors'}
user_score = 0
computer_score = 0

while True:
    try:
        total_rounds = int(input("\nHow many rounds would you like to play? "))
        if total_rounds > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter Valid number.")

for round_num in range(1, total_rounds + 1):
    print(f"\nRound {round_num} of {total_rounds}")
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")

    while True:
        try:
            user_choice = int(input("Type (1 for rock),(2 for paper), (3 for scissors): "))
            if user_choice not in list(choices.keys()):
                print("Invalid choice. Please Enter Choice between 1-3")
                continue
            else:
                break
        except ValueError:
            print("Invalid Input, Please Enter Choice between 1-3")    
            continue

    computer_choice = random.choice(list(choices.keys()))
    print(f"You chose: {choices[user_choice]}")
    print(f"The computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a Tie")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win this round")
        user_score += 1
    else:
        print("Computer wins this round")    
        computer_score += 1

print("\nGame Over!")
print(f"Final Score: You - {user_score} | Computer - {computer_score}")

if user_score > computer_score:
    print("🎉 Congratulations! You won the game! 🎉")
elif user_score < computer_score:
    print("The computer wins the game! Better luck next time!")
else:
    print("It's a tie! Great match!")

print("Thanks for playing!")    
