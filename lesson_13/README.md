1. [areas_of_shapes_revisited.py](./areas_of_shapes_revisited.py)
2. [basic_functions.py](./basic_functions.py)
3. [wind_chill_calculations.py](./wind_chill_calculations.py)

## [areas_of_shapes_revisited.py](./areas_of_shapes_revisited.py)

### Overview

Earlier in the course, you completed a team activity to compute the areas of squares, rectangles, and circles. Please refer to 03 Teach: Team Activity for the details of that activity.

For this assignment, you are going to repeat the earlier calculations, but this time, you will make three functions, one to calculate each of the areas.

### Assignment

Write functions to compute and return the areas of squares, rectangles, and circles. These functions should not display the values directly, but rather should return them, so they could be used in other parts of the program.

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.

Below the function, write code to prompt the user for the side of a square and save it into a variable, then pass this variable to the function to compute the area. Finally, get the result back from the function and display it.

Repeat the previous step to write and test the functions compute_area_rectangle and compute_area_circle.

Write a loop to ask the user what kind of shape they have, then prompt for the length of a side, or sides, or radius, and then calls the appropriate function, and displays the result. The program should continue looping until the user enters "quit" for the shape.

### STRETCH CHALLENGE

Recognize that you can compute the area of a square by passing the task along to a function that computes the areas of rectangles, by giving it the side of the square twice.

Change your program so that the compute_area_square function doesn't compute the area directly, but instead calls the compute_area_rectangle to do the work. It should pass the square side length to it (twice) and then return the value that the compute_area_rectangle function computes.

Write a new function called compute_area that accepts a first parameter of shape that can be either "square" or "circle" and then a value for the length of the side or the radius depending on the context. The function should then determine the correct function to use, based on the first parameter, call it, and return the value.

Change your program to use this function for the square and circle cases and verify that it works.

Add the ability for your new compute_area function to also compute the areas for rectangles. This means that you'll have to be able to accept calls like this: compute_area("circle", 5), this: compute_area("square", 10), and this compute_area("rectangle", 7, 8).

In order to make this work correctly, you'll need to make use of a default value for the last parameter.

Change your program to use this for all three calculations and verify that it works.

## [basic_functions.py](./basic_functions.py)

### Overview

This checkpoint is designed to help you practice writing basic functions.

### Assignment

Write three functions:

display_regular—Receives a string and prints it out, exactly as received.

display_uppercase—Receives a string, converts it to upper case, and then prints it out.

display_lowercase—Receives a string, converts it to lower case, and then prints it out.

In your program below the functions, ask the user to type a message. Then, pass that message to each of the three functions, so it it displays it each way, as shown:

```
What is your message? Brother Burton
Brother Burton
BROTHER BURTON
brother burton
```

Another example is:

```
What is your message? The only thing we have to fear is FEAR itself!
The only thing we have to fear is FEAR itself!
THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF!
the only thing we have to fear is fear itself!
```

### Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

Try your program with each of the following conditions and ensure that it works as expected.

- A single word
- A phrase with multiple words
- A word in ALL CAPS
- A phrase where each word starts with a capital
- An empty string

## [wind_chill_calculations.py](./wind_chill_calculations.py)

### Overview

When it's cold outside and the wind is blowing, it feels even colder!

(For those of you that have been to the BYU-Idaho campus in Rexburg during a Winter semester, you are very familiar with this concept.)

To try to quantify how cold it feels outside, instead of using temperature, a calculation for "wind chill" has been developed that takes into account both the temperature and the wind speed.

The U.S. National Weather Service defines the following formula to calculate wind chill in degrees Fahrenheit from a temperature in degrees Fahrenheit and wind speed in miles per hour:

### Wind Chill Chart and Formula

(To find the formula, follow the above link and look for the formula at the bottom of the chart.)

Keep in mind that:

T is the temperature in degrees Fahrenheit

V is the wind speed in miles per hour

V^0.16 means V to the power of 0.16, which can be found in Python using the \*\* operator.

### Assignment

Your assignment is to write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service chart does. To help users who are more familiar with Celsius, your program should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit before using the formula.

The following shows the expected output of this program:

```
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
```

Another example that uses Celsius is:

```
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
```

This assignment is designed to be smaller than previous assignments and is therefore not broken up into a milestone component and a final deliverable. Instead, you should complete the whole program for this lesson.

### REQUIREMENTS

The following are the required components of this assignment:

Write a function to calculate and return the wind chill based on a given temperature and wind speed.

Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.

### SHOWING CREATIVITY

Because this assignment is so clearly defined, it is more difficult to find a way to show creativity. Because of this, you are welcome to, but not required to add anything additional the way you did in previous assignments. Instead, if you meet the requirements above, you are eligible for 100% on the assignment.
