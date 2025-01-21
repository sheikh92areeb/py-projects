import random

def mad_twist(result):
    # Random operator selection
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    # Random number selection
    number = random.randint(1, 10)
    
    # Perform the twist calculation
    if operator == "+":
        final_result = result + number
    elif operator == "-":
        final_result = result - number
    elif operator == "*":
        final_result = result * number
    elif operator == "/":
        final_result = result / number
    
    return operator, number, final_result

def mad_calculator():
    print("Welcome to the Mad Calculator!")
    print("Perform your calculation, but beware... the result will have a twist!\n")

    while True:
        try:
            # Get user inputs for calculation
            num1 = float(input("Enter the first number: "))
            op = input("Enter an operator (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))

            # Validate the operator
            if op not in ["+", "-", "*", "/"]:
                print("Invalid operator! Please use one of +, -, *, /.\n")
                continue

            # Perform the user's calculation
            if op == "+":
                user_result = num1 + num2
            elif op == "-":
                user_result = num1 - num2
            elif op == "*":
                user_result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Division by zero is not allowed!\n")
                    continue
                user_result = num1 / num2
            
            print(f"Your result: {user_result:.2f}")
            
            # Apply the mad twist
            operator, number, twisted_result = mad_twist(user_result)

            print("\nTwist Applied!")
            print(f"The computer added a random operation: {operator} {number}")
            print(f"The final result is: {twisted_result:.2f}\n")

            # Ask to play again
            play_again = input("Do you want to try again? (y/n): ").lower().strip()
            if play_again != "y":
                print("Thanks for playing the Mad Calculator! Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

mad_calculator()
