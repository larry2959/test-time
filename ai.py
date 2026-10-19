"""Computer opponents."""
import random


def random_move(board, mark):
    return random.choice(board.available_moves())


def _minimax(board, mark, me, depth):
    winner = board.winner()
    if winner == me:
        return 10 - depth
    if winner is not None:
        return depth - 10
    if board.is_full():
        return 0

    other = "O" if mark == "X" else "X"
    scores = []
    for move in board.available_moves():
        board.place(move, mark)
        scores.append(_minimax(board, other, me, depth + 1))
        board.undo(move)
    return max(scores) if mark == me else min(scores)


def best_move(board, mark):
    other = "O" if mark == "X" else "X"
    best, best_score = None, -100
    for move in board.available_moves():
        board.place(move, mark)
        score = _minimax(board, other, mark, 1)
        board.undo(move)
        if score > best_score:
            best, best_score = move, score
    return best
