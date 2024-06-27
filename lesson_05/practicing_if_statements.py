"""
Overview
Practice the mechanics of if statements.

Assignment
COMPARING NUMBERS
Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

COMPARING STRINGS
Have the program ask the user for their favorite animal. Then write an if statement as follows:

Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

Here is an example of the program when it runs:


What is the first number? 4
What is the second number? 3
The first number is greater
The numbers are not equal
The second number is not greater

What is your favorite animal? giraffe
That one is not my favorite.
Another example:


What is the first number? 1009
What is the second number? 5250
The first number is not greater
The numbers are not equal
The second number is greater

What is your favorite animal? bear
That's my favorite animal too!
And finally, note that in this example, the animal matches, even though the case is different:


What is the first number? 42
What is the second number? 42
The first number is not greater
The numbers are equal
The second number is not greater

What is your favorite animal? BEAR
That's my favorite animal too!

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

Test it with two numbers that are equal. Verify that all three values that are printed are correct.

Test the second part of your program with an animal that is different. Verify that the correct message is shown.

Test it with an animal that is the same. Verify that the correct message is shown.

Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.
"""

first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

favorite_animal = input("What is your favorite animal? ").lower()

my_favorite_animal = "dog"

if favorite_animal == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
