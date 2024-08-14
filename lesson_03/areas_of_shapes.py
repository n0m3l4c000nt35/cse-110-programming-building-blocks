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
