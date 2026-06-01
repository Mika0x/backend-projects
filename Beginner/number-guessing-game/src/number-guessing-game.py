from utils import display_rules, display_welcome_message, get_difficulty_choice, display_difficulty_choice, display_start_message, get_user_guess, display_win_message, display_lose_message
import random

LOWER_END = 1
HIGHER_END = 100

DIFFICULTY = {
    1: {
        "name": "Easy",
        "attempts": 10
    },
    2: {
        "name": "Medium",
        "attempts": 5
    },
    3: {
        "name": "Hard",
        "attempts": 3
    }
}


def main():
    start_game()


def start_game():
    # Display a welcome message
    display_welcome_message(LOWER_END, HIGHER_END)

    # Display rules of the game
    display_rules(DIFFICULTY[1]["attempts"], DIFFICULTY[2]["attempts"], DIFFICULTY[3]["attempts"])

    # Generate an integer between 1 and 100 (inclusive)
    random_number = random.randint(1, 100)
    print(f"DEBUG: {random_number}")

    # Get the user's choice of difficulty
    difficulty_choice = get_difficulty_choice()
    while difficulty_choice not in [1, 2, 3]:
        print("\nIncorrect Option. Please choose between (1 - Easy, 2 - Medium, 3 - Hard)")
        difficulty_choice = get_difficulty_choice()

    # Set the user's number of attempts
    user_attempts = DIFFICULTY[difficulty_choice]["attempts"]

    display_difficulty_choice(DIFFICULTY[difficulty_choice]["name"])

    # Display the start game message!
    display_start_message()

    while user_attempts > 0:
        user_guess = get_user_guess()
        user_attempts -= 1

        if user_guess == random_number:
            display_win_message()
            break

        comparison = "less than" if random_number < user_guess else "greater than"
        print(f"Incorrect! The number is {comparison} {user_guess}.\n")

    if user_guess != random_number:
        display_lose_message(random_number)
        

if __name__ == "__main__":
    main()