import random

# Dictionary of 100 animal and plant words
words = ['aardvark', 'baboon', 'camel', 'daffodil', 'elephant', 'fern', 'giraffe', 'honeybee', 'iguana', 'jaguar',
         'kangaroo', 'lilac', 'maple', 'narwhal', 'oak', 'panda', 'quokka', 'rose', 'salamander', 'tulip',
         'umbrella', 'vulture', 'walrus', 'xylophage', 'yak', 'zebra', 'acacia', 'bison', 'cardinal', 'dandelion',
         'eggplant', 'fox', 'goldfish', 'hummingbird', 'iris', 'kiwi', 'lavender', 'magnolia', 'newt', 'orchid',
         'peony', 'quail', 'rabbit', 'sunflower', 'tarantula', 'unicorn', 'violet', 'whale', 'xanthium', 'yarrow',
         'zebra', 'angelfish', 'bamboo', 'clover', 'daisy', 'elderberry', 'fig', 'geranium', 'hyacinth', 'ivy',
         'kale', 'lotus', 'magnolia', 'nettle', 'orchid', 'poppy', 'quince', 'raven', 'sunflower', 'tiger']

# Dictionary of 30 funny phrases
funny_phrases = [
    "Oops, looks like you've got a few screws loose there, bud!",
    "Really? That's the best you could come up with? Come on, I know you can do better!",
    "Guess you're not as smart as you thought, huh? Don't worry, we all have our moments.",
    "Oof, that one hurt my brain a little. Maybe take a breather and try again?",
    "Hmm, I think your brain must be on vacation or something. No worries, it'll come back eventually!",
    "Yikes, that was a real head-scratcher, wasn't it? Don't worry, I still think you're a genius... sort of.",
    "Aw, come on, even a toddler could have figured that one out! But hey, at least you're trying, right?",
    "Whoa, that was a real brain fart, wasn't it? Don't worry, it happens to the best of us.",
    "Oof, that was a real doozy, wasn't it? Don't worry, I'm sure your brain is just taking a little nap.",
    "Ooh, that one must have really hurt your noggin, huh? Don't worry, I've got plenty more where that came from!",
    "Looks like you're really putting that brain of yours through the wringer today, aren't you?",
    "Wow, that was a real head-scratcher, wasn't it? Don't worry, I'm sure you'll get the hang of this eventually.",
    "Yikes, that one was a real doozy, wasn't it? Don't worry, I'm sure your brain is just taking a little vacation.",
    "Oof, that was a real brain teaser, wasn't it? Don't worry, I'm sure you'll get it eventually... maybe.",
    "Whoa, that was a real head-spinner, wasn't it? Don't worry, I'm sure your brain will come back to you eventually.",
    "Ooh, that one must have really put your thinking cap through the wringer, huh? Don't worry, I'm still impressed!",
    "Yikes, that was a real brain buster, wasn't it? Don't worry, I'm sure you'll figure it out... eventually.",
    "Wow, that was a real head-scratcher, wasn't it? Don't worry, I'm sure your brain is just taking a little power nap.",
    "Oof, that was a real doozy, wasn't it? Don't worry, I'm sure you'll get the hang of this in no time... maybe.",
    "Ooh, that one must have really made your brain work overtime, huh? Don't worry, I'm sure it'll all come back to you eventually.",
    "Yikes, that was a real brain teaser, wasn't it? Don't worry, I'm sure your brain is just playing a little game of hide and seek.",
    "Wow, that was a real head-spinner, wasn't it? Don't worry, I'm sure your brain is just taking a little vacation.",
    "Oof, that was a real doozy, wasn't it? Don't worry, I'm sure you'll figure it out... eventually. Probably.",
    "Ooh, that one must have really put your thinking cap through the wringer, huh? Don't worry, I'm still impressed... kind of.",
    "Yikes, that was a real brain buster, wasn't it? Don't worry, I'm sure your brain is just taking a little power nap.",
    "Wow, that was a real head-scratcher, wasn't it? Don't worry, I'm sure you'll get the hang of this in no time... maybe.",
    "Oof, that was a real doozy, wasn't it? Don't worry, I'm sure your brain is just playing a little game of hide and seek.",
    "Ooh, that one must have really made your brain work overtime, huh? Don't worry, I'm sure it'll all come back to you eventually... probably.",
    "Yikes, that was a real brain teaser, wasn't it? Don't worry, I'm sure your brain is just taking a little vacation.",
    "Wow, that was a real head-spinner, wasn't it? Don't worry, I'm sure you'll figure it out... eventually. Hopefully."
]

# We assigned the WORD with the random dictionary
word = random.choice(words)

# We decide how many lives we have
guessed_letters = []
lives = 6

# ASCII art for the hangman
hangman_art = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
]

# Game loop
# the commas and the space between is where the user should insert a letter
# After we implemented the "_" for where the letter should be guessed
# We added the hangman_art to the 6 lives and to print how many we have left
while True:

    print(" ".join(["_" if letter not in guessed_letters else letter for letter in word]))
    print(hangman_art[6 - lives])
    print(f"Lives: {lives}")

    # We get the user input and the comment he would receive to start with.

    guess = input("Guess the letter: ").lower()

    # Check if the guess is valid, to asure if he puts valid alphabetical words
    #and not numbers or other symbols and to be sure is one word at a time.
    #if all is correct to continue with the code
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    # Check if the letter has already been guessed and if he did to print messege
    # that letter already been guessed.
    if guess in guessed_letters:
        print(f"You already guessed that letter '{guess}'. {random.choice(funny_phrases)}")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word if not to lose a life and the ascii code
    #to be printed for losing only 1 life and to receive the funny comment
    # If he looses to be shown the correct word
    if guess not in word:
        lives -= 1
        print(f"Incorrect. You have {lives} lives left. {random.choice(funny_phrases)}")
        if lives == 0:
            print(f"You lose! The word was '{word}' You can do better than that TRY AGAIN.")
            break
    else:
        print(f"Correct! '{guess}' is in the word. {random.choice(funny_phrases)}")

        # Check if the player has won and to be congratulated and say the
        #corect word was guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word ! Hope you enjoyed the game. Come Again ! '{word}'. a"
                  f"")
            break