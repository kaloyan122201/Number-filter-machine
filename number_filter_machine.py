# Welcome to the Filter-number machine
# You add numbers and then you say what do you want to see
# positive numbers, negative numbers, odd numbers or even numbers
# Note: 0 is a positive and even number
# After the machine is done its going to show you the sorted numbers into the category

n = int(input("How many numbers are you going to filter? :"))
positive_numbers = []
negatives_numbers = []
even = []
odd = []
for i in range(n):
    number = int(input("Number: "))
    if number == 0 or number %2 == 0:
        even.append(number)
    elif number % 1 == 0:
        odd.append(number)
    if number >=0:
        positive_numbers.append(number)
    elif number <0:
        negatives_numbers.append(number)
print("Positive | Negative | Odd | Even")
operation = input("Choose an operator:")
if operation == "Even" or operation == "even":
    print(even)
elif operation == "Odd" or operation == "odd":
    print(odd)
elif operation == "Positive" or operation == "positive":
    print(positive_numbers)
elif operation == "Negative" or operation == "negative":
    print(negatives_numbers)
print("The machine is done!")