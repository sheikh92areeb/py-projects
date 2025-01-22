print("Welcome! to Inventory Management System")
print("Setup Your Inventory\n")

inventory = {}
actions = { 1:"add", 2:"update", 3:"remove", 4:"view", 0:"exit" }

while True:
    print("Select Action:")
    print("1. Add a new item")
    print("2. Update an item's quantity")
    print("3. Remove an item")
    print("4. View all items")
    print("0. Exit")

    try:
        user_action = int(input("Enter your action: "))

        if user_action not in actions:
            print("Invalid Action, Please Enter action between 1-4 or 0 for exit")
            continue
        else:
            if user_action == 0:
                print("Goodbye! Thanks For Using Inventory System")
                break
            elif user_action == 1:
                while True:
                    key = input("Enter Item Name: ").strip()

                    if key not in inventory:
                        value = int(input("Enter Item Quantity: "))

                        if 0 > value:
                            print("Please Enter Positive Value")
                            continue
                        else:
                            inventory = {key:value}
                            print(f"{key} has been added successfully")
                            break
            elif user_action == 2:
                while True:
                    key = input("Enter Item Name: ").strip()

                    if key not in inventory:
                        print(f"{key} is not Exist")
                        continue
                    else:
                        old_value = inventory[key]
                        print(f"Item: {key} Quantity: {old_value}")
                        value = int(input("Update Item Quantity: "))

                        if 0 > value:
                            print("Please Enter Positive Value")
                            continue
                        else:
                            inventory = {key:value}
                            print(f"{key}'s Quantity has been updated successfully")
                            break
            elif user_action == 3:
                while True:
                    key = input("Enter Item Name: ").strip()

                    if key not in inventory:
                        print(f"{key} is not Exist")
                        continue
                    else:
                        print(f"Item: {key} Quantity: {inventory[key]}")
                        while True:
                            confirm = input("Are you sure to delete? (y/n):").lower().strip()
                            if confirm in ["y","n"]:
                                break
                            else:
                                print("Invalid Choice, Type 'y' for yes or 'n' for no")
                                continue
                        if confirm == "y":
                            del inventory[key]
                            print(f"{key} has been removed successfully")
                            break
                        else:
                            break
            elif user_action == 4:
                if not inventory:
                    print("No Item Available")
                    continue
                else:
                    for key, value in inventory.items():
                        print(f"Item : {key} Quantity : {value}")
                    continue    

    except ValueError:
        print("Invalid Input, Please Enter action between 1-4 or 0 for exit")
        continue
    
    while True:
        choice = input("Do you want to use again? (y/n): ").lower().strip()
        if choice in ["y","n"]:
            break
        else:
            print("Invalid Choice, Type 'y' for yes or 'n' for no")
            continue
    if choice != "y":
        print("Goodbye! Thanks For Using Inventory System")
        break