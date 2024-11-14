# TODO: Write a program to manage a store inventory.
# 1. Define a dictionary with product names and values
# 2. Print the current inventory
# 3. Allow the user to add new products or update existing ones. 
# 4. Allow the user to remove products from the inventory

inventory = {
    "apples": 30,
    "oranges": 42,
    "pineapples": 12,
    "tomatoes": 3,
}

def display_inventory():
    print("Current inventory:")
    print("-"*10)
    for keys, values in inventory.items():
        print(f"{keys}: {values}")
    print("-"*10)

def display_options():
    print("1. Add or update product")
    print("2. Remove product")
    print("3. Exit")

def add_update_product(key, value):
    inventory[key] = value

def remove_product(key):
    if key in inventory:
        inventory.pop(key)
    else:
        print("This product does not exists")

while True:

    display_inventory()
    display_options()

    try:
        choice = int(input("Select operation:"))
    except ValueError as e:
        print("Invalid option: {e}")

    if choice == 1:
        key = str(input("Enter product name: "))
        value = int(input("Enter product quantity: "))
        add_update_product(key, value)

    elif choice == 2:
        key = str(input("Enter product name to remove: ")).strip().lower()
        remove_product(key)

    elif choice == 3:
        break

    else:
        print("Invalid choice")