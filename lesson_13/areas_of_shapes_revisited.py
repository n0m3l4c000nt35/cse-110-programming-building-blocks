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