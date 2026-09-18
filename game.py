"""Two player game loop."""
from board import Board


def play():
    board = Board()
    current = "X"
    while not board.is_full():
        print(board)
        move = int(input(f"Player {current}, choose 1-9: ")) - 1
        if board.place(move, current):
            current = "O" if current == "X" else "X"
    print(board)
    print("Game over")
