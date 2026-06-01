# Number Guessing Game CLI

A command-line number guessing game where players attempt to guess a randomly generated number within a limited number of attempts. This project demonstrates CLI development, user input handling, control flow, random number generation, and game state management.

🔗 **Project Source:** https://roadmap.sh/projects/number-guessing-game

🔗 **Repository:** https://github.com/Mika0x/backend-projects/tree/main/Beginner/number-guessing-game

---

## 📌 Overview

Number Guessing Game CLI is a simple terminal-based game in which the computer randomly selects a number between 1 and 100. The player must guess the number before running out of attempts.

Players can choose between multiple difficulty levels, each providing a different number of chances. After every incorrect guess, the game provides feedback indicating whether the target number is higher or lower than the guessed value.

---

## 🚀 Features

- Random number generation between 1 and 100
- Multiple difficulty levels
- User input validation
- Limited attempts based on difficulty
- Feedback after incorrect guesses
- Win and lose conditions
- Attempt tracking

### Difficulty Levels

- Easy (10 attempts)
- Medium (5 attempts)
- Hard (3 attempts)

---

## 🛠️ Tech Stack

- Python
- Python Standard Library
- random module

---

## 📂 Project Structure

```text
number-guessing-game/
│── src/
│   └── number-guessing-game.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mika0x/backend-projects.git
cd backend-projects/Beginner/number-guessing-game
```

### 2. Verify Python Installation

```bash
python3 --version
```

---

## ▶️ Usage

```bash
python3 src/number-guessing-game.py
```

---

## 🎮 Example Gameplay

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.

Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
```

---

## 📝 Notes

- A random number is generated each time the game starts.
- Difficulty determines the number of available attempts.
- Incorrect guesses provide directional hints.
- The game ends when the player guesses correctly or runs out of attempts.

---

## 🔮 Future Improvements

- Play multiple rounds
- High score tracking
- Timer support
- Hint system
- Remaining-attempt display
- Persistent statistics

---

## 📄 License

This project is open-source and available under the MIT License.
