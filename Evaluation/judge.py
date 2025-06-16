import os
import sys
import importlib
import time
from ultimate_ttt_engine import UltimateTTT

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BOT_DIR = os.path.join(CURRENT_DIR, "bots")

if BOT_DIR not in sys.path:
    sys.path.append(BOT_DIR)

def to_module_name(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def get_mini_board_score(game, player):
    score = 0
    for r in range(3):
        for c in range(3):
            val = game.mainboard[r][c]
            if val == player:
                score += 0.25
            elif val == 3:
                score += 0
    return score

def run(idx_bot1, idx_bot2, all_bots):
    bot1_module = to_module_name(all_bots[idx_bot1][1])
    bot2_module = to_module_name(all_bots[idx_bot2][1])

    bot1 = importlib.import_module(bot1_module)
    bot2 = importlib.import_module(bot2_module)

    game = UltimateTTT()
    prev_move = None
    player = 1

    for _ in range(81):
        game.print_board()
        start_time = time.time()

        if player == 1:
            move = bot1.play(game.board, prev_move, 1)
        else:
            move = bot2.play(game.board, prev_move, 2)

        elapsed = time.time() - start_time

        if elapsed > 4:
            print(f"Player {player} exceeded 4 seconds. Player {3 - player} wins!")
            if 3 - player == 1:
                all_bots[idx_bot1][0] += 6
            else:
                all_bots[idx_bot2][0] += 6
            return

        if not game.move(*move):
            print(f"Invalid move by Player {player} at {move}. Player {3 - player} wins!")
            if 3 - player == 1:
                all_bots[idx_bot1][0] += 1
            else:
                all_bots[idx_bot2][0] += 1
            return

        prev_move = move
        player = 3 - player

    winner = game.get_winner()

    if winner == 1:
        all_bots[idx_bot1][0] += 1
    elif winner == 2:
        all_bots[idx_bot2][0] += 1
    else:
        p1_mb = get_mini_board_score(game, 1)
        p2_mb = get_mini_board_score(game, 2)
        all_bots[idx_bot1][0] += 0.5 + p1_mb
        all_bots[idx_bot2][0] += 0.5 + p2_mb

def competition():
    bot_folder = BOT_DIR
    bot_files = [
        f for f in os.listdir(bot_folder)
        if f.endswith(".py")
        and "bot" in f
        and not f.startswith("__")
        and f != 'judge.py'
    ]
    bot_paths = [os.path.join(bot_folder, f) for f in bot_files]
    bots_data = [[0, path] for path in bot_paths]

    n = len(bots_data)
    for i in range(n):
        for j in range(i + 1, n):
            name1 = os.path.basename(bots_data[i][1])
            name2 = os.path.basename(bots_data[j][1])

            print(f"\n=== Match: {name1} vs {name2} ===")
            run(i, j, bots_data)

            print(f"\n=== Reverse Match: {name2} vs {name1} ===")
            run(j, i, bots_data)

    print("\n=== Final Scores ===")
    for points, path in bots_data:
        print(f"{os.path.basename(path)}: {points} points")

if __name__ == '__main__':
    competition()
