# This file is to run a game for bot v/s bot 


import importlib
from ultimate_ttt_engine import UltimateTTT

user_bot = importlib.import_module("bot_template")
random_bot = importlib.import_module("random_bot")

def run():
    game = UltimateTTT()
    prev_move = None
    player = 1
    for i in range(81):
        game.print_board()
        if player == 1:
            move = user_bot.play(game.board, prev_move, 1)

        else:
            move = random_bot.play(game.board, prev_move, 2)

        if not game.move(*move):
            print(f"Invalid move by Player {player} at {move}. Player {3 - player} wins!")
            return 3 - player

        prev_move = move
        player = 3 - player

    print("Draw!")
    return 0;

if __name__ == '__main__':
    run();