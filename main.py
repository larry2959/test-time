from game import play
from scoreboard import Scoreboard


def main():
    scoreboard = Scoreboard()
    vs_computer = input("Play against the computer? (y/n): ").strip().lower() == "y"
    difficulty = "easy"
    if vs_computer:
        difficulty = input("Difficulty (easy/hard): ").strip().lower() or "easy"

    while True:
        winner = play(vs_computer=vs_computer, difficulty=difficulty)
        scoreboard.record(winner)
        print(scoreboard)
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
