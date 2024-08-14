import random

def generate_hint(secret_word, guess):
    hint = ''
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += '_'
    return hint

def word_guessing_game():
    secret_word = "mosiah"
    total_guesses = 0
    
    print("Welcome to the word guessing game!\n")
    print("Your hint is: " + "_ " * len(secret_word))
    
    while True:
        guess = input("What is your guess? ").strip().lower()
        total_guesses += 1
        
        if len(guess) != len(secret_word):
            print(f"Sorry, the guess must have the same number of letters as the secret word ({len(secret_word)} letters).")
            continue
        
        if guess == secret_word:
            print(f"Congratulations! You guessed it!\nIt took you {total_guesses} guesses.")
            break
        else:
            hint = generate_hint(secret_word, guess)
            print(f"Your hint is: {hint}\n")

word_guessing_game()