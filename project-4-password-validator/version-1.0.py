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

    user_password = input("Enter Your Password: ")

    if len(user_password) < min_len:
        print("Password must be at least 8 characters long.")
        break

    if len(user_password) > max_len:
        print("Password must not exceed 16 characters.")
        break

    if not any( char.isupper() for char in user_password):
        print("Password must include at least one uppercase letter.")
        break

    if not any( char.islower() for char in user_password):
        print("Password must include at least one lowercase letter.")
        break

    if not any( char.isdigit() for char in user_password):
        print("Password must include at least one digit.")
        break

    if not any( char in char_list for char in user_password):
        print("Password must include at least one special character.")
        break

    if " " in user_password:
        print("Password must not contain spaces.")
        break

    print("Password is Strong")
    break