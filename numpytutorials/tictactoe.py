import numpy as np

def create_board():
    return np.zeros((3, 3), dtype=int)

def check_win(board, player):
    # Check rows
    for row in board:
        if np.all(row == player):
            return True
    # Check columns
    for col in board.T:
        if np.all(col == player):
            return True
    # Check diagonals
    if (board[0, 0] == player and board[1, 1] == player and board[2, 2] == player) or \
       (board[0, 2] == player and board[1, 1] == player and board[2, 0] == player):
        return True
    return False

def check_draw(board):
    return np.all(board != 0)

def play_game():
    board = create_board()
    player = 1

    while True:
        print(board)
        row, col = map(int, input(f"Player {player}'s turn (row, col): ").split())

        if board[row, col] != 0:
            print("Invalid move. Try again.")
            continue

        board[row, col] = player

        if check_win(board, player):
            print(f"Player {player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        player = 2 if player == 1 else 1


play_game()
