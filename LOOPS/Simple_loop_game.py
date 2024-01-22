import random

def guess_the_number():
    # Generate a random number between 1 and 20
    target_number = random.randint(1, 20)

    # Initialize variables
    attempts = 0
    guessed_correctly = False

    # While loop for the game
    while not guessed_correctly:
        # Get user input for their guess
        user_guess = int(input("Enter your guess (between 1 and 20): "))

        # Update attempts count
        attempts += 1

        # Check if the guess is correct, too high, or too low
        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            guessed_correctly = True
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the function to start the game
guess_the_number()
