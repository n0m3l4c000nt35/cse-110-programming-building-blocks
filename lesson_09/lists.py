friends = []

while True:
    name = input("Type the name of a friend: ")

    if name.lower() == "end":
        break

    friends.append(name)

print("\nYour friends are:")
for friend in friends:
    print(friend)