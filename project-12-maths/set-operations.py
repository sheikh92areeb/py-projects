print("Welcome! Set Operation App\n")

while True:
    user_set1 = input("\nEnter elements for Set 1 (comma-separated): ")
    user_set2 = input("Enter elements for Set 2 (comma-separated): ")

    if not user_set1 or not user_set2:
        print("Empty Input Please Enter Values")
        continue
    else:    
        set1 = set(map(str.strip, user_set1.split(",")))
        set2 = set(map(str.strip, user_set2.split(",")))


    print("\nSelect Action:")
    print("-" * 30)
    print("1: Union")
    print("2: Intersection")
    print("3: Difference")
    print("4: Symmetric Difference")
    print("0: Exit")
    print("-" * 30)

    try:
        user_action = int(input("Enter Your Action: "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 4.\n")
        continue

    if user_action not in [0,1,2,3,4]:
        print("Invalid Action! Please Enter between 1-4 or 0 for exit\n")
        continue

    if user_action == 0:
        print("Goodbye! Thanks For Using")
        break

    if user_action == 1:
        print(f"\nSet 1: {sorted(set1)}")
        print(f"Set 2: {sorted(set2)}")
        union = set1.union(set2)
        print(f"The Union is: {sorted(union)}\n")

    if user_action == 2:
        print(f"\nSet 1: {sorted(set1)}")
        print(f"Set 2: {sorted(set2)}")
        intersection = set1.intersection(set2)
        if not intersection:
            print("The Intersection is empty.\n")
        else:
            print(f"The Intersection is: {sorted(intersection)}\n")

    if user_action == 3:
        print(f"\nSet 1: {sorted(set1)}")
        print(f"Set 2: {sorted(set2)}")
        difference = set1.difference(set2)
        print(f"The Difference is: {sorted(difference)}\n")

    if user_action == 4:
        print(f"\nSet 1: {sorted(set1)}")
        print(f"Set 2: {sorted(set2)}")
        symmetric = set1.symmetric_difference(set2)
        print(f"The Symmetric Difference is: {sorted(symmetric)}\n")

    while True:
        choice = input("\nDo you want to perform another operation? (y/n): ").lower().strip()
        if choice in ["y","n"]:
            break
        else:
            print("Invalid Choice, type 'y' for yes or 'n' for no\n")
            continue
    if choice != 'y':
        print("Goodbye! Thanks For Using")
        break