print("Simple Calculator")
print("Perform your Calculation here")
print("Supported Operators are +, -, *, /")

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
opr = input("Enter the operator: ")

if opr == "+":
    print(f"The Addition of {n} and {m} is {n + m}")
elif opr == "-":
    print(f"The Subtraction of {n} and {m} is {n - m}")
elif opr == "*":
    print(f"The Multiplication of {n} and {m} is {n * m}")
elif opr == "/":
    print(f"The division of {n} and {m} is {n / m}")
else:
    print("Invalid Operator")