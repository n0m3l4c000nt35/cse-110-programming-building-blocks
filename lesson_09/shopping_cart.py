"""
Overview
Many apps use some type of shopping cart, where users can add items to the cart, remove items, view the contents of the cart, and see the total. Storing this collection of items requires keeping track of a list of items and updating it in various ways.

Project Description
For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

For the milestone deliverable, you only need to worry about storing a list of the names of the items (not the prices yet), and only need to be able to add new items and display the list. Then, for the complete project, you'll add the ability to store the prices, remove items, and compute the total.

Assignment
For this project, the user will be given a menu and have the ability to choose items from the menu. The options in the menu include the following:

Add a new item

Display the contents of the shopping cart

Remove an item (only needed for the final project deliverable)

Compute the total (only needed for the final project deliverable)

Quit

When the user chooses one of these options, the program should perform the appropriate action. Then the program should show them the menu again, and allow them to choose another option. It should continue running until the user choose the option to quit.

The following sections outline the expected behavior of each option:

ADD A NEW ITEM
The program asks the user for the name of the item. For the final project deliverable it should also ask the user for the price of the item.

The program stores these values in a list. When you are working on the milestone deliverable, you will only need one list (to store the names). For the final project, when you are storing both names and prices, you should use two lists, one for the names and one for the prices.

An example of the functionality of this item could look as follows:


What item would you like to add? socks
What is the price of 'socks'? 5.99
'socks' has been added to the cart.
After the user provides these values, the item and its price are stored in the list.

Hint: You should create new blank lists at the beginning of the program, so that when you get to this point, you'll have a list already in place in which you can store the name or price.

DISPLAY THE CONTENTS OF THE SHOPPING CART
The program should display all of the items in the shopping cart, one per line. For the milestone deliverable, you only need to display the names of the items. For the final project deliverable, the price of each item should be displayed next to the item.

Also, for the final project, the program should also display the number associated with each item in the list, beginning with 1. This is different than how Python will store them, because it will start counting at 0, but to make it more natural for the user, you should start the numbers at 1.

An example of the functionality of this item could look as follows:


The contents of the shopping cart are:
1. bed - $100.00
2. chair - $24.99
3. blanket - $48.50

REMOVE AN ITEM
The user types in the number of the item they want to remove and the item is removed from the list.

In order to do this correctly, your program will need to do each of the following:

Convert the number the user enters to a 0-based index. For example, if they want to remove the second item in the list they will type "2" (because they will see the numbers starting at 1), but this item will be stored in Python at index 1 (because Python will start counting at 0).

Make sure that the index is within the bounds of the current list (for example, you cannot remove item 10 if there are only 5 items in the list). If the index is outside the bounds of the list, you should not attempt to remove it, but rather, display a message informing the user that they have made an invalid choice.

Remove the item at that spot in the list. Don't forget that if you are storing names and prices, you'll need to remove both the name and the price from their respective lists.

The following shows an example of this functionality assuming there are 5 items in the list:


Which item would you like to remove? 3
Item removed.

Which item would you like to remove? 13
Sorry, that is not a valid item number.

COMPUTE THE TOTAL
The program should iterate through each item in the list and add up the prices and then display the total amount to the user.

The following shows the expected result, assuming the total amount of the items in the shopping cart is $35.68


The total price of the items in the shopping cart is $35.68

The following shows an example of the complete program:


Welcome to the Shopping Cart Program!

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 1
What item would you like to add? Milk
What is the price of 'Milk'? 3.49
'Milk' has been added to the cart.

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 1
What item would you like to add? Bread
What is the price of 'Bread'? 2.50
'Bread' has been added to the cart.

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 1
What item would you like to add? Butter
What is the price of 'Butter'? 4.00
'Butter' has been added to the cart.

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 2
The contents of the shopping cart are:
1. Milk - $3.49
2. Bread - $2.50
3. Butter - $4.00

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 3
Which item would you like to remove? 2
Item removed.
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 2
The contents of the shopping cart are:
1. Milk - $3.49
2. Butter - $4.00

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 4
The total price of the items in the shopping cart is $7.49

Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 5
Thank you. Goodbye.

Showing Creativity and Exceeding Requirements
In addition to the functionality listed above, add something of your own creativity to the assignment. You could consider adding better formatting (for example, aligning the prices), storing extra information, such as the quantity of the items in the list, or you can add anything else you think of to make the shopping cart better.
"""

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