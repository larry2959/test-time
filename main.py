from game import play

if __name__ == "__main__":
    choice = input("Play against the computer? (y/n): ").strip().lower()
    play(vs_computer=choice == "y")
