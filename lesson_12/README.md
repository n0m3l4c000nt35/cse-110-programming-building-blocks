1. [find_youngest_person.py](./find_youngest_person.py)
2. [finding_items_in_a_file.py](./finding_items_in_a_file.py)

## [find_youngest_person.py](./find_youngest_person.py)

### Overview

This checkpoint will help you practice finding things in a list.

### Assignment

To simplify your program to focus on the task at hand, instead of reading from a file, please copy and paste the following list of people and their ages into your program:

```python
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
```

Write a program to find the youngest person in the list.

Consider following these steps to build up to the finished program:

Iterate through the list and display each string to the screen.

Split the string into a name and age and print them to the screen.

Find the age that is the youngest.

Keep track of the name of the person that is the youngest.

### Testing Procedure

Because there is no user input, you don't need to test the program with different values. Instead, make sure that that following components are in place:

- The list of people is included in the program.
- The program can iterate through each string in the list.
- The program can split the string into the appropriate pieces.
- The youngest age is identified.
- The name of the youngest person is identified.

## [finding_items_in_a_file.py](./finding_items_in_a_file.py)

### Overview

In this activity, you will practice finding items in a file. You will be supplied with a file that contains the books in the Standard Works of the Scriptures, and for each book the number of chapters. You will need to open this file, parse through it, and discover books that have certain properties.

### Assignment

Download the file: books_and_chapters.txt and save it to a folder for your project. Then, open that folder in VS Code and create a Python script to read through the file line by line.

Take a minute to look at the file, understand the type of data it contains, and what character you'll need to split on to separate it into the proper pieces.

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format:

Scripture: Old Testament, Book: Genesis, Chapters: 50

Find the largest number of chapters in the scriptures.

Find the book that has the largest number of chapters in the scriptures.

### STRETCH CHALLENGE

Change your program so that it only prints the books in the Book of Mormon.

Find the book in the Book of Mormon that has the largest number of chapters.

At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). Then, find the book in that volume of scripture that has the largest number of chapters.
