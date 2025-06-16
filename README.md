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
![687474703a2f2f7374617469632e7a7962756c756f2e636f6d2f54616e6757696c6c2f7a30636368307761717274303735387761377932666174382f496e636f6d706c6574655f556c74696d6174655f5469632d5461632d546f655f426f6172642e706e67](https://github.com/user-attachments/assets/ba4d93f1-5403-41ad-a73e-f6bd45b8c959)


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
