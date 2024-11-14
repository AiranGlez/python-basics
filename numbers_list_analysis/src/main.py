# TODO: Write a function that takes a list of int numbers and do the following operations:
# 1. Calculate and print the largest and smallest numbers 
# 2. Calculate and print the average
# 3. Return a new list with only even numbers

def number_list_operations(number_list):

    largest = max(number_list)
    smallest = min(number_list)
    average = sum(number_list) / len(number_list)
    even_numbers = [num for num in number_list if num % 2 == 0]

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Average: {average}")
    print(f"Even numbers list: {even_numbers}")

def get_number_list():

    while True:
        number_list = input("Enter a list of numbers separated by whitespaces: ")
        number_list = number_list.split()

        try:
            number_list = [int(num) for num in number_list]
            return number_list
        except ValueError:
            print("Invalid input. Try numbers only separated by spaces")

number_list = get_number_list()
print(f"User number list: {number_list}")

number_list_operations(number_list)
