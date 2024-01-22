import random

def choose_random_word():
    word_list = ["apple", "banana", "cherry", "grape", "lemon", "orange", "strawberry", "watermelon"]
    return random.choice(word_list)

def play_word_guessing_game():
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word, one letter at a time.")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("Secret word:", display_word)
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in secret_word):
                print(f"Congratulations! You've guessed the word: {secret_word}")
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess. {attempts} attempts left.")

    if attempts == 0:
        print(f"Out of attempts. The secret word was: {secret_word}")

if __name__ == "__main__":
    play_word_guessing_game()
