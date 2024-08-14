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