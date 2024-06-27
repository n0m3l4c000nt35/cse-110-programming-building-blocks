"""
Overview
When it's cold outside and the wind is blowing, it feels even colder!

(For those of you that have been to the BYU-Idaho campus in Rexburg during a Winter semester, you are very familiar with this concept.)

To try to quantify how cold it feels outside, instead of using temperature, a calculation for "wind chill" has been developed that takes into account both the temperature and the wind speed.

The U.S. National Weather Service defines the following formula to calculate wind chill in degrees Fahrenheit from a temperature in degrees Fahrenheit and wind speed in miles per hour:

Wind Chill Chart and Formula

(To find the formula, follow the above link and look for the formula at the bottom of the chart.)

Keep in mind that:

T is the temperature in degrees Fahrenheit

V is the wind speed in miles per hour

V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.

Assignment
Your assignment is to write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service chart does. To help users who are more familiar with Celsius, your program should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit before using the formula.

The following shows the expected output of this program:


What is the temperature? 8
Fahrenheit or Celsius (F/C)? F
At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
At temperature 8.0F, and wind speed 10 mph, the windchill is: -6.02F
At temperature 8.0F, and wind speed 15 mph, the windchill is: -9.15F
At temperature 8.0F, and wind speed 20 mph, the windchill is: -11.50F
At temperature 8.0F, and wind speed 25 mph, the windchill is: -13.40F
At temperature 8.0F, and wind speed 30 mph, the windchill is: -15.00F
At temperature 8.0F, and wind speed 35 mph, the windchill is: -16.39F
At temperature 8.0F, and wind speed 40 mph, the windchill is: -17.62F
At temperature 8.0F, and wind speed 45 mph, the windchill is: -18.73F
At temperature 8.0F, and wind speed 50 mph, the windchill is: -19.74F
At temperature 8.0F, and wind speed 55 mph, the windchill is: -20.67F
At temperature 8.0F, and wind speed 60 mph, the windchill is: -21.53F
Another example that uses Celsius is:


What is the temperature? -10
Fahrenheit or Celsius (F/C)? C
At temperature 14.0F, and wind speed 5 mph, the windchill is: 5.93F
At temperature 14.0F, and wind speed 10 mph, the windchill is: 1.42F
At temperature 14.0F, and wind speed 15 mph, the windchill is: -1.47F
At temperature 14.0F, and wind speed 20 mph, the windchill is: -3.63F
At temperature 14.0F, and wind speed 25 mph, the windchill is: -5.38F
At temperature 14.0F, and wind speed 30 mph, the windchill is: -6.85F
At temperature 14.0F, and wind speed 35 mph, the windchill is: -8.13F
At temperature 14.0F, and wind speed 40 mph, the windchill is: -9.27F
At temperature 14.0F, and wind speed 45 mph, the windchill is: -10.29F
At temperature 14.0F, and wind speed 50 mph, the windchill is: -11.22F
At temperature 14.0F, and wind speed 55 mph, the windchill is: -12.07F
At temperature 14.0F, and wind speed 60 mph, the windchill is: -12.87F
This assignment is designed to be smaller than previous assignments and is therefore not broken up into a milestone component and a final deliverable. Instead, you should complete the whole program for this lesson.

REQUIREMENTS
The following are the required components of this assignment:

Write a function to calculate and return the wind chill based on a given temperature and wind speed.

Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.

SHOWING CREATIVITY
Because this assignment is so clearly defined, it is more difficult to find a way to show creativity. Because of this, you are welcome to, but not required to add anything additional the way you did in previous assignments. Instead, if you meet the requirements above, you are eligible for 100% on the assignment.
"""

def calculate_wind_chill(temp_f, wind_speed):
    """Calculates the wind chill based on the given temperature in Fahrenheit and wind speed."""
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    """Converts a temperature from Celsius to Fahrenheit."""
    return temp_c * (9/5) + 32

def main():
    temperature = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if scale == 'C':
        temperature = celsius_to_fahrenheit(temperature)
        print(f"Temperature in Fahrenheit: {temperature:.2f}F")

    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()