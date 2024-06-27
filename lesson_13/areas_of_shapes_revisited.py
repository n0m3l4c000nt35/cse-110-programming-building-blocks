"""
Overview
Earlier in the course, you completed a team activity to compute the areas of squares, rectangles, and circles. Please refer to 03 Teach: Team Activity for the details of that activity.

For this assignment, you are going to repeat the earlier calculations, but this time, you will make three functions, one to calculate each of the areas.

Assignment
Write functions to compute and return the areas of squares, rectangles, and circles. These functions should not display the values directly, but rather should return them, so they could be used in other parts of the program.

CORE REQUIREMENTS
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.

Below the function, write code to prompt the user for the side of a square and save it into a variable, then pass this variable to the function to compute the area. Finally, get the result back from the function and display it.

Repeat the previous step to write and test the functions compute_area_rectangle and compute_area_circle.

Write a loop to ask the user what kind of shape they have, then prompt for the length of a side, or sides, or radius, and then calls the appropriate function, and displays the result. The program should continue looping until the user enters "quit" for the shape.

STRETCH CHALLENGE
Recognize that you can compute the area of a square by passing the task along to a function that computes the areas of rectangles, by giving it the side of the square twice.

Change your program so that the compute_area_square function doesn't compute the area directly, but instead calls the compute_area_rectangle to do the work. It should pass the square side length to it (twice) and then return the value that the compute_area_rectangle function computes.

Write a new function called compute_area that accepts a first parameter of shape that can be either "square" or "circle" and then a value for the length of the side or the radius depending on the context. The function should then determine the correct function to use, based on the first parameter, call it, and return the value.

Change your program to use this function for the square and circle cases and verify that it works.

Add the ability for your new compute_area function to also compute the areas for rectangles. This means that you'll have to be able to accept calls like this: compute_area("circle", 5), this: compute_area("square", 10), and this compute_area("rectangle", 7, 8).

In order to make this work correctly, you'll need to make use of a default value for the last parameter.

Change your program to use this for all three calculations and verify that it works.
"""

import math

def compute_area_square(side):
    """Calculates the area of a square given the side length."""
    return side * side

def compute_area_rectangle(length, width):
    """Calculates the area of a rectangle given the length and width."""
    return length * width

def compute_area_circle(radius):
    """Calculates the area of a circle given the radius."""
    return math.pi * radius * radius

def compute_area_square(side):
    """Calculates the area of a square by calling the compute_area_rectangle function."""
    return compute_area_rectangle(side, side)

def compute_area(shape, dimension1, dimension2=None):
    """Calculates the area based on the specified shape."""
    if shape == "square":
        return compute_area_square(dimension1)
    elif shape == "rectangle":
        return compute_area_rectangle(dimension1, dimension2)
    elif shape == "circle":
        return compute_area_circle(dimension1)
    else:
        raise ValueError("Shape not recognized")

def main():
    while True:
        shape = input("What kind of shape do you have (square, rectangle, circle, quit)? ").lower()

        if shape == "quit":
            break
        elif shape == "square":
            side = float(input("Enter the side of the square: "))
            area = compute_area("square", side)
            print(f"The area of the square is: {area}")
        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = compute_area("rectangle", length, width)
            print(f"The area of the rectangle is: {area}")
        elif shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = compute_area("circle", radius)
            print(f"The area of the circle is: {area}")
        else:
            print("Invalid shape. Please try again.")

if __name__ == "__main__":
    main()