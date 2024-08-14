## guess_my_number_game.py

### Overview

In the Guess My Number game the computer picks a magic number, and then the user tries to guess it. After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

This assignment is a little tricky, because it brings together many of the concepts you've learned in this course including loops and if statements.

### Assignment

#### HAVING THE COMPUTER PICK A RANDOM NUMBER

There is a random number library included with Python that contains a number of different functions to generate random numbers, depending on if you want integers, floating point numbers, and from different statistical distributions.

The only function you will need from this library is called randint. To use it, you give it two numbers and it returns back a random number in that range. In order to use this function you need to import it from the random library.

The following code shows how to import the function and use it to get a random number from 1 to 10.

```python
import random

number = random.randint(1, 10)
print(number)
```

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. You will build a simple working solution first, then we will have you modify that solution to create the final version of this assignment. Please do not skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Start by asking the user for the magic number. We are letting the user pick the magic number for now, but in future steps we will change this to have the computer generate a random number for us. Pretend that you do not know what this number is when playing the game.

Ask the user to guess the magic number; again pretend you don't know it.

Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it correctly.

At this point, you won't have any loops in your code. It will run once and complete no matter what number was entered.

The following shows the expected output at this point:

```
What is the magic number? 6
What is your guess? 4
Higher

What is the magic number? 6
What is your guess? 7
Lower

What is the magic number? 6
What is your guess? 6
You guessed it!
```

Now add a loop that keeps looping as long as the guess does not match the magic number.

At this point, the user should be able to keep playing until they get the correct answer.

The following shows the expected output at this point. Keep in mind that we are still pretending that we do not know what the magic number is, even though we are the ones picking it:

```
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
```

Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

Play the game and make sure it works!

### STRETCH CHALLENGE

Keep track of how many guesses the user has made and inform them of it at the end of the game.

After the game is over, ask the user if they want to play again. Then, loop back and play the whole game again and continue this loop as long as they keep saying "yes".

## loops.py

### Overview

Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

### Assignment

Write a Python Program that does each of the following:

Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:

```
Please type a positive number: -3
Sorry, that is a negative number. Please try again.
Please type a positive number: -8
Sorry, that is a negative number. Please try again.
Please type a positive number: -1
Sorry, that is a negative number. Please try again.
Please type a positive number: 12
The number is: 12
```

Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:

May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? yes
Thank you.

### Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

For the positive number program, enter several negative numbers, then a positive one.

Try entering a positive number first, and ensure that it doesn't ask again.

Try entering 0 and ensure that it correctly treats it as a positive number.

For the piece of candy program, test your last loop by entering different amounts of no's before finally saying yes.

Try saying "yes" the very first time, and ensure that it works as expected.

## word_guessing_game.py

### Overview

Many games and puzzles require iteration where a person (or a computer) repeats the same steps for each piece in the game or each spot in a puzzle. For this assignment, you will create an interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.

Wordle is a web-based word game that became popular online in the early part of 2022. (You can learn more about it from the Wordle Wikipedia page.)

For this assignment, you'll create a puzzle game that follows a similar pattern.

### Project Description

The program contains a hidden secret word stored in a variable. This word can have any number of letters in it. When the program runs, the user is shown underscores ( \_ ) for each letter of the word.

The user then enters a guess. If the guess is correct, the user wins and the game is over.

If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

The game continues prompting the user for new guesses and showing them hints until they guess the word correctly. When the game is over, the program displays the number of guesses that were made.

The guess must be the same number of letters as the secret word. If the guess has a different numbers of letters, the user is given a message explaining this, and no hint is provided.

The hint is a rendering of the letters in the guess according to the following guidelines:

An underscore \_ indicates that the letter was not present in the secret word.

A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)

For example, if the secret word were: mosiah, then the program would initially display:

Your hint is: \_ \_ \_ \_ \_ \_
If the user's guess were: temple, they would learn that the m in temple is the only letter in the secret word, but it is in the wrong spot, so it would be displayed in lowercase as shown:

Your hint is: \_ _ m _ \_ \_
But if the user instead guessed: moroni, they would receive the following as a hint:

Your hint is: M O _ o _ i
Notice that in the hint above, the M and the first O from moroni are capitalized, because those letters are also the first two letters of mosiah.

The i and the second o from moroni are displayed, because they are present in the secret word, but they are shown in lowercase, because the the letters in the secret word at that location are different.

The r and the n from moroni are not displayed, but instead an underscore is shown in each place, because these letters are not present in the secret word in any location.

A sample of the complete program might look as follows:

```
Welcome to the word guessing game!

Your hint is: _ _ _ _ _ _
What is your guess? temple
Your hint is: _ _ m _ _ _
What is your guess? moroni
Your hint is: M O _ o _ i
What is your guess? hhhhhh
Your hint is: h h h h h H
What is your guess? mosiah
Congratulations! You guessed it!
It took you 4 guesses.
```

Because capital letters have meaning in our hints, the secret word should be all lower case. Similarly, when the user enters their guess, you should convert it to lowercase prior to checking for matches.

If the guess has a different number of letters than the secret word, it still counts as a guess, but the user does not receive a hint. This is shown in the following example:

```
Welcome to the word guessing game!

Your hint is: _ _ _ _ _ _
What is your guess? nephi
Sorry, the guess must have the same number of letters as the secret word.

What is your guess? a
Sorry, the guess must have the same number of letters as the secret word.

What is your guess? helaman
Sorry, the guess must have the same number of letters as the secret word.

What is your guess? abcdefghijklmnopqrstuvwxyz
Sorry, the guess must have the same number of letters as the secret word.

What is your guess? temple
Your hint is: _ _ m _ _ _
What is your guess? mosiah
Congratulations! You guessed it!
It took you 6 guesses.
```

### Showing Creativity and Exceeding Requirements

Once you have the basic rules of the game in place, consider adding something extra to the hints, other rules or limitations to the number of guesses, or anything else you think would be fun.

If you want to look ahead at lists or files, you could start the game with a list of words, and select a random one for the secret word.
