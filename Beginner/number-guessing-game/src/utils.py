def display_welcome_message(min, max):
    print(
        "Welcome to the Number Guessing Game!\n" \
        f"I'm thinking of a number between {min} and {max}.\n"
    )


def display_rules(easy_attemtps, medium_attempts, hard_attempts):
    print(
        f"Please select the difficulty level:\n" \
        f"1. Easy ({easy_attemtps} chances)\n" \
        f"2. Medium ({medium_attempts} chances)\n" \
        f"3. Hard ({hard_attempts} chances)\n"
    )


def get_difficulty_choice():
    return int(input("\nEnter your choice: "))


def display_difficulty_choice(difficulty_name):
    print(f"Great! You have selected the {difficulty_name} difficulty level.\n")


def display_start_message():
    print("Let's start the game!\n")


def get_user_guess():
    return int(input("Enter your guess: "))


def display_win_message(remaining_attempts):
    print(f"Congratulations! You guessed the correct number in {remaining_attempts} attempts.")


def display_lose_message(random_number):
    print("Game Over! You've used all your chances.\n")
    print(f"The correct number was {random_number}.")