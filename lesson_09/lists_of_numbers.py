"""
Assignment
Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

Once you have a list, have your program do the following:

CORE REQUIREMENTS
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Compute the sum, or total, of the numbers in the list.

Compute the average of the numbers in the list.

Find the maximum, or largest, number in the list.

The following shows the expected output:


Enter a list of numbers, type 0 when finished.
Enter number: 18
Enter number: 36
Enter number: 2
Enter number: 48
Enter number: 6
Enter number: 12
Enter number: 9
Enter number: 0
The sum is: 131
The average is: 18.714285714285715
The largest number is: 48

STRETCH CHALLENGE
Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

The following shows the expected output after completing the stretch challenges:


Enter a list of numbers, type 0 when finished.
Enter number: 3
Enter number: 5
Enter number: 7
Enter number: 3
Enter number: 2
Enter number: -1
Enter number: -4
Enter number: -8
Enter number: 0
The sum is: 7
The average is: 0.875
The largest number is: 7
The smallest positive number is: 2
The sorted list is:
-8
-4
-1
2
3
3
5
7
"""

numbers = []

print("Enter a list of numbers, type 0 when finished.")

while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    numbers.append(number)

total_sum = sum(numbers)

average = total_sum / len(numbers) if numbers else 0

max_number = max(numbers) if numbers else None

smallest_positive = min([num for num in numbers if num > 0], default=None)

sorted_numbers = sorted(numbers)

print(f"The sum is: {total_sum}")
print(f"The average is: {average}")
print(f"The largest number is: {max_number}")
print(f"The smallest positive number is: {smallest_positive}")
print("The sorted list is:")

for num in sorted_numbers:
    print(num)