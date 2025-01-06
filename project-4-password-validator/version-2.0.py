import string

print("Welcome to the Password Validator!")
print("Rules for a strong password:")
print("- Must be 8-16 characters long.")
print("- Must include at least one uppercase letter.")
print("- Must include at least one lowercase letter.")
print("- Must include at least one digit.")
print("- Must include at least one special character.")
print("- Must not contain spaces.\n")

while True:
    min_len = 8
    max_len = 16
    char_list = string.punctuation
    errors = []

    password = input("Enter Your Password or type (exit) to quit: ")

    if password.lower().strip() == "exit":
        print("Goodbye! Thanks for using")
        break

    if len(password) < min_len:
        print("Password must be at least 8 characters long.")
        again = input("Do you want to Try Again: (y/n)").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for using")
            break
        else:
            continue

    if len(password) > max_len:
        print("Password must not exceed 16 characters.")
        again = input("Do you want to Try Again: (y/n)").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for using")
            break
        else:
            continue

    if not any(char.isupper() for char in password):
        errors.append("Password must include at least one uppercase letter.")
        
    if not any(char.islower() for char in password):
        errors.append("Password must include at least one lowercase letter.")    

    if not any(char.isdigit() for char in password):
        errors.append("Password must include at least one digit.")    

    if not any( char in char_list for char in password):
        errors.append("Password must include at least one special character.")

    if " " in password:
        errors.append("Password must not contain space")           

    if len(errors) > 2:
        print("Password Strength:")
        print("Weak Password")
        print("\n".join(errors))
        again = input("Do you want to Try Again: (y/n)").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for using")
            break
        else:
            continue
    elif len(errors) > 0 and len(errors) <= 2:
        print("Password Strength:")
        print("Good Password")
        print("\n".join(errors))
        again = input("Do you want to Try Again: (y/n)").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for using")
            break
        else:
            continue
    else:
        print("Password Strength:")
        print("Strong Password")
        again = input("Do you want to Try Again: (y/n)").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for using")
            break
        else:
            continue