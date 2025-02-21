import random

def faulty(m,n,o):
    if o == "+":
        return m - n
    elif o == "-":
        return m * n
    elif o == "*":
        return m / n
    elif o == "/":
        return m + n

def calculate(m,n,o):
    if o == "+":
        return m + n
    elif o == "-":
        return m - n
    elif o == "*":
        return m * n
    elif o == "/":
        return m / n

while True:
    random_time = random.randint(1,100)

    m = int(input("Enter First Number: "))
    n = int(input("Enter Second Number: "))
    o = input("Choose Operation (+,-,*,/): ").strip()

    if random_time <= 10:
        result = faulty(m,n,o)
    else:
        result = calculate(m,n,o)

    print(f"Result is {result}")

    while True:
        choise = input("Do you want to use again (y/n): ").strip().lower()
        if choise in ["y", "n"]:
            break
        else:
            print("type 'y' for yes or 'n' for no")
            continue

    if choise != "y":
        print("Goodbye! Thanks for using")
        break