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

animal = ["dog", "cat", "chicken", "kangaroo", "elephant", "dolphin", "penguin", "pigeon", "lion", "tardigrade"]


# Choose a random word from the list
def choose_word():
    return random.choice(animal)

# Display the word with guessed letters and underscores for unguessed ones
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Track guessed letters, while the player gets 8 tries.
def play_hangman():
    word = choose_word().lower()
    guessed_letters = set()
    tries = 8
    print("Welcome to Hangman!")
    print(f"Your word has {len(word)} letters.")
# Display the unguessed word as underscores
    print(display_word(word, guessed_letters))