"""
Overview
For this assignment, you'll work as a team to write a program for a fictitious amusement park ride.

THE SCENARIO: RIDER REQUIREMENTS
The local amusement park has just installed a new ride. Because of its speed and extreme twists and turns, it has very strict requirements for the riders, especially as it pertains to children or other shorter riders.

To help the ride attendants follow the rules, you've been asked to write an app to help them know if the riders are acceptable for the car.

The basic rules are as follows:

No one under 36 inches may ever ride, either by themselves or with another rider.

Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

If there are two riders and one of them is at least 18 years old, they may ride together.

Assignment
Implement the ride requirements defined above. Your program should prompt for the riders' ages and heights, and then display a message indicating whether they can ride or not.

CORE REQUIREMENTS
Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.

Handle the case of a single rider.

Finish implementing the basic rules.

An example run of the program may look as follows:


What is the age of the first rider? 12
What is the height of the first rider? 46
Is there a second rider (yes/no)? no
Sorry, you may not ride.
Another example may look as follows:


What is the age of the first rider? 82
What is the height of the first rider? 75
Is there a second rider (yes/no)? yes
What is the age of the second rider? 14
What is the height of the second rider? 35
Sorry, you may not ride.
And a final example:


What is the age of the first rider? 82
What is the height of the first rider? 75
Is there a second rider (yes/no)? yes
What is the age of the second rider? 14
What is the height of the second rider? 36
Welcome to the ride. Please be safe and have fun!

STRETCH CHALLENGE
In addition to the basic rules, the amusement park has added the following. Please implement each one for the stretch challenges:

If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

Whew! That's complicated! Now you see why they need an app.
"""

def get_integer_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                return value
            else:
                if min_val is not None and max_val is not None:
                    print(f"Please enter a number between {min_val} and {max_val}.")
                elif min_val is not None:
                    print(f"Please enter a number greater than or equal to {min_val}.")
                elif max_val is not None:
                    print(f"Please enter a number less than or equal to {max_val}.")
                else:
                    print("Invalid input range specified.")
        except ValueError:
            print("Please enter a valid integer.")

def check_ride_eligibility():
    print("Welcome to the Amusement Park Ride Eligibility Checker!")
    
    age1 = get_integer_input("What is the age of the first rider? ")
    height1 = get_integer_input("What is the height of the first rider (in inches)? ")

    second_rider = input("Is there a second rider (yes/no)? ").strip().lower() == "yes"

    if second_rider:
        age2 = get_integer_input("What is the age of the second rider? ")
        height2 = get_integer_input("What is the height of the second rider (in inches)? ")

        if age1 >= 18 or age2 >= 18:
            print("Welcome to the ride. Please be safe and have fun!")
        elif age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
            print("Welcome to the ride. Please be safe and have fun!")
        else:
            print("Sorry, you may not ride.")
    else:
        if age1 >= 18 and height1 >= 62:
            print("Welcome to the ride. Please be safe and have fun!")
        elif age1 >= 12 and height1 >= 36:
            print("Welcome to the ride. Please be safe and have fun!")
        else:
            print("Sorry, you may not ride.")

check_ride_eligibility()