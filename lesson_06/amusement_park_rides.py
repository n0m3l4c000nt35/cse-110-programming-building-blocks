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