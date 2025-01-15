print("Welcome! to Prime Number Checker")

while True:
    user = input("Enter a number or type 'exit' to quit: ").strip().lower()
    count = 0

    if user == 'exit':
        print("Goodbye! Thanks For Using")
        break

    if int(user) < 1:
        print("Please! Enter positive Number")
        continue
    elif int(user) > 1:
        for i in range(2,int(user)):
            if int(user) % i == 0:
                count += 1

        if count > 0:
            print(f"{user} is not Prime Number")
        else:
            print(f"{user} is Prime Number")            
    else:
        print("1 is not a prime number because it has only one factor.")

    choice = input("Do you want to use again? (y/n)").strip().lower()    
    if choice != "y":
        print("Goodbye! Thanks For Using")
        break