grade_percentage = float(input("Enter your grade percentage: "))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

last_digit = int(str(grade_percentage)[-1])

if last_digit >= 7 and letter != "A" and letter != "F":
    sign = "+"
elif last_digit < 3 and letter != "F":
    sign = "-"
else:
    sign = ""

if sign:
    print("Your letter grade is:", letter + sign)
else:
    print("Your letter grade is:", letter)

if grade_percentage >= 70:
    print("Congratulations! You passed the course.")
else:
    print("You did not pass the course. Keep working hard!")