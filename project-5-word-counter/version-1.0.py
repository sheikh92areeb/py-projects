print("Welcome! to the Word Counter")

user_word = input("Enter Your word or Sentence Here: ").strip()

words = 0
total_char = 0
char_ws = 0
space = 0

words = len(user_word.split(" "))
total_char = len(user_word)
char_ws = len(user_word.replace(" ",""))
space = total_char - char_ws

print(f"Your sentence contains {words} words.")
print(f"Your sentence contains {total_char} Total characters.")
print(f"Your sentence contains {char_ws} characters without spaces.")
print(f"Your sentence contains {space} spaces.")
