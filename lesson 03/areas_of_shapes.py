"""
Overview
Python can be used to calculate values for data analysis and complex mathematical and scientific problems. In this activity, you will practice using variables and expressions for straight-forward math calculations. The purpose of the assignment is to help you become more comfortable using variables to accomplish a problem, not to focus on the actual math at hand.

Assignment
Start by completing the core requirements, then when that part is complete, if you have time, see if you can complete some of the stretch challenges as well.

CORE REQUIREMENTS
Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

An example run of the program might look something like the following:


What is the length of a side of the square? 5
The area of the square is: 25.0
What is the length of rectangle? 6
What is the width of the rectangle? 7
The area of the rectangle is: 42.0
What is the radius of the circle? 5
The area of the circle is: 78.5
Another run could be the following:


What is the length of a side of the square? 3.5
The area of the square is: 12.25
What is the length of rectangle? 6
What is the width of the rectangle? 7.5
The area of the rectangle is: 45.0
What is the radius of the circle? 8.2
The area of the circle is: 211.1336
STRETCH CHALLENGE
Once you have finished the core requirements, you are welcome to move on to the stretch challenges. These can be more difficult and may require finding solutions that weren't directly covered in the reading. These aren't specifically required for the assignment, but are a great chance to dive deeper into the concepts of the lesson.

The stretch challenges for this activity are:

Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module. Hint, you might try searching on the internet for something like, "python how to get the value of pi."

Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.
"""

import math

side_square = float(input("What is the length of a side of the square? "))
area_square = side_square ** 2
print(f"The area of the square is: {area_square}")

length_rectangle = float(input("What is the length of the rectangle? "))
width_rectangle = float(input("What is the width of the rectangle? "))
area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle is: {area_rectangle}")

radius_circle = float(input("What is the radius of the circle? "))
area_circle = math.pi * (radius_circle ** 2)
print(f"The area of the circle is: {area_circle}")

length_value = float(input("\nEnter a length value: "))

area_square_stretch = length_value ** 2
area_circle_stretch = math.pi * (length_value ** 2)
volume_cube = length_value ** 3
volume_sphere = (4 / 3) * math.pi * (length_value ** 3)

print(f"\nFor the length value {length_value}:")
print(f"Area of the square: {area_square_stretch}")
print(f"Area of the circle: {area_circle_stretch}")
print(f"Volume of the cube: {volume_cube}")
print(f"Volume of the sphere: {volume_sphere}")

side_square_cm = float(input("\nWhat is the length of a side of the square (in cm)? "))
area_square_cm = side_square_cm ** 2
area_square_m2 = area_square_cm / 10000
print(f"The area of the square is: {area_square_cm} square cm ({area_square_m2} square meters)")

length_rectangle_cm = float(input("What is the length of the rectangle (in cm)? "))
width_rectangle_cm = float(input("What is the width of the rectangle (in cm)? "))
area_rectangle_cm = length_rectangle_cm * width_rectangle_cm
area_rectangle_m2 = area_rectangle_cm / 10000
print(f"The area of the rectangle is: {area_rectangle_cm} square cm ({area_rectangle_m2} square meters)")

radius_circle_cm = float(input("What is the radius of the circle (in cm)? "))
area_circle_cm = math.pi * (radius_circle_cm ** 2)
area_circle_m2 = area_circle_cm / 10000
print(f"The area of the circle is: {area_circle_cm} square cm ({area_circle_m2} square meters)")
