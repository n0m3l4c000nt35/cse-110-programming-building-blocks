"""
Overview
For this assignment, you will implement a simplistic system to determine if a user can qualify for a loan.

The Problem: Qualifying for a loan
When loaning money to someone, you want to have some level of confidence that they will be able to repay the loan.

There are different characteristics you might base this decision on, or different questions you might ask someone. And depending on their answers to those questions, you might ask other questions. For example, consider the following possible questions:

Does the person have a job, and if so, how long have they worked there, and how much money do they make?

Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)

Does the person have a good credit score or history of paying back loans?

How much other debt does the person have?

How much money does the person have?

Will the person have a down payment, and if so, what percentage of the loan does it amount to?

Assignment
Write a program to determine whether to loan money based on the following rules.

First, ask for a rating from 1–10 on the following:

How large is the loan?

How good is your credit history?

How high is your income?

How large is your down payment?

Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:

First, check if the loan size is at least 5. If it is, use the following rules:

If the credit history and income are both at least 7, then the decision is "yes"

If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"

Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

Otherwise (if the loan is not 5 or greater), use these rules:

If the credit is less than 4, then the decision is "no"

Otherwise, check the following:

If either the income or the down payment is at least 7, the decision is "yes"

If both the income and the down payment are at least 4, then the answer is "yes"

Otherwise, the decision is "no"

Finally, display the decision to the user.

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Test your program with these values and ensure you arrive at the decision indicated:

Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"

Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"

Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"

Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"

Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"
"""

def get_rating(prompt, min_val, max_val):
    while True:
        try:
            rating = int(input(prompt))
            if min_val <= rating <= max_val:
                return rating
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

def loan_qualification():
    print("Welcome to the Loan Qualification System!")
    print("Please rate the following on a scale of 1 to 10:")

    loan_size = get_rating("How large is the loan? (1-10): ", 1, 10)
    credit_history = get_rating("How good is your credit history? (1-10): ", 1, 10)
    income = get_rating("How high is your income? (1-10): ", 1, 10)
    down_payment = get_rating("How large is your down payment? (1-10): ", 1, 10)

    if loan_size >= 5:
        if credit_history >= 7 and income >= 7:
            decision = "yes"
        elif credit_history >= 7 or income >= 7:
            if down_payment >= 5:
                decision = "yes"
            else:
                decision = "no"
        else:
            decision = "no"
    else:
        if credit_history < 4:
            decision = "no"
        else:
            if income >= 7 or down_payment >= 7:
                decision = "yes"
            elif income >= 4 and down_payment >= 4:
                decision = "yes"
            else:
                decision = "no"

    print(f"\nDecision: {decision.capitalize()}")

loan_qualification()