def missing_char(input_str):

    full_set = set("0123456789abcdefghijklmnopqrstuvwxyz")
    input_set = set(input_str.lower())
    missing_characters = sorted(full_set - input_set)
    return "".join(missing_characters)


input_string = input("Enter a string: ")

print(missing_char(input_string))