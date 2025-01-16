def avg(numbers):    
    if not numbers:
        return 0 
    return sum(numbers) / len(numbers)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))
print(avg(numbers))