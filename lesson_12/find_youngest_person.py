"""
Overview
This checkpoint will help you practice finding things in a list.

Assignment
To simplify your program to focus on the task at hand, instead of reading from a file, please copy and paste the following list of people and their ages into your program:


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

Write a program to find the youngest person in the list.

Consider following these steps to build up to the finished program:

Iterate through the list and display each string to the screen.

Split the string into a name and age and print them to the screen.

Find the age that is the youngest.

Keep track of the name of the person that is the youngest.

Testing Procedure
Because there is no user input, you don't need to test the program with different values. Instead, make sure that that following components are in place:

The list of people is included in the program.

The program can iterate through each string in the list.

The program can split the string into the appropriate pieces.

The youngest age is identified.

The name of the youngest person is identified.
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = float('inf')
youngest_person = ""

for person in people:
    print(person)
    
    name, age = person.split()
    age = int(age)
    print(f"Name: {name}, Age: {age}")
    
    if age < youngest_age:
        youngest_age = age
        youngest_person = name

print(f"\nThe youngest person is {youngest_person} with an age of {youngest_age}.")