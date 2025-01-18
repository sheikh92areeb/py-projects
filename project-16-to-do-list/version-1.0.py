print("Welcome to the To-Do List Application!")

task_list = []
actions = {1:"add", 2:"view", 3:"update", 4:"delete", 0:"exit"}

while True:
    print("\nChoose an option:")
    print("1- Add Task")
    print("2- View Task")
    print("3- Update Task")
    print("4- Delete Task")
    print("0- Exit\n")

    user_choice = int(input("Enter your Choice: "))

    if user_choice not in actions:
        print("Invalid Action, Please Enter Choice between 1-4 or 0 to exit.")
        continue

    if user_choice == 0:
        print("Goodbye! Thanks For Using To-Do List Application")
        break
    elif user_choice == 1:
        while True:
            add_task = input("Add your Task: ").strip()

            if not add_task:
                print("Please Enter Task Name")
                continue
            else:
                task_list.append(add_task)
                print("Task has been added successfully")
                break
    elif user_choice == 2:
        if not task_list:
            print("No tasks available.")
        else:
            for index, value in enumerate(task_list):
                print(f"Index: {index}, Task: {value}")
    elif user_choice == 3:
        if not task_list:
            print("No tasks available.")
        else:    
            while True:
                task_index = int(input("Enter Index of task to update: "))

                if task_index < 0 or task_index >= len(task_list):
                    print("Invalid Index, Please Enter a Valid Index")
                    continue
                else:
                    print(task_list[task_index])
                    update_task = input("Update Task: ")
                    task_list[task_index] = update_task
                    break
    elif user_choice == 4:
        if not task_list:
            print("No tasks available.")
        else: 
            while True:
                task_index = int(input("Enter Index of task to update: "))

                if task_index < 0 or task_index >= len(task_list):
                    print("Invalid Index, Please Enter a Valid Index")
                    continue
                else:
                    print(task_list[task_index])
                    del_task = input("Are you sure to delete? (y/n): ").lower().strip()
                    while True:
                        if del_task in ["y","n"]:
                            break
                        else:
                            print("Invalid input! Please enter 'y' for yes or 'n' for no.")
                            
                    if del_task == "y":
                        print("Task has been deleted successfully")
                        del task_list[task_index]
                        break

    choice = input("Do you perform more actions? (y/n): ").lower().strip() 
    while True:
        if choice in ["y","n"]:
            break
        else:
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")

    if choice != "y":
        print("Goodbye! Thanks For Using To-Do List Application")
        break