print("Welcome! to Contact Book Application")

actions = {1:"add", 2:"search", 3:"update", 4:"delete", 5:"view", 0:"exit"}
contact_list = {}

while True:
    print("\nChoose an option:")
    print("1- Add Contact")
    print("2- Search Contact")
    print("3- Update Contact")
    print("4- Delete Contact")
    print("5- View Contact")
    print("0- Exit\n")

    try:
        user_action = int(input("Enter your Choice: "))

        if user_action not in actions:
            print("Invalid Choice, Please Enter choice between 1-5 or 0 to exit.")
            continue

        if user_action == 0:
            print("Goodbye! Thanks For Using Contact Book")
            break
                
        if user_action == 1:
            while True:
                key = input("Enter Name: ").strip()
                value = input("Enter Number: ").strip()

                if value.isdigit():
                    contact_list.update({key:value})
                    print("Contact has been added successfully")
                    break
                else:
                    print("Invalid Number, Please Enter Valid Number")
                    continue
        elif user_action == 2:

            if not contact_list:
                print("No Contact Available")
            else:
                key = input("Search Contact: ").strip()
                if key not in contact_list:
                    print("No Result Found")
                else:
                    print(contact_list[key])
        elif user_action == 3:
            while True:
                key = input("Enter Name: ").strip()

                if key not in contact_list:
                    print(f"{key}: is not exist")
                    continue
                else:
                    value = input("Update Number: ").strip()

                    if value.isdigit():
                        contact_list.update({key:value})
                        print("Contact has been updated successfully")
                        break
                    else:
                        print("Invalid Number, Please Enter Valid Number")    
                        continue
        elif user_action == 4:
            while True:
                key = input("Enter Name: ").strip()

                if key not in contact_list:
                    print(f"{key}: is not exist")
                    continue
                else:
                    print(f"Name: {key}, Number: {contact_list[key]}")
                    while True:
                        confirm = input("Are you sure to delete? (y/n): ").strip().lower()
                        if confirm in ["y", "n"]:
                            break
                        else:
                            print("Invalid input! Please enter 'y' for yes or 'n' for no.")
                            continue
                    if confirm == "y":
                        del contact_list[key]
                        print("Contact has been deleted successfully")
                        break
                    break
        elif user_action == 5:
            if not contact_list:
                print("No Contact Available")
            else:
                for key, value in contact_list.items():
                    print(f"Name: {key}: Number : {value}")


        while True:
            choice = input("Do you want to use again? (y/n): ").lower().strip()
            if choice in ["y","n"]:
                break
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")
                continue
        if choice != "y":
            print("Goodbye! Thanks for using contact book")
            break            
    except ValueError:
        print("Invalid Input, Please Enter number between 1-5 or 0 to exit.")
        continue