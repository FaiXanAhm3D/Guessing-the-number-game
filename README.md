# 🎯 Guess the Number — Match-Based Python Game

A Python terminal-based guessing game where the user plays through **3 matches**, each with **3 rounds**. Guess the correct number in any round to win that match. Win **2 out of 3 matches** to win the entire game!

---

## 🕹️ Game Rules

- Each **game session** has **3 matches**.
- Each **match** has **3 rounds**.
- In every match, a new random number is generated.
- If you guess the correct number in any round → ✅ You win the **match**.
- If you fail all 3 rounds → ❌ You lose the match and the correct number is shown.
- After 3 matches:
  - Win **at least 2 matches** → You win the game 🎉
  - Else → You lose the game ❌

- At the end of each game, you’ll be asked whether you want to **play again**.
- The script tracks your **overall score** (games won/lost) across multiple plays.

---

## ⚙️ How to Run

1. Make sure you have **Python 3** installed.
2. Clone the repository or download the script.
3. Open terminal in the script folder.
4. Run the game:
   ```bash
   python guess_the_number.py
