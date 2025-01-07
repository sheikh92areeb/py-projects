import string

print("Welcome! to Palindrome Checker")
print("Check your word or phrase is Palindrome or not")

user_input = input("Enter Your word or phrase: ").lower().strip()
clear_space = user_input.replace(" ", "")
cleaned_string = ''.join(char for char in clear_space if char not in string.punctuation)
normalize_word = cleaned_string[::-1]

if normalize_word == cleaned_string:
    print("It is Palindrome")
else:
    print("It is not Palindrome")    