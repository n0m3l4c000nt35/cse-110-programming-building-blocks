price_child_meal = float(input("What is the price of a child's meal? "))
price_adult_meal = float(input("What is the price of an adult's meal? "))

number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

sales_tax_rate = float(input("What is the sales tax rate? "))

subtotal = (price_child_meal * number_of_children) + (price_adult_meal * number_of_adults)

print(f"Subtotal: ${subtotal:.2f}")

sales_tax = subtotal * (sales_tax_rate / 100)

total_price = subtotal + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total_price:.2f}")

payment_amount = float(input("What is the payment amount? "))

change = payment_amount - total_price
print(f"Change: ${change:.2f}")

"""
Explanation of the Code

1. The program prompts the user to enter the prices of a child's meal and an adult's meal, storing these values as floating point numbers.
2. It then asks for the number of children and adults, storing these values as integers.
3. The user is prompted to enter the sales tax rate, which is stored as a floating point number.
.4 The subtotal is calculated by multiplying the number of children by the price of a child's meal and the number of adults by the price of an adult's meal, then adding these two values together.
5. The subtotal is displayed.
6. The sales tax is computed by multiplying the subtotal by the sales tax rate divided by 100.
7. The total price of the meal is calculated by adding the sales tax to the subtotal.
8. The program then asks for the payment amount, computes the change, and displays the change.
"""