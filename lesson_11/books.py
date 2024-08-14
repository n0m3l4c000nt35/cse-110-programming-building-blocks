with open("books.txt", "r") as file:
    for line in file:
        book_name = line.strip()
        print(book_name)
