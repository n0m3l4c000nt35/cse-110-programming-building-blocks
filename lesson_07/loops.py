"""
Overview
Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

Assignment
Write a Python Program that does each of the following:

Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:


Please type a positive number: -3
Sorry, that is a negative number. Please try again.
Please type a positive number: -8
Sorry, that is a negative number. Please try again.
Please type a positive number: -1
Sorry, that is a negative number. Please try again.
Please type a positive number: 12
The number is: 12

Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:

May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? yes
Thank you.

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

For the positive number program, enter several negative numbers, then a positive one.

Try entering a positive number first, and ensure that it doesn't ask again.

Try entering 0 and ensure that it correctly treats it as a positive number.

For the piece of candy program, test your last loop by entering different amounts of no's before finally saying yes.

Try saying "yes" the very first time, and ensure that it works as expected.
"""

def positive_number_input():
    while True:
        number = int(input("Please type a positive number: "))
        if number >= 0:
            print(f"The number is: {number}")
            break
        else:
            print("Sorry, that is a negative number. Please try again.")


def candy_request_simulation():
    while True:
        response = input("May I have a piece of candy? ").strip().lower()
        if response == "yes":
            print("Thank you.")
            break
        else:
            print("No? Please ask again.")


positive_number_input()
candy_request_simulation()