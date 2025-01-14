from datetime import datetime

print("Welcome! to Our Chatbot App")
print("Start Conversation.. or type 'exit/bye' to quit: ")

now = datetime.now()
current_date = now.strftime("%d-%b-%y")
current_time = now.strftime("%I:%M:%S %p")
current_day = now.strftime("%A")
greetings = ["hi", "hello", "hey", "hy"]
compliments = ["good", "thanks", "awesome"]
response = ""

while True:
    user = input("User: ").lower().strip()

    if user == 'exit' or "bye" in user:
        print("Goodbye! Have a great day!")
        break

    if user in greetings:
        response = "Hello! How can I assist you today?"
    elif user in compliments:
        response = "You're welcome! 😊 If you have more questions I will Assist you"
    elif "date" in user:
        response = f"Today's date is {current_date}"
    elif "day" in user:
        response = f"Today is {current_day}"
    elif "time" in user:
        response = f"Current Time is {current_time}"
    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"    

    print(f"Bot: {response}")
