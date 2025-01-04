print("Simple Calculator")
print("Perform your Calculation here")
print("Supported Operators are +, -, *, /")

while True:
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))
    opr = input("Enter the operator: ").strip()

    if opr == "+":
        print(f"The Addition of {n} and {m} is {n + m}")
    elif opr == "-":
        print(f"The Subtraction of {n} and {m} is {n - m}")
    elif opr == "*":
        print(f"The Multiplication of {n} and {m} is {n * m}")
    elif opr == "/":
        if m == 0:
            print("Division by Zero is not allowed")
        else:
            print(f"The division of {n} and {m} is {n / m}")
    else:
        print("Invalid Operator excepted are +, -, *, /")
    
    choice = input("Do you want to continue? (y/n): ").lower().strip()
    if choice != "y":
        print("Thank you for using the calculator")
        break