## books.py

### Overview

Practice Opening Files

### Assignment

For this assignment, you'll download the file books.txt that contains the names of the books in the Book of Mormon, and save it to your computer.

Once you have the file saved to your computer, in VS Code, open the folder that contains it and create a new Python script.

Have your program open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

The following shows the expected output:

```
1 Nephi
2 Nephi
Jacob
Enos
Jarom
Omni
Words of Mormon
Mosiah
Alma
Helaman
3 Nephi
4 Nephi
Mormon
Ether
Moroni
```

### Testing Procedure

For this program, there isn't any user input, so you don't need to try different values. Instead, simply verify that the following work as described

The books.txt file is downloaded and saved to your computer.

Your program can open the file.

Your program reads a line from the file and displays it to the screen.

Your program iterates through each line in the file and displays them to the screen.

Your program strips off the "\n" characters at the end of each line before displaying them, so it doesn't produce a blank line in between each displayed line.

## human_resources_system.py

### Overview

Consider the scenario of a Human Resources (HR) system. It contains various information about the employees of a company, such as their names, ID numbers, job titles, salaries, etc. From this data you may need to run a payroll process to generate paychecks, generate information for tax purposes, or produce any number of reports of various kinds.

The data for these HR systems is stored on servers. In a real system, this data would be stored in a database, but for our purposes, we will practice by using data stored in a single text file.

### Assignment

Download the file hr_system.txt. This file contains information for a set of employees. The first few lines look as follows:

```
Alexia 1913 Engineer 84000
Herman 4266 Manager 106000
Jay 5849 Engineer 93000
Ahmad 1326 Tester 85000
```

The format of each line is:

```
name id_number job_title salary
```

There is a single space between each field of data.

Your assignment is to write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.

### CORE REQUIREMENTS

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Download the file and save it to your computer. In VS Code, open the folder that contains this file. Then, create a new Python script in that folder.

Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.

Split the line into parts and change your display, so that it shows only the names (instead of the whole line).

For each line, get the name and the job title for each person, and display those to the screen.

At this point, your output should look like the following:

```
Name: Alexia, Title: Engineer
Name: Herman, Title: Manager
Name: Jay, Title: Engineer
Name: Ahmad, Title: Tester
Name: Ciaran, Title: Engineer
Name: Callum, Title: Engineer
Name: Samantha, Title: Tester
Name: Antonio, Title: Tester
Name: May, Title: CFO
Name: Sebastian, Title: Scientist
Name: Kaitlyn, Title: Support
Name: William, Title: Tester
Name: Sophie, Title: Engineer
Name: Isaiah, Title: Designer
Name: Aimee, Title: CEO
Name: Patrick, Title: Sales
Name: Gloria, Title: Designer
Name: Joseph, Title: Sales
Name: Barbara, Title: Engineer
```

### STRETCH CHALLENGE

Strip off any leading and trailing whitespace from each line.

In addition to the name and the job title, also access the salary and the ID number and save them into variables. Display all four values in this format: name (ID: id_number), job_title - $salary. Don't forget to convert the salary to a number and display it with two decimals.

The following shows the first few lines of expected output at this point.

```
Alexia (ID: 1913), Engineer - $84000.00
Herman (ID: 4266), Manager - $106000.00
Jay (ID: 5849), Engineer - $93000.00
Ahmad (ID: 1326), Tester - $85000.00
```

Instead of displaying the salary information, calculate and display a paycheck amount for the employee. Assume that they are paid twice a month.

Change the program so that it generates bonuses for anyone who is an engineer. For each of these employees, add $1000 to their paycheck amount.

The following shows sample output at the end of the stretch challenges:

```
Alexia (ID: 1913), Engineer - $4500.00
Herman (ID: 4266), Manager - $4416.67
Jay (ID: 5849), Engineer - $4875.00
Ahmad (ID: 1326), Tester - $3541.67
Ciaran (ID: 2019), Engineer - $3583.33
Callum (ID: 8005), Engineer - $4041.67
Samantha (ID: 4802), Tester - $3333.33
Antonio (ID: 1423), Tester - $2125.00
May (ID: 5575), CFO - $4666.67
Sebastian (ID: 7378), Scientist - $4250.00
Kaitlyn (ID: 4542), Support - $2625.00
William (ID: 7364), Tester - $3083.33
Sophie (ID: 3437), Engineer - $5541.67
Isaiah (ID: 1518), Designer - $2416.67
Aimee (ID: 8093), CEO - $5208.33
Patrick (ID: 2214), Sales - $3625.00
Gloria (ID: 4414), Designer - $3291.67
Joseph (ID: 9427), Sales - $3791.67
Barbara (ID: 5967), Engineer - $5333.33
```

## life_expectancy.py

### Overview

At this point in the course, you have learned how to use the major building blocks of programming, including variables, if-statements, loops, lists, and now files. Equipped with these tools, you can use them to solve real-world problems.

For this assignment you will write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.

### Project Description

The dataset you will be using comes from OurWorldInData.org from an article on the Spanish Flu. The first graph on that page shows the life expectancies over the years for various countries.

You can download the dataset directly here: life-expectancy.csv. This is a .csv (Comma Separated Values) file that contains the data you'll need with each column separated by commas. There are roughly 19,000 rows in this dataset.

This dataset is licensed under the Creative Commons BY license, you may also read the Life Expectancy Data License.

Your task is to write a program to help analyze this large amount of data.

### Assignment

Download the dataset and write a Python program to analyze it to answer the following questions:

What is the year and country that has the lowest life expectancy in the dataset?

What is the year and country that has the highest life expectancy in the dataset?

Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.

A sample run could look as follows:

```
Enter the year of interest: 1959

The overall max life expectancy is: 86.751 from Monaco in 2019
The overall min life expectancy is: 17.76 from Iceland in 1882

For the year 1959:
The average life expectancy across all countries was 54.95
The max life expectancy was in Norway with 73.49
The min life expectancy was in Mali with 28.077
```

### Milestone Requirements

At the end of Lesson 11, to help make sure you are on track to finish the assignment, you need to complete the following:

Download the dataset

Load the dataset in your Python program

Iterate through the data line by line

Split each line into parts

Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. (Note that at this point, you just need the value for this, not the year and the country for that value.)

### Final Requirements

Finish the program by getting the answers to the questions above and adding the required functionality.

### Showing Creativity and Exceeding Requirements

You can show creativity and exceed the core requirements by adding any kind of data exploration or additional features. For example, you could:

Identify the year and country that has the largest drop from one year to the next.

Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.

Look for interesting anomalies or patterns in the data.

Find another dataset and work with it.

Anything else you can think of!
