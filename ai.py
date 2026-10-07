"""Computer opponents."""
import random


def random_move(board, mark):
    return random.choice(board.available_moves())
