import string
import re

print("Welcome! to Vowel Counter")
print("Enter Word or Sentence for Counting Vowels and Cononant")

while True:
    special_char = string.punctuation
    vowel_list = ["a", "e", "i", "o", "u"]
    vowels = 0
    consonants = 0

    user_input = input("Enter Your Word or Sentence Here: ").strip().lower()

    if not user_input:
        print("Error: You entered an empty sentence!")
        continue

    clear_spaces = user_input.replace(" ", "")
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', clear_spaces)

    for i in cleaned_string:
        if i in vowel_list:
            vowels += 1
        else:
            consonants += 1    

    print(f"The sentence '{user_input}' contains:")
    print(f"🎵 Vowels: {vowels}")
    print(f"🔤 Consonants: {consonants}")


    choice = input("Do you want to check more? (y/n)").lower().strip()
    if choice != "y":
        print("Goodbye! Thanks for using the program")
        break