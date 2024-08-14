first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

favorite_animal = input("What is your favorite animal? ").lower()

my_favorite_animal = "dog"

if favorite_animal == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
