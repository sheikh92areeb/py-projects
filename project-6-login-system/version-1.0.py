print("Welcome to the Simple Login System!")

user_name = "areeb"
password = "12345"

user_name_input = input("Enter your username: ").lower().strip()

if user_name == user_name_input:
    password_input = input("Enter your password:").strip()
    if password == password_input:
        print(f"Welcome! {user_name}")
    else:
         print("Incorrect Password")   
else:
    print("User does not exist")