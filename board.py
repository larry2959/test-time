"""Board representation for Tic Tac Toe."""


class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def place(self, index, mark):
        if self.cells[index] != " ":
            return False
        self.cells[index] = mark
        return True

    def is_full(self):
        return " " not in self.cells

    def __str__(self):
        rows = []
        for r in range(3):
            row = self.cells[r * 3:r * 3 + 3]
            rows.append(" " + " | ".join(row))
        return "\n---+---+---\n".join(rows)
