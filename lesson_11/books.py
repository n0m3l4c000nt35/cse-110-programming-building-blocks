"""
Overview
Practice Opening Files

Assignment
For this assignment, you'll download the file books.txt that contains the names of the books in the Book of Mormon, and save it to your computer.

Once you have the file saved to your computer, in VS Code, open the folder that contains it and create a new Python script.

Have your program open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

The following shows the expected output:


1 Nephi
2 Nephi
Jacob
Enos
Jarom
Omni
Words of Mormon
Mosiah
Alma
Helaman
3 Nephi
4 Nephi
Mormon
Ether
Moroni

Testing Procedure
For this program, there isn't any user input, so you don't need to try different values. Instead, simply verify that the following work as described

The books.txt file is downloaded and saved to your computer.

Your program can open the file.

Your program reads a line from the file and displays it to the screen.

Your program iterates through each line in the file and displays them to the screen.

Your program strips off the "\n" characters at the end of each line before displaying them, so it doesn't produce a blank line in between each displayed line.
"""

with open("books.txt", "r") as file:
    for line in file:
        book_name = line.strip()
        print(book_name)
