print("Welcome! to Quiz App")
print("Answer simple questions and get points")
print("Let's Play!\n")

user_score = 0
correct_answers = []
wrong_answers = []
answers = ["a","b","c","d"]
question_id = 1

questions = {
    "Q-1": {"question":"What is the capital of France?", 
    "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], 
    "answer": "c" },

    "Q-2": {"question":"What is the national language of U.K?", 
    "options": ["A. English", "B. Spanish", "C. French", "D. Roman"],
    "answer": "a" }
}

while True:
    for idx, (key, value) in enumerate(questions.items(), 1):
        print(f"Here is Question: {idx}")
        print(f"Question: {value['question']}")
        print("Options:")
        for option in value["options"]:
            print(f"  {option}")    

        while True:
            user_answer = input("Enter Your Answer (A - D): ").lower().strip()

            if user_answer not in answers:
                print("Invalid Option, Please Enter between (A - D)")
                continue
            else:
                break

        if user_answer == value["answer"]:
            print("Correct Answer, Great Job\n")
            user_score += 10
            correct_answers.append(key)
        else:
            print("Wrong Answer")
            print(f"Correct Answer is {value['answer']}\n")
            wrong_answers.append(key)

    print("Quiz Over!")
    print("Game Summary")
    print("Correct Answers:")
    if not correct_answers:
        print("No Answer is correct\n")
    else:
        for i in correct_answers:
            print(f"{i} is correct")

    print("\nWrong Answers:")
    if not wrong_answers:
        print("Great! No Answer is Wrong\n")
    else:
        for i in wrong_answers:
            print(f"{i} is wrong")

    if user_score == 0:
        print(f"Your Score is {user_score}, Better Luck Next Time\n")
    else:
        print(f"Your Score is {user_score}, You Played Well!\n")    

    correct_answers.clear()
    wrong_answers.clear()
    user_score = 0
    
    while True:
        choice = input("Do you want to play again? (y/n): ")
        if choice in ["y","n"]:
            break
        else:
            print("Invalid Choice, Please Enter 'y' for yes or 'n' for no")
            continue
    if choice != "y":
        print("Goodbye! Thanks For Playing")
        break