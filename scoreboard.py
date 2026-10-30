"""Simple session scoreboard."""


class Scoreboard:
    def __init__(self):
        self.scores = {"X": 0, "O": 0, "draws": 0}

    def record(self, winner):
        if winner is None:
            self.scores["draws"] += 1
        else:
            self.scores[winner] += 1

    def __str__(self):
        s = self.scores
        return f"X: {s['X']}  O: {s['O']}  Draws: {s['draws']}"
