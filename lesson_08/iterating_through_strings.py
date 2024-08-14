word = "Commitment"

for letter in word:
    if letter == 'm':
        print(letter.upper())
    else:
        print(letter.lower())

word = "Commitment"

for letter in word:
    if letter == 'm':
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

word = "Commitment"
favorite_letter = input("What is your favorite letter? ").lower()

for letter in word:
    if letter.lower() == favorite_letter:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

word = "Commitment"
favorite_letter = input("What is your favorite letter? ").lower()

for letter in word:
    if letter.lower() == favorite_letter:
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
n = int(input("Please enter a number: "))

for i, letter in enumerate(quote):
    if (i + 1) % n == 0:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

while True:
    n = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if (i + 1) % n == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()

    another = input("Would you like to enter another number? (yes/no) ").lower()
    if another != "yes":
        print("Goodbye")
        break