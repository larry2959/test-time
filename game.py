"""Game loop supporting human and computer players."""
from board import Board
import ai


def ask_move(board, mark):
    while True:
        raw = input(f"Player {mark}, choose 1-9: ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        move = int(raw) - 1
        if board.place(move, mark):
            return
        print("That square is not available.")


def play(vs_computer=False, ai_mark="O"):
    board = Board()
    current = "X"
    while True:
        print(board)
        if vs_computer and current == ai_mark:
            board.place(ai.random_move(board, current), current)
            print(f"Computer ({current}) moved.")
        else:
            ask_move(board, current)
        winner = board.winner()
        if winner:
            print(board)
            print(f"Player {winner} wins!")
            return winner
        if board.is_full():
            print(board)
            print("It's a draw.")
            return None
        current = "O" if current == "X" else "X"
