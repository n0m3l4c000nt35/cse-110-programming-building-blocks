## multiple_lists.py

### Overview

Sometimes you have two lists that you want to keep in sync with each other. For example, in this assignment, you will track bank accounts and the balances in each one.

#### Hint from Instructor:

In future courses you will learn how to create a new custom data type (so you aren't limited to ints, floats, and strings). In that case, you can create a data type for bank accounts that stores both the name of the account and it's balance. Then, you only have one list: a list of bank accounts. This is called Programming with Classes or "Object-oriented Programming."

### Assignment

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Create two lists, one for the names of the bank accounts, and one for the balances.

Ask the user for the name of the bank account and then for it's current balance. Keep looping until the user types "quit" for the name of an account. For each one, add the name and the balance to the appropriate list.

Loop through the lists using an index and display the name of the account with the balance next to it.

Compute and display the total balance in all of the accounts and the average balance.

The following shows the expected output:

```
Enter the names and balances of bank accounts (type: quit when done)
What is the name of this account? checking
What is the balance? 102.57
What is the name of this account? savings
What is the balance? 82.32
What is the name of this account? emergency fund
What is the balance? 200.00
What is the name of this account? quit

Account Information:
checking - $102.57
savings - $82.32
emergency fund - $200.0

Total: $384.89
Average: $128.30
```

### STRETCH CHALLENGE

Determine which bank account has the highest balance and display the name and balance of that account.

Change your display so that it shows the index of the account next to the name.

After displaying the list, ask the user if they want to update an account. If they respond with yes, ask for the index of the account, and the new balance.

Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.

The following shows the expected output after completing the stretch challenges:

```
Enter the names and balances of bank accounts (type: quit when done)
What is the name of this account? checking
What is the balance? 238.12
What is the name of this account? savings
What is the balance? 392.99
What is the name of this account? quit

Account Information: 0. checking - $238.12

1. savings - $392.99

Total: $631.11
Average: $315.56
Highest balance: savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 0
What is the new amount? 200

Account Information: 0. checking - $200.00

1. savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 1
What is the new amount? 425.50

Account Information: 0. checking - $200.00

1. savings - $425.50

Do you want to update an account? no

Account Information: 0. checking - $200.00

1. savings - $425.50
```

## shopping_list.py

### Overview

Practice working with list indexes.

### Assignment

Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

Then complete the following:

Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.

Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk

Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.

The following examples show the expected output:

```
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

The shopping list with indexes is: 0. Milk

1. Bread
2. Candy
3. Carrots

Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is: 0. Milk

1. Bread
2. Apples
3. Carrots
```

### Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

Verify that you can add all the items to the list and display them. (Verify similar to the check point from the previous lesson.)

Iterate through the list using an index. Verify that your program displays the index before the item and that the index starts at 0 for the first item.

Verify that you can ask the user to type an index and a new item.

Set the value at that index to be the new item the user typed. Verify that this does not cause errors.

Print the items out again, and verify that your new item is in the list at the correct spot.
