"""
Overview
At this point in the course, you have learned how to use the major building blocks of programming, including variables, if-statements, loops, lists, and now files. Equipped with these tools, you can use them to solve real-world problems.

For this assignment you will write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.

Project Description
The dataset you will be using comes from OurWorldInData.org from an article on the Spanish Flu. The first graph on that page shows the life expectancies over the years for various countries.

You can download the dataset directly here: life-expectancy.csv. This is a .csv (Comma Separated Values) file that contains the data you'll need with each column separated by commas. There are roughly 19,000 rows in this dataset.

This dataset is licensed under the Creative Commons BY license, you may also read the Life Expectancy Data License.

Your task is to write a program to help analyze this large amount of data.

Assignment
Download the dataset and write a Python program to analyze it to answer the following questions:

What is the year and country that has the lowest life expectancy in the dataset?

What is the year and country that has the highest life expectancy in the dataset?

Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.

A sample run could look as follows:


Enter the year of interest: 1959

The overall max life expectancy is: 86.751 from Monaco in 2019
The overall min life expectancy is: 17.76 from Iceland in 1882

For the year 1959:
The average life expectancy across all countries was 54.95
The max life expectancy was in Norway with 73.49
The min life expectancy was in Mali with 28.077

Milestone Requirements
At the end of Lesson 11, to help make sure you are on track to finish the assignment, you need to complete the following:

Download the dataset

Load the dataset in your Python program

Iterate through the data line by line

Split each line into parts

Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. (Note that at this point, you just need the value for this, not the year and the country for that value.)

Final Requirements
Finish the program by getting the answers to the questions above and adding the required functionality.

Showing Creativity and Exceeding Requirements
You can show creativity and exceed the core requirements by adding any kind of data exploration or additional features. For example, you could:

Identify the year and country that has the largest drop from one year to the next.

Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.

Look for interesting anomalies or patterns in the data.

Find another dataset and work with it.

Anything else you can think of!
"""

import csv

file_path = 'life-expectancy.csv'

min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        life_expectancy = float(row[3])
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy

print(f"Lowest life expectancy in the dataset: {min_life_expectancy}")
print(f"Highest life expectancy in the dataset: {max_life_expectancy}")

user_year = input("\nEnter the year of interest: ")

total_life_expectancy = 0
count = 0
min_life_expectancy_year = float('inf')
max_life_expectancy_year = float('-inf')
country_min = ''
country_max = ''

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        year = row[2]
        if year == user_year:
            life_expectancy = float(row[3])
            total_life_expectancy += life_expectancy
            count += 1
            if life_expectancy < min_life_expectancy_year:
                min_life_expectancy_year = life_expectancy
                country_min = row[1]
            if life_expectancy > max_life_expectancy_year:
                max_life_expectancy_year = life_expectancy
                country_max = row[1]

if count > 0:
    average_life_expectancy = total_life_expectancy / count
    print(f"\nFor the year {user_year}:")
    print(f"The average life expectancy across all countries was: {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {country_max} with {max_life_expectancy_year:.2f}")
    print(f"The min life expectancy was in {country_min} with {min_life_expectancy_year:.2f}")
else:
    print(f"No data found for the year {user_year}")