import random

def guess_my_number():
    print("Welcome to Guess My Number Game!")
    
    magic_number = random.randint(1, 100)
    
    guess_count = 0
    
    while True:
        guess = int(input("What is your guess? "))
        
        guess_count += 1
        
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            break
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == "yes":
        guess_my_number()
    else:
        print("Thank you for playing!")

guess_my_number()