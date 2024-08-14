def positive_number_input():
    while True:
        number = int(input("Please type a positive number: "))
        if number >= 0:
            print(f"The number is: {number}")
            break
        else:
            print("Sorry, that is a negative number. Please try again.")


def candy_request_simulation():
    while True:
        response = input("May I have a piece of candy? ").strip().lower()
        if response == "yes":
            print("Thank you.")
            break
        else:
            print("No? Please ask again.")


positive_number_input()
candy_request_simulation()