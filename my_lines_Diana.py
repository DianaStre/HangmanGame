# Build a hangman game.
# build it how I want, the way I want it to run and respects 3 conditions.
# Conditions:
    #1. hardcode your chosen word in a list, theme/ category, max 25., min. 10.
    #2. word is chosen at random from list, but at start (default) it will be represented as underscores.
    # (e.g. "dog" -> "_ _ _")
    #3. Print as follows: "_ _ _", not as
    #"_
    #_
    #_"
# Limit your "lives"/changes to guess. Every team can choose their own number of tries,
# just inform the user about it.
    #4. We'll stick to English (for now).
    #5. When the user guesses correctly, the "Lives" will not be affected/ lost.
    #6. In the end, the user needs to WANT to play the game again. Make it happen! Choose your funniest messages of deep encouragement wisely.

# Deadline: 3 Octombrie

import random

# List of 10 words defined (as a list)
animals = ["cat", "dog", "elephant", "mouse", "kangaroo", "tardigrade", "octopus", "dolphin", "shark", "stork"]

# Choose a random word from the provided list
word = random.choice(animals).lower()
guessed_letters = []  # To store guessed letters
tries = 8  # User can adjust here the number of total tries

# Function to display the word with underscores for unguessed letters
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

print("Welcome to 😈Hell😈, there is only one way out!")
print(display_word())  # Display the unguessed word as underscores

# Main game loop, start with a function to allow input from user
while tries > 0:
    guess = input(f"\nYou have {tries} tries left to escape 💀Hell💀. Guess a letter: ").lower()

    # Ensures that only one letter is entered at a time
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter, there are no quick exits.")
        continue

    # If the player guesses correctly
    if guess in word:
        guessed_letters.append(guess)
        print(f"Good guess!😎 '{guess}' is in the word. One step closer to freedom!")
    else:
        tries -= 1  # If guessed incorrectly, reduces tries (by one)
        print(f"Wrong guess!💀 '{guess}' is not in the word. Get comfortable!")

    # Display current progress before another guess
    print(display_word())

    # Check if player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print(f"✨Congratulations! You've guessed the word: {word}. You may now leave Hell!✨")
        break
else:
    print(f"😞Sorry, you can't leave. The word was: {word}")
