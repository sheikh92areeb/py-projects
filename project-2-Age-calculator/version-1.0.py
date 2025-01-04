from datetime import datetime

# Get the current year
current_year = datetime.now().year

print("Welcome to the Age Calculator!")
print("Calculate your age by entering your birth year.")

birth_year = int(input("Enter your birth year: ")) 

if birth_year > current_year:
    print("Future year! You are not born yet.")
elif birth_year == current_year:
    print("Same year! You are a newborn.")   
else:
    age = current_year - birth_year
    print(f"You are {age} years old.") 
