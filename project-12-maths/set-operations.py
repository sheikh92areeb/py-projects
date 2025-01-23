print("Welcome! Set Operation App")

while True:
    user_set1 = input("Enter elements for Set 1 (comma-separated): ")
    user_set2 = input("Enter elements for Set 2 (comma-separated): ")

    set1 = set(user_set1.strip().split(","))
    set2 = set(user_set2.strip().split(","))

    print("Select Action:")
    print("1: Union")
    print("2: Intersection")
    print("3: Difference")
    print("4: Symmetric Difference")
    print("0: Exit")

    user_action = int(input("Enter Your Action: "))

    if user_action not in [0,1,2,3,4]:
        print("Invalid Action! Please Enter between 1-4 or 0 for exit")
        continue

    if user_action == 0:
        print("Goodbye! Thanks For Using")
        break

    if user_action == 1:
        print("The Union of Your Sets is:")
        union = set1.union(set2)
        print(union)

    if user_action == 2:
        print("The Intersection of Your Sets is:")
        intersection = set1.intersection(set2)
        print(intersection)    

    if user_action == 3:
        print("The Difference Between Your Sets is:")
        difference = set1.difference(set2)
        print(difference)

    if user_action == 4:
        print("The Symmetric Difference of Your Sets is:")
        symmetric = set1.symmetric_difference(set2)
        print(symmetric)

    while True:
        choice = input("Do you want to perform another operation? (y/n): ").lower().strip()
        if choice in ["y","n"]:
            break
        else:
            print("Invalid Choice, type 'y' for yes or 'n' for no")
            continue
    if choice != 'y':
        print("Goodbye! Thanks For Using")
        break