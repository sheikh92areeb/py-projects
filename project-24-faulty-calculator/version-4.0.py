import random
import operator

# Mapping correct and faulty operations
faultyOps = { "+": operator.sub, "-": operator.truediv, "*": operator.add, "/": operator.pow }
correctOps = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

while True:
    try:
        # Generating a random number for faulty behavior
        random_time = random.randint(1,100)

        # Taking user input
        m = float(input("Enter First Number: "))
        n = float(input("Enter Second Number: "))
        o = input("Choose Operation (+, -, *, /): ").strip()

        # Checking for valid operation
        if o not in correctOps:
            print("❌ Invalid operation! Please enter one of +, -, *, /.")
            continue

        # Handling faulty operations 10% of the time
        operation = faultyOps[o] if random_time <= 10 else correctOps[o]

        # Handling division by zero safely
        if o == "/" and n == 0:
            print("❌ Error: Division by zero is not allowed.")
            continue

        # Performing calculation
        result = operation(m, n)
        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Invalid input! Please enter numerical values.")

    # Asking user if they want to continue
    while True:
        choice = input("🔄 Do you want to use it again? (y/n): ").strip().lower()
        if choice in ["y", "n"]:
            break
        else:
            print("❌ Please enter 'y' for yes or 'n' for no.")

    if choice != "y":
        print("👋 Goodbye! Thanks for using the Faulty Calculator.")
        break
