# Function to confirm whether the user wants to continue
def get_user_choice():
    """
    Prompt the user to confirm whether to continue using the system.
    Returns 'y' for yes and 'n' for no.
    """
    while True:
        choice = input("Do you want to use the system again? (y/n): ").lower().strip()
        if choice in ["y", "n"]:
            return choice
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Main Banking System Code
print("Welcome to the Banking System!")

actions = [0, 1, 2, 3]
balance = 1000

while True:
    print("\n=== Banking Menu ===")
    print("1 - Deposit money")
    print("2 - Withdraw money")
    print("3 - Check balance")
    print("0 - Exit")
    print("====================")

    try:
        user_action = int(input("Enter your action (1-3) or 0: "))

        if user_action not in actions:
            print("Invalid action. Please enter a number between 0 and 3.")
            continue

        if user_action == 0:
            print("Goodbye! Thanks for using the Banking System!")
            break
        elif user_action == 3:
            print(f"Your current balance is: ${balance}")
            continue
        elif user_action == 2:
            while True:
                try:
                    amount_withdraw = int(input("Enter withdrawal amount: $"))
                    if amount_withdraw > balance:
                        print(f"Insufficient balance. Your current balance is: ${balance}.")
                        print("Please enter an amount within your available balance.")
                    elif amount_withdraw <= 0:
                        print("Please enter a positive amount.")
                    else:
                        balance -= amount_withdraw
                        print(f"${amount_withdraw} successfully withdrawn.")
                        print(f"Your updated balance is: ${balance}.")
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        elif user_action == 1:
            while True:
                try:
                    amount_deposit = int(input("Enter amount to deposit: $"))
                    if amount_deposit <= 0:
                        print("Please enter a positive amount.")
                    else:
                        balance += amount_deposit
                        print(f"${amount_deposit} successfully deposited.")
                        print(f"Your updated balance is: ${balance}.")
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
    except ValueError:
        print("Invalid input! Please enter a number.")

    # Call the reusable function for Yes/No confirmation
    choice = get_user_choice()

    if choice != "y":
        print("Goodbye! Thanks for using the Banking System!")
        break