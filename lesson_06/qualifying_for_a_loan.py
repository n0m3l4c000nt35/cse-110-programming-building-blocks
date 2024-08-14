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