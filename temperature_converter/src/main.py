# TODO: Write a program to convert a Celsius temperature to Fahrenheit and vice versa. 
# 1. Ask the user to to choose between convertion
# 2. Ask the user to enter the temperature value
# 3. Do the correspondant conversion F = C * 9/5 + 32
# 4. Print the result

def temperature_convertion(choice, temp_value):
    if choice == 1:
        result = temp_value * 9/5 + 32
    elif choice == 2:
        result = (temp_value - 32) * 5/9

    else:
        print("Invalid choice")

    print(f"Temperature convertion result: {result}")

while True:
    print("1. Celsius to Fahrenheit:")
    print("2. Fahrenheit to Celsius:")

    try:
        choice = int(input("Choose your convertion type:"))
        temp_value = float(input("Enter the temperature value:"))
        break
    
    except ValueError as e:
        print(f"Invalid choice: {e}")

temperature_convertion(choice, temp_value)
