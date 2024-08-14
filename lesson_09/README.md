## lists_of_numbers.py

### Assignment

Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

Once you have a list, have your program do the following:

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Compute the sum, or total, of the numbers in the list.

Compute the average of the numbers in the list.

Find the maximum, or largest, number in the list.

The following shows the expected output:

```
Enter a list of numbers, type 0 when finished.
Enter number: 18
Enter number: 36
Enter number: 2
Enter number: 48
Enter number: 6
Enter number: 12
Enter number: 9
Enter number: 0
The sum is: 131
The average is: 18.714285714285715
The largest number is: 48
```

### STRETCH CHALLENGE

Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

The following shows the expected output after completing the stretch challenges:

```
Enter a list of numbers, type 0 when finished.
Enter number: 3
Enter number: 5
Enter number: 7
Enter number: 3
Enter number: 2
Enter number: -1
Enter number: -4
Enter number: -8
Enter number: 0
The sum is: 7
The average is: 0.875
The largest number is: 7
The smallest positive number is: 2
The sorted list is:
-8
-4
-1
2
3
3
5
7
```

## lists.py

### Overview

Practice working with lists.

### Assignment

Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

**Hint 1**: You should keep asking for friends, as long as the name is not "end". (Does this sound like a loop you know?)

**Hint 2**: Be careful not to add "end" to the list of names when it is typed. You can check if the name is or is not something before you add it to the list.

The following examples show the expected output:

```
Type the name of a friend: Matthew
Type the name of a friend: Mark
Type the name of a friend: Luke
Type the name of a friend: John
Type the name of a friend: end

Your friends are:
Matthew
Mark
Luke
John
```

Another example could be the following:

```
Type the name of a friend: Peter
Type the name of a friend: James
Type the name of a friend: John
Type the name of a friend: end

Your friends are:
Peter
James
John
```

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Test it with just one name.

Test it with 3–4 names

Make sure that the word "end" doesn't display at the end of your list of friends.

Test it by entering the same name 3 times before typing end (the result should be that you see the name repeated 3 times in the list).

Test it with no names, just the word end, and make sure it doesn't cause any errors.

## shopping_cart.py

### Overview

Many apps use some type of shopping cart, where users can add items to the cart, remove items, view the contents of the cart, and see the total. Storing this collection of items requires keeping track of a list of items and updating it in various ways.

### Project Description

For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

For the milestone deliverable, you only need to worry about storing a list of the names of the items (not the prices yet), and only need to be able to add new items and display the list. Then, for the complete project, you'll add the ability to store the prices, remove items, and compute the total.

### Assignment

For this project, the user will be given a menu and have the ability to choose items from the menu. The options in the menu include the following:

- Add a new item
- Display the contents of the shopping cart
- Remove an item (only needed for the final project deliverable)
- Compute the total (only needed for the final project deliverable)
- Quit

When the user chooses one of these options, the program should perform the appropriate action. Then the program should show them the menu again, and allow them to choose another option. It should continue running until the user choose the option to quit.

The following sections outline the expected behavior of each option:

#### ADD A NEW ITEM

The program asks the user for the name of the item. For the final project deliverable it should also ask the user for the price of the item.

The program stores these values in a list. When you are working on the milestone deliverable, you will only need one list (to store the names). For the final project, when you are storing both names and prices, you should use two lists, one for the names and one for the prices.

An example of the functionality of this item could look as follows:

```
What item would you like to add? socks
What is the price of 'socks'? 5.99
'socks' has been added to the cart.
```

After the user provides these values, the item and its price are stored in the list.

**Hint**: You should create new blank lists at the beginning of the program, so that when you get to this point, you'll have a list already in place in which you can store the name or price.

#### DISPLAY THE CONTENTS OF THE SHOPPING CART

The program should display all of the items in the shopping cart, one per line. For the milestone deliverable, you only need to display the names of the items. For the final project deliverable, the price of each item should be displayed next to the item.

Also, for the final project, the program should also display the number associated with each item in the list, beginning with 1. This is different than how Python will store them, because it will start counting at 0, but to make it more natural for the user, you should start the numbers at 1.

An example of the functionality of this item could look as follows:

```
The contents of the shopping cart are:

1. bed - $100.00
2. chair - $24.99
3. blanket - $48.50
```

#### REMOVE AN ITEM

The user types in the number of the item they want to remove and the item is removed from the list.

In order to do this correctly, your program will need to do each of the following:

Convert the number the user enters to a 0-based index. For example, if they want to remove the second item in the list they will type "2" (because they will see the numbers starting at 1), but this item will be stored in Python at index 1 (because Python will start counting at 0).

Make sure that the index is within the bounds of the current list (for example, you cannot remove item 10 if there are only 5 items in the list). If the index is outside the bounds of the list, you should not attempt to remove it, but rather, display a message informing the user that they have made an invalid choice.

Remove the item at that spot in the list. Don't forget that if you are storing names and prices, you'll need to remove both the name and the price from their respective lists.

The following shows an example of this functionality assuming there are 5 items in the list:

```
Which item would you like to remove? 3
Item removed.

Which item would you like to remove? 13
Sorry, that is not a valid item number.
```

#### COMPUTE THE TOTAL

The program should iterate through each item in the list and add up the prices and then display the total amount to the user.

The following shows the expected result, assuming the total amount of the items in the shopping cart is $35.68

The total price of the items in the shopping cart is $35.68

The following shows an example of the complete program:

```
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
6. Milk - $3.49
7. Bread - $2.50
8. Butter - $4.00

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
6. Add item
7. View cart
8. Remove item
9. Compute total
10. Quit
    Please enter an action: 2
    The contents of the shopping cart are:
11. Milk - $3.49
12. Butter - $4.00

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
```

### Showing Creativity and Exceeding Requirements

In addition to the functionality listed above, add something of your own creativity to the assignment. You could consider adding better formatting (for example, aligning the prices), storing extra information, such as the quantity of the items in the list, or you can add anything else you think of to make the shopping cart better.
