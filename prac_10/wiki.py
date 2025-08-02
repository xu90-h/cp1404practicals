import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    """A function to try wikipedia"""
    while True:
        title = input("Enter title page:").strip()
        if not title:
            print("Thank you.")
            break