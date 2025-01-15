print("Welcome! To Character Counter")
print("Count the Characters of your words or sentence")

while True:
    user_word = input("Enter Your Word or type 'exit' to quit: ").strip().lower()

    if user_word == "exit":
        print("Goodbye! Thanks For Using")
        break

    char_count = {}

    for i in user_word:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for key, value in char_count.items():
        print(key, "=", value)

    choice = input("Do you want to count more? (y/n): ").strip().lower()        
    if choice != "y":
        print("Goodbye! Thanks For Using")
        break