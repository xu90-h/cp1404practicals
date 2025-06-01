import random

MIN_SCORE = 0
MAX_SCORE = 100

def user_score(score):
    """Return the result according to score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score."
    elif score >= 90:
        return "Excellent."
    elif score >= 50:
        return "Pass."
    else:
        return "Bad."

def main():
    """Get the user's score, display the result and display the random score"""
    score = float(input("Enter score: "))
    print(user_score(score))
    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    print("Random score is: ", random_score)
    print(user_score(random_score))

main()