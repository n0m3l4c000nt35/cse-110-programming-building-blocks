"""
Overview
In a text-based adventure game, the user is presented a scenario with different options. Depending on the option they choose, they have different consequences, which in turn present different choices for the next action.

Consider the following example:

You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?

The user can then type "match" or "flashlight".

If the user types "match" they may see a response such as:

You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?

Whereas, if the user typed "flashlight" in response to the original question, they may see a response such as:

You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?

Your choice at each step of the game determines what you see next and the options you have available at that point.

Instructions
Create your own text-based adventure game with at least three levels of choices. It's up to you to determine the scenarios, the choices, and the consequences.

Keep in mind the following guidelines and requirements:

You need to have at least three levels of scenarios with possible choices.

At least one of your scenarios must have more than two possible choices.

In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.

When checking the users responses, you should match on the keyword, regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).

Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

Choices should only work for the correct question.

In other words, if one scenario resulted in choices of Run/Hide, but another resulted in choices Follow/Look, you should not be able to respond with "Follow" to the question that asked for Run/Hide.

A good way to accomplish this is to have a series of nested if statements. (That is, the print and then the next if statement will be within the body/block of the first if statement.)

For each question, you should provide an "else" clause to handle the case that the user tries to type something other than the possible choices. It is up to you how to handle this case.

Showing Creativity and Exceeding Requirements
Obviously, you'll show creativity by customizing the prompts and choices. To achieve the grade category of "Shows creativity and exceeds requirements" for this one, you need to add something additional to the framework of the game. For example, you might add even more levels or you might have more choices at each level. You might add hidden choices or trick questions. Have fun with this and see what you can do!

If you've already learned other programming concepts (for example, loops, lists, etc.) you are welcome to use those concepts here as a way to make show creativity and exceed requirements.
"""

def get_choice(prompt, options):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in options:
            return user_input
        else:
            print("Sorry, I didn't understand that. Please choose one of the given options.")

print("Welcome to the Enchanted Forest Adventure!")
print("You find yourself lost in a mystical forest...")

print("\nYou come across a fork in the path.")
direction = get_choice("To the LEFT, you see sunlight filtering through the trees. To the RIGHT, you hear running water. Which way do you want to go? (LEFT/RIGHT): ", ["LEFT", "RIGHT"])

if direction == "LEFT":
    print("\nYou walk towards the sunlight and find a clearing with a pond shimmering in the middle.")
    print("Birds sing around you, and you feel a sense of peace.")
    explore_or_return = get_choice("Do you want to EXPLORE the clearing, or RETURN to the path? (EXPLORE/RETURN): ", ["EXPLORE", "RETURN"])
    
    if explore_or_return == "EXPLORE":
        print("\nYou explore the clearing and discover a hidden path leading deeper into the forest...")
        print("As you venture deeper, you encounter a mystical creature...")
        encounter = get_choice("Do you want to APPROACH the creature, or HIDE and observe? (APPROACH/HIDE): ", ["APPROACH", "HIDE"])
        
        if encounter == "APPROACH":
            print("\nYou cautiously approach the creature, which turns out to be a friendly forest spirit.")
            print("The spirit gifts you with a magical map revealing the forest's secrets...")
            print("Congratulations! You completed the first part of your journey.")
        elif encounter == "HIDE":
            print("\nYou quietly observe the creature from afar. It eventually disappears into the forest.")
            print("You decide to continue exploring the path...")
            print("Congratulations! You completed the first part of your journey.")

    elif explore_or_return == "RETURN":
        print("\nYou decide to return to the path and continue your journey...")
        print("You venture deeper into the forest, navigating through the dense trees and foliage...")
        print("As you walk further, you come across an ancient stone monument...")
        print("Congratulations! You completed the first part of your journey.")

elif direction == "RIGHT":
    print("\nYou follow the sound of running water and discover a babbling brook.")
    print("The water is crystal clear, and colorful butterflies flutter around.")
    follow_or_cross = get_choice("Do you want to FOLLOW the brook downstream, or CROSS over it to the other side? (FOLLOW/CROSS): ", ["FOLLOW", "CROSS"])
    
    if follow_or_cross == "FOLLOW":
        print("\nYou follow the brook downstream, enjoying the serene beauty of the forest...")
        print("As you walk along the brook, you notice a hidden cave entrance behind a waterfall...")
        explore_cave = get_choice("Do you want to EXPLORE the cave, or KEEP FOLLOWING the brook? (EXPLORE/KEEP): ", ["EXPLORE", "KEEP"])
        
        if explore_cave == "EXPLORE":
            print("\nYou enter the cave and discover ancient carvings on the walls...")
            print("Inside, you find a treasure chest filled with sparkling gems and artifacts.")
            print("Congratulations! You completed the first part of your journey.")
        elif explore_cave == "KEEP":
            print("\nYou decide to continue following the brook, wondering what else the forest holds...")
            print("Congratulations! You completed the first part of your journey.")

    elif follow_or_cross == "CROSS":
        print("\nYou carefully cross over the brook and explore the dense foliage on the other side...")
        print("As you explore, you stumble upon a hidden path leading to a mysterious ancient ruin...")
        investigate_ruins = get_choice("Do you want to INVESTIGATE the ruins, or RETURN to the brook? (INVESTIGATE/RETURN): ", ["INVESTIGATE", "RETURN"])
        
        if investigate_ruins == "INVESTIGATE":
            print("\nYou enter the ruins and uncover secrets of a lost civilization...")
            print("Congratulations! You completed the first part of your journey.")
        elif investigate_ruins == "RETURN":
            print("\nYou decide to return to the brook and continue exploring...")
            print("Congratulations! You completed the first part of your journey.")
