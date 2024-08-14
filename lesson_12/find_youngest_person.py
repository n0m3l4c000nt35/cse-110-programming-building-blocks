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