"""
Overview
Programs can obtain information from users and then combine those values to compute meaningful results. In this assignment, you will write a program to calculate the price of a meal.

Instructions
Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

Ask the user for the following:

The price of a child's meal (floating point)

The price of an adult's meal (floating point)

The number of children (integer)

The number of adults (integer)

The sales tax rate (floating point)

Then, complete the following steps:

Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and multiplying the number of adults by the price of their meal and adding those two values together.

Display the subtotal.

Hint from Instructor:
As you will see in the requirements list below, this is as far as you need to get for the milestone requirements of Lesson 03, but you should try to get as far as you can during Lesson 03 to make it even easier for yourself in the next lesson, especially if you run into trouble.

Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

Compute and display the total price of the meal by adding the subtotal and the sales tax.

Finally:

Ask the user for the the payment amount (floating point)

Compute and display the change.

A sample run of the program might look as follows:


What is the price of a child's meal? 4.50
What is the price of an adult's meal? 9.00
How many children are there? 4
How many adults are there? 2
What is the sales tax rate? 6

Subtotal: $36.00
Sales Tax: $2.16
Total: $38.16

What is the payment amount? 40
Change: $1.84

Another example, in which the user typed different values, might look like this:


What is the price of a child's meal? 2.25
What is the price of an adult's meal? 6.99
How many children are there? 2
How many adults are there? 1
What is the sales tax rate? 4

Subtotal: $11.49
Sales Tax: $0.46
Total: $11.95

What is the payment amount? 20
Change: $8.05

Showing Creativity and Exceeding Requirements
For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage, or anything else you can think of. Play around with different ideas and see what you can learn!

Milestone Requirements
At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.

Ask the user for the number of adults and children and store these values properly into variables as integers.

Ask the user for the sales tax rate and store the value properly as a floating point number.

Compute and display the subtotal (don't worry about rounding to two decimals at this point).

Final requirements
At the end of Lesson 04, in addition to the milestone requirements above, you need to also complete the following:

Compute and display the sales tax.

Compute and display the total.

Ask the user for the payment amount and store the value properly as a floating point number.

Compute and display the change.

Include a dollar sign ($) before each displayed value.

Display each value to two decimals.

Double check that the calculations are correct.

Show creativity and exceed the core requirements by adding additional features.

Use good style in your program, including variable names and whitespace.
"""

price_child_meal = float(input("What is the price of a child's meal? "))
price_adult_meal = float(input("What is the price of an adult's meal? "))

number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

sales_tax_rate = float(input("What is the sales tax rate? "))

subtotal = (price_child_meal * number_of_children) + (price_adult_meal * number_of_adults)

print(f"Subtotal: ${subtotal:.2f}")

sales_tax = subtotal * (sales_tax_rate / 100)

total_price = subtotal + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total_price:.2f}")

payment_amount = float(input("What is the payment amount? "))

change = payment_amount - total_price
print(f"Change: ${change:.2f}")

"""
Explanation of the Code

1. The program prompts the user to enter the prices of a child's meal and an adult's meal, storing these values as floating point numbers.
2. It then asks for the number of children and adults, storing these values as integers.
3. The user is prompted to enter the sales tax rate, which is stored as a floating point number.
.4 The subtotal is calculated by multiplying the number of children by the price of a child's meal and the number of adults by the price of an adult's meal, then adding these two values together.
5. The subtotal is displayed.
6. The sales tax is computed by multiplying the subtotal by the sales tax rate divided by 100.
7. The total price of the meal is calculated by adding the sales tax to the subtotal.
8. The program then asks for the payment amount, computes the change, and displays the change.
"""