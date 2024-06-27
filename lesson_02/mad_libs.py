"""
Overview
Mad Libs are a type of funny story, where a person is asked for words without knowing their context. The words are then placed into a story in a pre-determined format, often resulting in funny statements.

For example, consider prompts for:

Plural noun

Verb

Adjective

Noun

And a story, such as:

When it comes to [plural-noun], you would never want to [verb], especially if you encountered a [adjective] [noun].

A person, may respond to the prompts with the following:

Plural noun: ducks

Verb: jump

Adjective: cold

Noun: taco

Then the story would read:

When it comes to ducks, you would never want to jump, especially if you encountered a cold taco.

Instructions
For this assignment, you will implement a program that asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places.

The program should begin by asking the user for each of the words. It should then, fill those words into the appropriate places in the story.

To begin, please use the following story:

The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.

Make sure to match the punctuation and spacing of the original story exactly (for example, you should not put your words on their own line, they should fit naturally into the story).

Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.

SAMPLE OUTPUT
Here is an example of how your program might work:


Please enter the following:

adjective: happy
animal: zebra
verb: sneeze
exclamation: hooray
verb: read
verb: drive

Your story is:

The other day, I was really in trouble. It all started when I saw a very
happy zebra sneeze down the hallway. "Hooray!" I yelled. But all
I could think to do was to read over and over. Miraculously,
that caused it to stop, but not before it tried to drive
right in front of my family. 
Another example, where the user typed different values might look like this:


Please enter the following:

adjective: tired
animal: snail
verb: yell
exclamation: oh no
verb: sing
verb: skip

Your story is:

The other day, I was really in trouble. It all started when I saw a very
tired snail yell down the hallway. "Oh no!" I yelled. But all
I could think to do was to sing over and over. Miraculously,
that caused it to stop, but not before it tried to skip
right in front of my family. 
Showing Creativity and Exceeding Requirements
For this assignment, show creativity and exceed the core requirements by adding more to the story, including several more words that will be filled in.

If you have previous experience with topics that we will see later in the semester, consider a sentence that has an "a" or "an" in front of your word, and let the program fill in the right one.

Anything else you can think of is also fair game. Remember, the goal here is to experiment with different ideas and to have fun.
"""

print("Please enter the following:")

adjective1 = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")

noun1 = input("noun: ")
place = input("place: ")
adjective2 = input("adjective: ")
plural_noun = input("plural noun: ")

print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective1} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print(f"right in front of my family. Just then, a {noun1} appeared out of nowhere,")
print(f"and we all had to run to {place} to escape the {adjective2} {plural_noun}.")
print(f"It was a day to remember!")