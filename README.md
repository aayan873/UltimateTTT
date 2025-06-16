#  Ultimate Tic-Tac-Toe Bot Competition

**Ultimate Tic-Tac-Toe Bot Competition** — a coding contest where participants write bots to compete

> ⚠️ This repository contains game logic, simulation scripts, and tournament management code.

---

## 🎮 Game Overview

**Ultimate Tic-Tac-Toe** is played on a 9×9 grid, subdivided into nine 3×3 local boards (the global board). Each move in a cell determines where the opponent must play next. The goal is to win three local boards in a row — just like regular Tic-Tac-Toe, but on a grander scale.

- The board is represented as a 9×9 matrix.
- A move is a `(row, col)` tuple (0-indexed).
- Winning a local board earns you a cell on the global board.
- If a local board is already won or full, the next player can choose any available cell on any valid board.

---

## 🧩 Repository Structure

UltimateTTT/  
📁 ultimate-ttt-competition/
├── evaluation/
│ ├──bots/
│ │ ├── random_bot.py # Example random bot
│ │ └── ... # Other participant bots
│ ├── judge.py
│ ├── ultimate_ttt_engine.py # Game logic and rule enforcement
│ ├──Compfile/
│ │ ├── bot_template.py # Bot template where participants can implement thier bots
│ │ ├── player_vs_bot.py # Script to play against any bot manually
│ │ ├── bot_vs_bot.py # Game between 2 bots
│ │ ├── random_bot.py # Bot that return random moves
│ │ ├── ultimate_ttt_engine.py # Game logic and rule enforcement
│ └── README.md # This file

---

## Goal of the Competition
Create the best bot that can beat other bots in Ultimate Tic-Tac-Toe.


## 📂 How Bots Work

Each bot is a Python file inside the `bots/` directory, and must implement the following function:

```python
def play(board, prev_move, player):
    # board: 9x9 current board state
    # prev_move: (row, col) of the last move played
    # player: 1 or 2 (you are given your ID)
    # Return: (row, col) of your move
    ...
