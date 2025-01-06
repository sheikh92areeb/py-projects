import string

print("Welcome! to the Word Counter")

while True:
    special_char = string.punctuation

    user_sentence = input("Enter Your Word or Sentence Here: ").strip()

    if not user_sentence:
        print("Error: You entered an empty sentence!")
        continue

    words = len(user_sentence.split())
    total_char = len(user_sentence)
    char_ws = len(user_sentence.replace(" ", ""))
    spaces = total_char - char_ws
    punctuation_char = 0

    for i in user_sentence:
        if i in special_char:
            punctuation_char += 1

    print(f"Your Sentence contains {words} word{'s' if words != 1 else ''}.")
    print(f"Your Sentence contains {total_char} total character{'s' if total_char != 1 else ''}.")
    print(f"Your Sentence contains {char_ws} character{'s' if char_ws != 1 else ''} without space.")
    print(f"Your Sentence contains {spaces} space{'s' if spaces != 1 else ''}.")
    print(f"Your Sentence contains {punctuation_char} special charecter{'s' if punctuation_char != 1 else ''}.")
    break