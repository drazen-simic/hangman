import random

def choose_word():
    """Randomly selects a word from a predefined list."""
    words = ["python", "hangman", "programming", "developer", "function", "variable", "control", "iteration"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the current state of the word with guessed letters revealed."""
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word before you run out of attempts.")
    
    # Step 1: Setup
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_left = 6  # Total attempts before losing
    word_set = set(word_to_guess)  # Unique letters in the word
    
    while attempts_left > 0:
        print("\n" + "-" * 40)
        print(f"Word to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts_left}")
        
        # Step 2: Get user input
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        # Step 3: Check the guess
        guessed_letters.add(guess)
        if guess in word_set:
            print("Good guess!")
            word_set.remove(guess)
            if not word_set:  # All letters guessed
                print(f"🎉 Congratulations! You've guessed the word: {word_to_guess}")
                break
        else:
            print("Incorrect guess!")
            attempts_left -= 1
    
    # Step 4: Game over
    if attempts_left == 0:
        print("\nGame over! You've run out of attempts.")
        print(f"The correct word was: {word_to_guess}")

def main():
    while True:
        hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
