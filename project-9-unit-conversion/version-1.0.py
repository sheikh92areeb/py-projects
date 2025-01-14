print("Welcome! to Unit Converter")
print("Unit Converter Menu:")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")

while True:
    user = input("Enter your Choice (1 to 6) or type 'exit' to quit: ")

    if user == 'exit':
        print("Goodbye! Thanks For Using")
        break

    value = int(input("Enter Value to Convert: "))

    match user:
        case 1:
            formula = value * 0.621371
            unit = "Kilometers"
            convert = "Miles"
        case 2:
            formula = value / 0.621371
            unit = "Miles"
            convert = "Kilometers"
        case 3:
            formula = (value * 9/5) + 32 
            unit = "Celsius"
            convert = "Fahrenheit"
        case 4:    
            formula = (value - 32) * 5/9
            unit = "Fahrenheit"
            convert = "Celsius"
        case 5:
            formula =  value * 2.20462    
            unit = "Kilograms"
            convert = "Pounds"
        case 6:
            formula = value / 2.20462    
            unit = "Pounds"
            convert = "Kilograms"


    print(f"{value} {unit} is equal to {formula:.2f} {convert}")

    choice = input("Do you want to use again? (y/n)").lower().strip()
    if choice != "y":
        print("Goodbye! Thanks For Using")
        break