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