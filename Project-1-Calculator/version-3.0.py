print("Welcome! to Simple Calculator \n")
print("Operations")
print("+ for Addition")
print("- forSubtraction")
print("* for Multiplication")
print("/ for Division")
print("0 for Exit")

operators = ["0","+","-","*","/"]

while True:
    user_opr = input("Select Your Operation: ")

    if user_opr not in operators:
        print("Invalid operator.") 
        continue
    elif user_opr == "0":
        print("Goodbye! Thanks For Using")       
        break
    else:
        try:
            m = int(input("Enter First Number: "))
            n = int(input("Enter Second Number: "))

            if user_opr == "+":
                result = m + n
            elif user_opr == "-":
                result = m - n
            elif user_opr == "*":
                result = m * n
            elif user_opr == "/":
                if n == 0:
                    print("Division by zero is not allowed.")
                    continue
                else:
                    result = m / n    

            print(f"The Result is {result}")

            choice = input("Do you want to use again? (y/n)").lower().strip()  
            if choice != "y":
                print("Goodbye! Thanks For Using")
                break
        except ValueError:
            print("Please! Enter a Valid Number")
            continue


