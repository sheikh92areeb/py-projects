print("Welcome to the Simple Login System!")

stored_name = "areeb"
stored_password = "12345"
attemps = 3

while True:
    if attemps < 3:
        print(f"Attemps left: {attemps}")
        
    user_input = input("Enter Your Username (or type 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        print("Goodbye! Thanks for using the system.")
        break

    if user_input == stored_name:
        password_input = input("Enter Your Password: ").strip()

        if password_input == stored_password:
            print(f"Welcome! {stored_name.capitalize()}")
            break
        else:
            print("Incorrect Password")    
            attemps -= 1
    else:
        print("User does not Exist")        
        attemps -= 1

    if attemps == 0:
        print("Too many failed attempts. Try again later.")
        break    