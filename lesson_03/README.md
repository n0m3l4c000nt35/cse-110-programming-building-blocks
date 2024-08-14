## areas_of_shapes.py

### Overview

Python can be used to calculate values for data analysis and complex mathematical and scientific problems. In this activity, you will practice using variables and expressions for straight-forward math calculations. The purpose of the assignment is to help you become more comfortable using variables to accomplish a problem, not to focus on the actual math at hand.

### Assignment

Start by completing the core requirements, then when that part is complete, if you have time, see if you can complete some of the stretch challenges as well.

### CORE REQUIREMENTS

Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

An example run of the program might look something like the following:

What is the length of a side of the square? 5
The area of the square is: 25.0
What is the length of rectangle? 6
What is the width of the rectangle? 7
The area of the rectangle is: 42.0
What is the radius of the circle? 5
The area of the circle is: 78.5
Another run could be the following:

What is the length of a side of the square? 3.5
The area of the square is: 12.25
What is the length of rectangle? 6
What is the width of the rectangle? 7.5
The area of the rectangle is: 45.0
What is the radius of the circle? 8.2
The area of the circle is: 211.1336

### STRETCH CHALLENGE

Once you have finished the core requirements, you are welcome to move on to the stretch challenges. These can be more difficult and may require finding solutions that weren't directly covered in the reading. These aren't specifically required for the assignment, but are a great chance to dive deeper into the concepts of the lesson.

The stretch challenges for this activity are:

Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module. Hint, you might try searching on the internet for something like, "python how to get the value of pi."

Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.

## meal_price_calculator.py

### Overview

Programs can obtain information from users and then combine those values to compute meaningful results. In this assignment, you will write a program to calculate the price of a meal.

### Instructions

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

#### Hint from Instructor:

As you will see in the requirements list below, this is as far as you need to get for the milestone requirements of Lesson 03, but you should try to get as far as you can during Lesson 03 to make it even easier for yourself in the next lesson, especially if you run into trouble.

Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

Compute and display the total price of the meal by adding the subtotal and the sales tax.

Finally:

Ask the user for the the payment amount (floating point)

Compute and display the change.

A sample run of the program might look as follows:

```
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
```

Another example, in which the user typed different values, might look like this:

```
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
```

### Showing Creativity and Exceeding Requirements

For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage, or anything else you can think of. Play around with different ideas and see what you can learn!

### Milestone Requirements

At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.

Ask the user for the number of adults and children and store these values properly into variables as integers.

Ask the user for the sales tax rate and store the value properly as a floating point number.

Compute and display the subtotal (don't worry about rounding to two decimals at this point).

### Final requirements

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

## numeric_data_types.py

### Overview

Practice converting user input to numeric data types and perform calculations.

### Assignment

For this assignment, you'll get to practice several different examples, but they should all be part of the same program.

Hint from Instructor:
After completing part of the assignment, if you want to keep the code there, but not have it run each time, you can put a # character at the front of the line to "comment it out" or temporarily turn it into a comment. Then, if you want the code to run again, you remove the # character and it is code again.

Write a program that does the following:

Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

Here is an example of the tasks when run:

```
How old are you? 25
On your next birthday, you will be 26

How many egg cartons do you have? 3
You have 36 eggs

How many cookies do you have? 18
How many people are there? 8
Each person may have 2.25 cookies
```

### Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

Run through the entire program using the inputs shown in the example above. Make sure your output matches the output shown above.

For the first question, regarding ages, try entering the ages 18 and 59 (one at a time), and ensure that the program correctly outputs the numbers 19 and 60 for the next birthdays.

For the second question, regarding eggs, try entering a 5 and 0 (one at a time), and ensure that the program outputs 60 and 0 eggs.

For the third question, regarding cookies, trying entering two more sets of values (one at a time) and make sure the division works correctly. Try one set of values that results in an even number (no decimal part) and one that results in a decimal and make sure they both work correctly.

Double check that the output matches the example output exactly, including:

The numeric values should appear in the middle of the other words, not on a separate line.

The number of spaces before and after the numbers should match the example output.

There should be a blank line before each section.
