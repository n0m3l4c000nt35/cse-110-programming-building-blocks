1. [formatting_strings.py](./formatting_strings.py)
2. [id_badge_generator.py](./id_badge_generator.py)
3. [mad_libs.py](./mad_libs.py)

## [formatting_strings.py](./formatting_strings.py)

### Overview

An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond." For this assignment you will write a program that asks for your name and repeats it back in this way.

### Assignment

Prompt the user for their first name. Then, prompt them for their last name. Display the text back all on one line saying, "Your name is last-name, first-name, last-name" as shown:

```
What is your first name? Scott
What is your last name? Burton

Your name is Burton, Scott Burton.

What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.
```

Make sure to be precise! You should have the spacing, comma, and period appear exactly as shown in the examples.

## [id_badge_generator.py](./id_badge_generator.py)

### Overview

An ID badge, such as a drivers license or student ID, contains personal details that are formatted in a very specific way.

For this activity you will write a program that will create a properly formatted ID badge.

### Assignment

Write a program to prompt the user for the following:

- First name
- Last name
- Email Address
- Phone Number
- Job Title
- ID Number

Then you should display the information back in this format:

Note that the square brackets [] indicate a value coming from the user and should not be displayed.

```
---
[LAST NAME], [first name]
[Job title]
ID: [id number]
[email address]
[phone number]
---
```

In addition to the spacing and punctuation shown above, you must implement the following requirements:

The last name should be converted from whatever the user types to be displayed in ALL CAPS.

The job title should be displayed so that the first letter is capitalized.

The email address should be displayed in all lowercase.

An example of the program running is shown:

```
Please enter the following information:
First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

---
The ID Card is:
DOE, Jane
Chief Software Architect
ID: 83-23821
janedoe@email.com
(208) 555-1234
---
```

### CORE REQUIREMENTS

Each team activity will contain three core requirements. These are items that you are expected to be able to complete during the one hour team meeting if you have come prepared.

You should work through the assignment in this order:

Prompt for all of the necessary values and store them in variables. Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.

Arrange the display so that the spacing and punctuation exactly match the example shown.

Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and the email display in all lowercase.

### STRETCH CHALLENGE

Most team activities will also contain stretch challenges, which are not specifically required by the assignment, but are a great way to dive deeper into the material. They can be more difficult and may require you to find solutions that weren't directly covered in the preparation material.

The stretch challenges for this activity are:

Add hair color and eye color and put them both on the same line in the display.

Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training. Put these both on the same line in the display.

For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses.

To complete this one, you may need to search the internet for something like, "python spacing format" or something similar to see if you get any ideas.

At the end of the stretch challenge, your output should look something like the following:

```
---
The ID Card is:

DOE, Jane
Chief Software Architect
ID: 83-23821
janedoe@email.com
(208) 555-1234
Hair: Brown Eyes: Blue
Month: September Training: Yes
---
```

## [mad_libs.py](./mad_libs.py)

### Overview

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

```
When it comes to ducks, you would never want to jump, especially if you encountered a cold taco.
```

### Instructions

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

### SAMPLE OUTPUT

Here is an example of how your program might work:

```
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
```

Another example, where the user typed different values might look like this:

```
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
```

### Showing Creativity and Exceeding Requirements

For this assignment, show creativity and exceed the core requirements by adding more to the story, including several more words that will be filled in.

If you have previous experience with topics that we will see later in the semester, consider a sentence that has an "a" or "an" in front of your word, and let the program fill in the right one.

Anything else you can think of is also fair game. Remember, the goal here is to experiment with different ideas and to have fun.
