def unit_conversion(value, current_unit , convert_unit):
    if current_unit == 1 and convert_unit == 2:
        return (value * 9/5) + 32
    elif current_unit == 2 and convert_unit == 1:
        return (value - 32) * 5/9
    elif current_unit == 1 and convert_unit == 3:
        return value + 273.15
    elif current_unit == 3 and convert_unit == 1:
        return value - 273.15
    elif current_unit == 2 and convert_unit == 3:
        return (value - 32) * 5/9 + 273.15
    elif current_unit == 3 and convert_unit == 2:
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid Units"

print("Welcome! to Temperature Concertor App")
print("Type 1 for 'Celsius', 2 for 'Fahrenheit', 3 for 'Kelvin'")

options = {1:"Celsius", 2:"Fahrenheit", 3:"Kelvin"}

while True:
    try:
        temp_value = int(input("Enter Temperature value: "))
        current_unit = int(input("Current temperature unit: "))
        convert_unit = int(input("Unit for conversion: "))

        if current_unit not in options or convert_unit not in options:
            print("Invalid Option, Please Enter between (1-3)")
            continue
        else:
            result = unit_conversion(temp_value, current_unit, convert_unit)

        print(f"{temp_value} {options[current_unit]} is Equal to {result:.2f} {options[convert_unit]}")

        while True:
            choice = input("Do you want to use again? (y/n): ").lower().strip()
            if choice in ["y","n"]:
                break
            else:
                print("Invalid Choice, Please type 'y' for yes or 'n' for no")
                continue
        if choice != "y":
            print("Goodbye! Thanks for using")        
            break

    except ValueError:
        print("Invalid Input, Please Enter Numeric Value")
        continue