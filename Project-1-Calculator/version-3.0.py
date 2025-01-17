def calculation(op, n, m):
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


print("Welcome! to Simple Calculator \n")
print("Operations")
print("+ for Addition")
print("- forSubtraction")
print("* for Multiplication")
print("/ for Division")
print("0 for Exit")

operators = ["0","+","-","*","/"]

while True:
    user_opr = input("\nSelect Your Operation: ")

    if user_opr not in operators:
        print("Invalid operator. Please choose from +, -, *, /, or 0.") 
        continue
    elif user_opr == "0":
        print("Goodbye! Thanks For Using")       
        break
    else:
        try:
            m = int(input("Enter First Number: "))
            n = int(input("Enter Second Number: "))

            # if user_opr == "+":
            #     result = m + n
            # elif user_opr == "-":
            #     result = m - n
            # elif user_opr == "*":
            #     result = m * n
            # elif user_opr == "/":
            #     if n == 0:
            #         print("Division by zero is not allowed.")
            #         continue
            #     else:
            #         result = m / n    

            # print(f"The Result is {result}")

            print("Result is ", calculation(user_opr, n,m))


            while True:
                choice = input("Do you want to use again? (y/n)").lower().strip()  
                if choice in ["y","n"] :
                    break
                else:
                    print("Invalid input! Please enter 'y' for yes or 'n' for no.")

            if choice != "y":
                print("Goodbye! Thanks For Using")
                break
        except ValueError:
            print("Please! Enter a Valid Number")
            continue


