import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

def main():
    try:
        quick_picks = int(input("How many quick picks?"))
        while quick_picks < 0:
            print("Please enter a non-negative number.")
    except ValueError:
        print("INvalid input. Please enter again.")
        return

    for _ in range(quick_picks):
        pick = quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

main()