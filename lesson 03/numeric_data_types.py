"""
Overview
Practice converting user input to numeric data types and perform calculations.

Assignment
For this assignment, you'll get to practice several different examples, but they should all be part of the same program.

Hint from Instructor:
After completing part of the assignment, if you want to keep the code there, but not have it run each time, you can put a # character at the front of the line to "comment it out" or temporarily turn it into a comment. Then, if you want the code to run again, you remove the # character and it is code again.

Write a program that does the following:

Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

Here is an example of the tasks when run:


How old are you? 25
On your next birthday, you will be 26

How many egg cartons do you have? 3
You have 36 eggs

How many cookies do you have? 18
How many people are there? 8
Each person may have 2.25 cookies

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Run through the entire program using the inputs shown in the example above. Make sure your output matches the output shown above.

For the first question, regarding ages, try entering the ages 18 and 59 (one at a time), and ensure that the program correctly outputs the numbers 19 and 60 for the next birthdays.

For the second question, regarding eggs, try entering a 5 and 0 (one at a time), and ensure that the program outputs 60 and 0 eggs.

For the third question, regarding cookies, trying entering two more sets of values (one at a time) and make sure the division works correctly. Try one set of values that results in an even number (no decimal part) and one that results in a decimal and make sure they both work correctly.

Double check that the output matches the example output exactly, including:

The numeric values should appear in the middle of the other words, not on a separate line.

The number of spaces before and after the numbers should match the example output.

There should be a blank line before each section.
"""

age = int(input("How old are you? "))
next_age = age + 1
print(f"On your next birthday, you will be {next_age}\n")

egg_cartons = int(input("How many egg cartons do you have? "))
total_eggs = egg_cartons * 12
print(f"You have {total_eggs} eggs\n")

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = cookies / people
print(f"Each person may have {cookies_per_person} cookies")