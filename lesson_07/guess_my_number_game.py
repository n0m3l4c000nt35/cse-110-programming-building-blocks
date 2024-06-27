"""
Overview
In the Guess My Number game the computer picks a magic number, and then the user tries to guess it. After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

This assignment is a little tricky, because it brings together many of the concepts you've learned in this course including loops and if statements.

Assignment
HAVING THE COMPUTER PICK A RANDOM NUMBER
There is a random number library included with Python that contains a number of different functions to generate random numbers, depending on if you want integers, floating point numbers, and from different statistical distributions.

The only function you will need from this library is called randint. To use it, you give it two numbers and it returns back a random number in that range. In order to use this function you need to import it from the random library.

The following code shows how to import the function and use it to get a random number from 1 to 10.


import random

number = random.randint(1, 10)
print(number)


CORE REQUIREMENTS
Work through these core requirements step-by-step to complete the program. You will build a simple working solution first, then we will have you modify that solution to create the final version of this assignment. Please do not skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Start by asking the user for the magic number. We are letting the user pick the magic number for now, but in future steps we will change this to have the computer generate a random number for us. Pretend that you do not know what this number is when playing the game.

Ask the user to guess the magic number; again pretend you don't know it.

Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it correctly.

At this point, you won't have any loops in your code. It will run once and complete no matter what number was entered.

The following shows the expected output at this point:


What is the magic number? 6
What is your guess? 4
Higher

What is the magic number? 6 
What is your guess? 7
Lower

What is the magic number? 6
What is your guess? 6
You guessed it!


Now add a loop that keeps looping as long as the guess does not match the magic number.

At this point, the user should be able to keep playing until they get the correct answer.

The following shows the expected output at this point. Keep in mind that we are still pretending that we do not know what the magic number is, even though we are the ones picking it:


What is the magic number? 18
What is your guess? 5
Higher
What is your guess? 6
Higher
What is your guess? 7
Higher
What is your guess? 20
Lower
What is your guess? 19
Lower
What is your guess? 18
You guessed it!


Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

Play the game and make sure it works!

STRETCH CHALLENGE
Keep track of how many guesses the user has made and inform them of it at the end of the game.

After the game is over, ask the user if they want to play again. Then, loop back and play the whole game again and continue this loop as long as they keep saying "yes".
"""

import random

def guess_my_number():
    print("Welcome to Guess My Number Game!")
    
    magic_number = random.randint(1, 100)
    
    guess_count = 0
    
    while True:
        guess = int(input("What is your guess? "))
        
        guess_count += 1
        
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            break
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == "yes":
        guess_my_number()
    else:
        print("Thank you for playing!")

guess_my_number()