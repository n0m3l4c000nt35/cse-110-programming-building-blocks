"""
Overview
Practice working with lists.

Assignment
Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

Hint 1: You should keep asking for friends, as long as the name is not "end". (Does this sound like a loop you know?)

Hint 2: Be careful not to add "end" to the list of names when it is typed. You can check if the name is or is not something before you add it to the list.

The following examples show the expected output:


Type the name of a friend: Matthew
Type the name of a friend: Mark
Type the name of a friend: Luke
Type the name of a friend: John
Type the name of a friend: end

Your friends are:
Matthew
Mark
Luke
John
Another example could be the following:


Type the name of a friend: Peter
Type the name of a friend: James
Type the name of a friend: John
Type the name of a friend: end

Your friends are:
Peter
James
John

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Test it with just one name.

Test it with 3–4 names

Make sure that the word "end" doesn't display at the end of your list of friends.

Test it by entering the same name 3 times before typing end (the result should be that you see the name repeated 3 times in the list).

Test it with no names, just the word end, and make sure it doesn't cause any errors.
"""

friends = []

while True:
    name = input("Type the name of a friend: ")

    if name.lower() == "end":
        break

    friends.append(name)

print("\nYour friends are:")
for friend in friends:
    print(friend)