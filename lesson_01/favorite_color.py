"""
Overview
For this assignment you will write a program that uses both input (obtaining data from the user via the keyboard) and output (displaying data to the user on the screen).

Instructions
Write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.

In the following example, the user types in "Blue" for their favorite color:


Please type your favorite color: Blue
Your favorite color is
Blue
Please note that the underline in this example for the word "Blue" is signifying that the user typed that in. You do not need to produce any underlines in your program.

In this example, the user types "Hot Pink" for their favorite color:


Please type your favorite color: Hot Pink
Your favorite color is
Hot Pink
Notice that the program displays back the color that the user entered, so it is different each time, depending on the color that was typed.

To make this program work, you will need to get input from the user and then save the data they provide into a variable. Then, at the appropriate time you print (i.e. display) the data stored in that variable.

Showing Creativity and Exceeding Requirements
As stated in the course syllabus. For each of the prove assignments this semester, you'll be provided with the core requirements, or minimum standard expectations, for the assignment. If you complete those requirements, you are eligible for a 93% on the assignment. However, to be eligible for a 100% on the assignment, you will need to do something to show creativity and exceed these core requirements.

For this assignment, here are some ideas of how you might show creativity in addition to the core requirements:

Ask some additional questions, store those answers in variables, and display them.

Change the formatting, such as putting the color on the same line as the other words, and adding punctuation around it (e.g., quotes around the color, and/or an exclamation point at the end).

Change the wording so that the program gives the user a more interesting message than simply saying "Your favorite color is."

Anything else you can think of!
"""

name = input("Please type your name: ")

favorite_color = input("Please type your favorite color: ")

print(f"Hello, {name}! Your favorite color is \"{favorite_color}\". That's a beautiful choice!")

favorite_food = input("Please type your favorite food: ")
favorite_animal = input("Please type your favorite animal: ")

print(f"Nice to meet you, {name}. It's cool that your favorite color is {favorite_color}, your favorite food is {favorite_food}, and your favorite animal is {favorite_animal}. Have a great day!")