"""
Overview
In this activity, you will practice finding items in a file. You will be supplied with a file that contains the books in the Standard Works of the Scriptures, and for each book the number of chapters. You will need to open this file, parse through it, and discover books that have certain properties.

Assignment
Download the file: books_and_chapters.txt and save it to a folder for your project. Then, open that folder in VS Code and create a Python script to read through the file line by line.

Take a minute to look at the file, understand the type of data it contains, and what character you'll need to split on to separate it into the proper pieces.

CORE REQUIREMENTS
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format:

Scripture: Old Testament, Book: Genesis, Chapters: 50

Find the largest number of chapters in the scriptures.

Find the book that has the largest number of chapters in the scriptures.

STRETCH CHALLENGE
Change your program so that it only prints the books in the Book of Mormon.

Find the book in the Book of Mormon that has the largest number of chapters.

At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). Then, find the book in that volume of scripture that has the largest number of chapters.
"""

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("The file was not found.")
        return []

def parse_line(line):
    parts = line.strip().split(':')
    if len(parts) == 3:
        book, chapters, scripture = parts
        return book, int(chapters), scripture
    return None, None, None

def display_books(lines):
    for line in lines:
        book, chapters, scripture = parse_line(line)
        if book and chapters and scripture:
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

def find_largest_chapters(lines):
    max_chapters = 0
    max_book = ""
    max_scripture = ""
    for line in lines:
        book, chapters, scripture = parse_line(line)
        if chapters > max_chapters:
            max_chapters = chapters
            max_book = book
            max_scripture = scripture
    return max_book, max_chapters, max_scripture

def display_books_in_volume(lines, volume):
    for line in lines:
        book, chapters, scripture = parse_line(line)
        if scripture == volume:
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

def find_largest_chapters_in_volume(lines, volume):
    max_chapters = 0
    max_book = ""
    for line in lines:
        book, chapters, scripture = parse_line(line)
        if scripture.lower() == volume and chapters > max_chapters:
            max_chapters = chapters
            max_book = book
    return max_book, max_chapters

def main():
    file_path = 'books_and_chapters.txt'
    lines = read_file(file_path)

    display_books(lines)

    max_book, max_chapters, max_scripture = find_largest_chapters(lines)
    print(f"\nThe book with the largest number of chapters is {max_book} from {max_scripture} with {max_chapters} chapters.")

    volume = input("Which volume of scriptures would you like to learn about? ").lower()
    
    display_books_in_volume(lines, volume)

    max_book, max_chapters = find_largest_chapters_in_volume(lines, volume)
    print(f"\nThe book in {volume} with the largest number of chapters is {max_book} with {max_chapters} chapters.")

if __name__ == "__main__":
    main()