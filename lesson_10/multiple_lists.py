"""
Overview
Sometimes you have two lists that you want to keep in sync with each other. For example, in this assignment, you will track bank accounts and the balances in each one.

Hint from Instructor:
In future courses you will learn how to create a new custom data type (so you aren't limited to ints, floats, and strings). In that case, you can create a data type for bank accounts that stores both the name of the account and it's balance. Then, you only have one list: a list of bank accounts. This is called Programming with Classes or "Object-oriented Programming."

Assignment
CORE REQUIREMENTS
Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

Create two lists, one for the names of the bank accounts, and one for the balances.

Ask the user for the name of the bank account and then for it's current balance. Keep looping until the user types "quit" for the name of an account. For each one, add the name and the balance to the appropriate list.

Loop through the lists using an index and display the name of the account with the balance next to it.

Compute and display the total balance in all of the accounts and the average balance.

The following shows the expected output:


Enter the names and balances of bank accounts (type: quit when done)
What is the name of this account? checking
What is the balance? 102.57
What is the name of this account? savings
What is the balance? 82.32
What is the name of this account? emergency fund
What is the balance? 200.00
What is the name of this account? quit

Account Information:
checking - $102.57
savings - $82.32
emergency fund - $200.0

Total: $384.89
Average: $128.30

STRETCH CHALLENGE
Determine which bank account has the highest balance and display the name and balance of that account.

Change your display so that it shows the index of the account next to the name.

After displaying the list, ask the user if they want to update an account. If they respond with yes, ask for the index of the account, and the new balance.

Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.

The following shows the expected output after completing the stretch challenges:


Enter the names and balances of bank accounts (type: quit when done)
What is the name of this account? checking
What is the balance? 238.12
What is the name of this account? savings
What is the balance? 392.99
What is the name of this account? quit

Account Information:
0. checking - $238.12
1. savings - $392.99

Total: $631.11
Average: $315.56
Highest balance: savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 0
What is the new amount? 200

Account Information:
0. checking - $200.00
1. savings - $392.99

Do you want to update an account? yes
What account index do you want to update? 1
What is the new amount? 425.50

Account Information:
0. checking - $200.00
1. savings - $425.50

Do you want to update an account? no

Account Information:
0. checking - $200.00
1. savings - $425.50
"""

account_names = []
account_balances = []

print("Enter the names and balances of bank accounts (type: quit when done)")
while True:
    account_name = input("What is the name of this account? ")
    if account_name.lower() == "quit":
        break
    account_balance = float(input("What is the balance? "))
    account_names.append(account_name)
    account_balances.append(account_balance)

def display_account_info():
    print("\nAccount Information:")
    for i in range(len(account_names)):
        print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

display_account_info()

total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances) if account_balances else 0

print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")

if account_balances:
    max_balance_index = account_balances.index(max(account_balances))
    print(f"Highest balance: {account_names[max_balance_index]} - ${account_balances[max_balance_index]:.2f}")

while True:
    update = input("\nDo you want to update an account? (yes/no) ").lower()
    if update == "no":
        break
    index_to_update = int(input("What account index do you want to update? "))
    if 0 <= index_to_update < len(account_names):
        new_balance = float(input("What is the new amount? "))
        account_balances[index_to_update] = new_balance
        display_account_info()
    else:
        print("Invalid index. Please try again.")

print("\nFinal Account Information:")
display_account_info()