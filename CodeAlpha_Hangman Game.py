import random

# List of predefined words
words = ["python", "hangman", "coding", "program", "developer"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Game loop
while wrong_guesses < max_wrong:
    # Display current word state
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check if word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong - wrong_guesses}")
    else:
        print("Good guess!")

# Lose condition
if wrong_guesses == max_wrong:
    print("\n❌ Game Over!")
    print("The word was:", secret_word)
