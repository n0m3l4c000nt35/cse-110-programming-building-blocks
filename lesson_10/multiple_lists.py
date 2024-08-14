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