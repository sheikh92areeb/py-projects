print("Welcome! to Banking System")
print("\nPerforming Actions:")
print("1- Deposit money")
print("2- Withdraw money")
print("3- Check balance")
print("0- Exit")

actions = [0,1,2,3]
balance = 1000

while True:
    user = int(input("Enter your Action (1-3) or 0: "))


    if user not in actions:
        print("Invalid Action, Please Enter between 1-3 or 0")
        continue
    else:
        if user == 0:
            print("Goodbye! Thanks for using the Banking System!")
            break
        elif user == 3:
            print(f"Your Current Balance is: ${balance}")
        elif user == 2:
            while True:
                try:
                    amount_withdraw = int(input("Enter Withdrawal Amount: $"))

                    if amount_withdraw > balance:
                        print("Insufficient balance,")
                        print(f"Your Current Balance is: ${balance}")
                        print("Please! Enter Amount Under your balance")
                        continue
                    else:
                        print(f"${amount_withdraw} is Successfully Withdraw")
                        balance = balance - amount_withdraw
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue
        elif user == 1:
            while True:
                try:
                    amount_deposit = int(input("Enter Amount to Deposit: $"))

                    if 0 > amount_deposit:
                        print("Please! Enter a Positive Amount")
                        continue
                    else:
                        print(f"You successfully deposited ${amount_deposit}")
                        balance = balance + amount_deposit
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue   
                
    while True:
        choice = input("Do you want to use again? (y/n): ").lower().strip()
        if choice in ["y", "n"]:
            break
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")

    if choice != "y":
        print("Goodbye! Thanks for using the Simple Calculator!")
        break