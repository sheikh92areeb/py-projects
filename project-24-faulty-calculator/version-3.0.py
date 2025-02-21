import random

faultyOps = { "+": "-", "-": "/", "*": "+", "/": "*" }
correctOps = { "+": "+", "-": "-", "*": "*", "/": "/" }

while True:
    random_time = random.randint(1,100)

    m = int(input("Enter First Number: "))
    n = int(input("Enter Second Number: "))
    o = input("Choose Operation (+,-,*,/): ").strip()

    ops = faultyOps[o] if random_time <= 10 else correctOps[o]
    result = eval(f"{m} {ops} {n}")

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