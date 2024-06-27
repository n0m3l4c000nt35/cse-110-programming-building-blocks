"""
Overview
Practice working with list indexes.

Assignment
Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

Then complete the following:

Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.

Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk

Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.

The following examples show the expected output:


Please enter the items of the shopping list (type: quit to finish):
Item: Milk
Item: Bread
Item: Candy
Item: Carrots
Item: quit

The shopping list is:
Milk
Bread
Candy
Carrots

The shopping list with indexes is:
0. Milk
1. Bread
2. Candy
3. Carrots

Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is:
0. Milk
1. Bread
2. Apples
3. Carrots

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Verify that you can add all the items to the list and display them. (Verify similar to the check point from the previous lesson.)

Iterate through the list using an index. Verify that your program displays the index before the item and that the index starts at 0 for the first item.

Verify that you can ask the user to type an index and a new item.

Set the value at that index to be the new item the user typed. Verify that this does not cause errors.

Print the items out again, and verify that your new item is in the list at the correct spot.
"""

shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish):")
while True:
    item = input("Item: ")
    if item.lower() == "quit":
        break
    shopping_list.append(item)

print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

index = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")