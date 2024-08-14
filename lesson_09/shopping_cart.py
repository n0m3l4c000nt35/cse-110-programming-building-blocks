item_names = []
item_prices = []

def display_menu():
    """Display the menu options to the user."""
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item():
    """Add an item and its price to the shopping cart."""
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    item_names.append(item)
    item_prices.append(price)
    print(f"'{item}' has been added to the cart.")

def view_cart():
    """Display the contents of the shopping cart."""
    if not item_names:
        print("Your shopping cart is empty.")
    else:
        print("The contents of the shopping cart are:")
        for i, (item, price) in enumerate(zip(item_names, item_prices), start=1):
            print(f"{i}. {item} - ${price:.2f}")

def remove_item():
    """Remove an item from the shopping cart by its number."""
    if not item_names:
        print("Your shopping cart is empty.")
    else:
        try:
            item_num = int(input("Which item would you like to remove? "))
            if 1 <= item_num <= len(item_names):
                removed_item = item_names.pop(item_num - 1)
                item_prices.pop(item_num - 1)
                print(f"Item '{removed_item}' removed.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Please enter a valid number.")

def compute_total():
    """Compute and display the total price of the items in the shopping cart."""
    if not item_prices:
        print("Your shopping cart is empty.")
    else:
        total = sum(item_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

def main():
    """Main function to run the shopping cart program."""
    print("Welcome to the Shopping Cart Program!")
    
    while True:
        display_menu()
        choice = input("Please enter an action: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            compute_total()
        elif choice == "5":
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()