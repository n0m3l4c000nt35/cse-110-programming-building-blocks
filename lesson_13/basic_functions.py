def display_regular(message):
    """Displays the message exactly as received."""
    print(message)

def display_uppercase(message):
    """Converts the message to upper case and displays it."""
    print(message.upper())

def display_lowercase(message):
    """Converts the message to lower case and displays it."""
    print(message.lower())

def main():
    user_message = input("What is your message? ")

    display_regular(user_message)
    display_uppercase(user_message)
    display_lowercase(user_message)

if __name__ == "__main__":
    main()