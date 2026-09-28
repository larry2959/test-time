"""Board representation for Tic Tac Toe."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def place(self, index, mark):
        if not 0 <= index < 9 or self.cells[index] != " ":
            return False
        self.cells[index] = mark
        return True

    def undo(self, index):
        self.cells[index] = " "

    def available_moves(self):
        return [i for i, c in enumerate(self.cells) if c == " "]

    def is_full(self):
        return " " not in self.cells

    def winner(self):
        for a, b, c in WIN_LINES:
            if self.cells[a] != " " and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def reset(self):
        self.cells = [" "] * 9

    def __str__(self):
        rows = []
        for r in range(3):
            chunk = self.cells[r * 3:r * 3 + 3]
            row = [c if c != " " else str(r * 3 + i + 1) for i, c in enumerate(chunk)]
            rows.append(" " + " | ".join(row))
        return "\n---+---+---\n".join(rows)
