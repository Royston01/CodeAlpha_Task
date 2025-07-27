import random

def hangman_game():
    # List of predefined words
    words = ["python", "computer", "hangman", "programming", "keyboard"]
    
    # Select a random word
    word = random.choice(words).lower()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()   # Letters guessed by user
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(f"The word has {len(word)} letters.")
    print("You have 6 incorrect guesses allowed.\n")
    
    # Game loop
    while incorrect_guesses < max_incorrect and word_letters:
        # Display current progress
        current_word = ""
        for letter in word:
            if letter in guessed_letters:
                current_word += letter + " "
            else:
                current_word += "_ "
        
        print(f"Word: {current_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(draw_hangman(incorrect_guesses))
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue
        
        # Add guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
    
    # Game over - check if won or lost
    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
        print("You won! 🎉")
    else:
        print(draw_hangman(incorrect_guesses))
        print(f"Game over! The word was: {word}")
        print("Better luck next time! 💀")

def draw_hangman(incorrect_guesses):
    """Draw hangman based on number of incorrect guesses"""
    stages = [
        # 0 incorrect guesses
        """
           -----
           |   |
           |
           |
           |
           |
        --------
        """,
        # 1 incorrect guess
        """
           -----
           |   |
           |   O
           |
           |
           |
        --------
        """,
        # 2 incorrect guesses
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        --------
        """,
        # 3 incorrect guesses
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        --------
        """,
        # 4 incorrect guesses
        """
           -----
           |   |
           |   O
           |  /|\\
           |
           |
        --------
        """,
        # 5 incorrect guesses
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        --------
        """,
        # 6 incorrect guesses - game over
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        --------
        """
    ]
    return stages[incorrect_guesses]

def main():
    while True:
        hangman_game()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing Hangman! Goodbye!")
            break
        print("\n" + "="*50 + "\n")

# Run the game
if __name__ == "__main__":
    main()
