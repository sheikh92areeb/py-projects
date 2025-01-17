# Welcome message and available operations
print("Welcome to Simple Calculator!\n")
print("Operations:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
print("0 to Exit")

# Function to perform calculations
def calculation(op, n, m):
    """
    Perform a calculation based on the operator and two numbers.
    """
    if op == "/" and n == 0:
        return "Division by zero is not allowed."
    elif op == "+":
        return m + n
    elif op == "-":
        return m - n
    elif op == "*":
        return m * n
    elif op == "/":
        return m / n
    else:
        return "Invalid operation."

# Supported operators
operators = ["0", "+", "-", "*", "/"]

# Main program loop
while True:
    user_opr = input("\nSelect Your Operation: ").strip()

    # Validate the operator
    if user_opr not in operators:
        print("Invalid operator. Please choose from +, -, *, /, or 0.") 
        continue
    elif user_opr == "0":
        print("Goodbye! Thanks for using the Simple Calculator!")
        break
    else:
        try:
            # Get input numbers from the user
            m = float(input("Enter the First Number: ").strip())
            n = float(input("Enter the Second Number: ").strip())

            # Perform the calculation
            result = calculation(user_opr, n, m)

            # Handle the case where the result is an error message
            if isinstance(result, str):
                print(result)
            else:
                # Format result to display as an integer if it's a whole number
                if result.is_integer():
                    print(f"Result: {int(result)}")  # Display as an integer
                else:
                    print(f"Result: {result}")  # Display as a float for decimal numbers

            # Prompt to use the calculator again
            while True:
                choice = input("Do you want to use again? (y/n): ").lower().strip()
                if choice in ["y", "n"]:
                    break
                else:
                    print("Invalid input! Please enter 'y' for yes or 'n' for no.")

            if choice != "y":
                print("Goodbye! Thanks for using the Simple Calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue