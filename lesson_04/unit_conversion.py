"""
Overview
Practice solving problems with variables and expressions, and displaying the results.

The Problem: Converting between different types of units
Temperature, like many other values, can be measured in different kinds of units. In this case, you might measure the value of degrees in Fahrenheit, Celsius, or Kelvin. Converting from one scale to another uses the same calculation over and over again for different input values.

Situations like this one are the perfect case for a program that can be coded to complete the steps of the calculation.

Assignment
Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

Here is an example of the program when it runs:


What is the temperature in Fahrenheit? 81
The temperature in Celsius is 27.2 degrees.
Another example is:


What is the temperature in Fahrenheit? 12
The temperature in Celsius is -11.1 degrees.

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Try the values in the examples on this page and ensure that your program generates the same results.

Verify that you are displaying the result to 1 decimal point of precision as shown.

Try converting 32 degrees Fahrenheit (freezing, which should be 0 degrees Celsius) and 212 degrees (boiling, which should be 100 degrees Celsius)

Try converting 0 and a negative number and make sure they come out as you would expect.

Verify that you have used good style, by checking the variable names you have used as well as the use of blank lines and whitespace around your operators.
"""

fahrenheit = float(input("What is the temperature in Fahrenheit? "))

celsius = (fahrenheit - 32) * (5 / 9)

print(f"The temperature in Celsius is {celsius:.1f} degrees.")