import random

random_time = random.randint(1,100)

m = int(input("Enter First Number: "))
n = int(input("Enter Second Number: "))
o = input("Choose Operation (+,-,*,/): ").strip()

if random_time <= 10:
    if o == "+":
        print(m - n)
    elif o == "-":
        print(m * n)
    elif o == "*":
        print(m / n)
    elif o == "/":
        print(m + n)
else:
    if o == "+":
        print(m + n)
    elif o == "-":
        print(m - n)
    elif o == "*":
        print(m * n)
    elif o == "/":
        print(m / n)