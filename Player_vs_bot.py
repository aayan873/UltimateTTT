# Here you can play with against your own bot

import importlib
from ultimate_ttt_engine import UltimateTTT

user_bot = importlib.import_module("random_bot")

def run_game():
    game = UltimateTTT()
    prev_move = None
    human_player = int(input("Do you want to be Player 1 or 2? "))
    bot_player = 3 - human_player

    player = 1
    while True:
        game.print_board()
        print(f"Player {player}'s turn")
        if player == human_player:
            move = tuple(map(int, input("Enter your move (i j): ").split()))
        else:
            move = user_bot.play(game.board, prev_move, bot_player)

        if not game.make_move(*move):
            print("Invalid move. You lose!")
            return

        prev_move = move
        winner = game.get_winner()
        if winner:
            game.print_board()
            print(f"Player {winner} wins!")
            return

        if all(game.board[i][j] != 0 for i in range(9) for j in range(9)):
            print("Draw!")
            return

        player = 3 - player

if __name__ == '__main__':
    run_game()
