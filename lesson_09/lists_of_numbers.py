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