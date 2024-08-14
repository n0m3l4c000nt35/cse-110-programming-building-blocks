## adventure_game.py

### Overview

In a text-based adventure game, the user is presented a scenario with different options. Depending on the option they choose, they have different consequences, which in turn present different choices for the next action.

Consider the following example:

You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?

The user can then type "match" or "flashlight".

If the user types "match" they may see a response such as:

You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?

Whereas, if the user typed "flashlight" in response to the original question, they may see a response such as:

You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?

Your choice at each step of the game determines what you see next and the options you have available at that point.

### Instructions

Create your own text-based adventure game with at least three levels of choices. It's up to you to determine the scenarios, the choices, and the consequences.

Keep in mind the following guidelines and requirements:

You need to have at least three levels of scenarios with possible choices.

At least one of your scenarios must have more than two possible choices.

In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.

When checking the users responses, you should match on the keyword, regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

Choices should only work for the correct question.

In other words, if one scenario resulted in choices of Run/Hide, but another resulted in choices Follow/Look, you should not be able to respond with "Follow" to the question that asked for Run/Hide.

A good way to accomplish this is to have a series of nested if statements. (That is, the print and then the next if statement will be within the body/block of the first if statement.)

For each question, you should provide an "else" clause to handle the case that the user tries to type something other than the possible choices. It is up to you how to handle this case.

Showing Creativity and Exceeding Requirements
Obviously, you'll show creativity by customizing the prompts and choices. To achieve the grade category of "Shows creativity and exceeds requirements" for this one, you need to add something additional to the framework of the game. For example, you might add even more levels or you might have more choices at each level. You might add hidden choices or trick questions. Have fun with this and see what you can do!

If you've already learned other programming concepts (for example, loops, lists, etc.) you are welcome to use those concepts here as a way to make show creativity and exceed requirements.

## grade_calculator.py

### Overview

Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60

### Assignment

Start by completing the core requirements, then when that part is complete, if you have time, see if you can complete some of the stretch challenges as well.

Please work through the requirements in order rather than jumping ahead to more complicated steps, to ensure that everyone is following the concepts.

### CORE REQUIREMENTS

Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.

Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.

### STRETCH CHALLENGE

Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. Then, display both the grade letter and the sign in one print statement.

At this point, don't worry about the exceptional cases of A+, F+, or F-.

Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.

## practicing_if_statements.py

### Overview

Practice the mechanics of if statements.

### Assignment

#### COMPARING NUMBERS

Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

- If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

- If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

- If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

#### COMPARING STRINGS

Have the program ask the user for their favorite animal. Then write an if statement as follows:

Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

Here is an example of the program when it runs:

```
What is the first number? 4
What is the second number? 3
The first number is greater
The numbers are not equal
The second number is not greater

What is your favorite animal? giraffe
That one is not my favorite.
```

Another example:

```
What is the first number? 1009
What is the second number? 5250
The first number is not greater
The numbers are not equal
The second number is greater

What is your favorite animal? bear
That's my favorite animal too!
```

And finally, note that in this example, the animal matches, even though the case is different:

```
What is the first number? 42
What is the second number? 42
The first number is not greater
The numbers are equal
The second number is not greater

What is your favorite animal? BEAR
That's my favorite animal too!
```

### Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

Test it with two numbers that are equal. Verify that all three values that are printed are correct.

Test the second part of your program with an animal that is different. Verify that the correct message is shown.

Test it with an animal that is the same. Verify that the correct message is shown.

Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.
