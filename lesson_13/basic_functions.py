"""
Overview
This checkpoint is designed to help you practice writing basic functions.

Assignment
Write three functions:

display_regular—Receives a string and prints it out, exactly as received.

display_uppercase—Receives a string, converts it to upper case, and then prints it out.

display_lowercase—Receives a string, converts it to lower case, and then prints it out.

In your program below the functions, ask the user to type a message. Then, pass that message to each of the three functions, so it it displays it each way, as shown:


What is your message? Brother Burton
Brother Burton
BROTHER BURTON
brother burton
Another example is:


What is your message? The only thing we have to fear is FEAR itself!
The only thing we have to fear is FEAR itself!
THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF!
the only thing we have to fear is fear itself!

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Try your program with each of the following conditions and ensure that it works as expected.

A single word

A phrase with multiple words

A word in ALL CAPS

A phrase where each word starts with a capital

An empty string
"""

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