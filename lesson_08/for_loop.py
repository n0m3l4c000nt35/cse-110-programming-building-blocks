"""
Overview
Demonstrate your understand of for loops.

Assignment
Write a Python Program that does each of the following:

Given the following list of items (copy and paste this line into your program):


colors = ["red", "blue", "green", "yellow"]
Use a for loop to iterate through this list one by one and display each item on its own line as follows:


red
blue
green
yellow
Use a for loop to display the numbers 1–8, one number on each line as follows:


1
2
3
4
5
6
7
8
Use a for loop to display the even numbers (hint: count by two) 2–20, one number on each line as follows:


2
4
6
8
10
12
14
16
18
20

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Verify that the colors display as desired.

Verify that your output for part 2 does not include 0.

Verify that your output for part 2 does not include 9.

Verify that your output for part 3 does not include any odd numbers.

Verify that your output for part 3 starts at 2 and ends at 20.
"""

colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)

print()

for number in range(1, 9):
    print(number)

print()

for even_number in range(2, 21, 2):
    print(even_number)