shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish):")
while True:
    item = input("Item: ")
    if item.lower() == "quit":
        break
    shopping_list.append(item)

print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

index = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")