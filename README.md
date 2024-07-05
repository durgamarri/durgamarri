import random

# List of words to choose from
words = ["python", "java", "swift", "javascript", "hangman", "programming", "developer"]

def select_random_word(words):
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def play_hangman():
    word = select_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word:", display_current_state(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}'!")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if incorrect_guesses == max_incorrect_guesses:
            print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
