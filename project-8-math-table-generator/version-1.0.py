print("Welcome! to Math Table Generator")
print("Enter Number and Generate Tabel")

while True:
    user_input = int(input("Enter Your Number: "))
    range_input = int(input("Enter Table Range: "))

    for i in range(1, (range_input + 1)):
        print(f"{user_input} x {i} = {i * user_input}")

    choice = input("Do you want to Generate again? (y/n): ").lower().strip()
    if choice != "y":
        print("Goodbye! Thanks for using the program")    
        break