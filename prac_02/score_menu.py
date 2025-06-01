import score

MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
"""

def get_valid_score():
    """Return the score from 0 to 100 and loop it."""
    score_value = float(input("Enter score: "))
    while score_value < 0 or score_value > 100:
        print("Invalid score.")
        score_value = float(input("Enter score: "))
    return score_value

def show_stars(score_value):
    print("*" * int(score_value))

def main():
    """Firstly, get a value score, then enter the menu loop."""
    print(get_valid_score())
    print(MENU)
    choice = input(">>> ")

    while choice != "Q":
        if choice == "G":
            score_value = get_valid_score()
        elif choice == "P":
            print()
        elif choice == "S":
            print(show_stars(score_value))
        else:
            print("Invalid option.")