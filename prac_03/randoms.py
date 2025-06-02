import random

print(random.randint(5, 20))  # line 1
# Return an integer including both ends.
# The minimum value is 5 and the maximum value is 20

print(random.randrange(3, 10, 2))  # line 2
# Return a value
# The minimum value is 3 and the maximum value is 9.

print(random.uniform(2.5, 5.5))  # line 3
# Return a random number of type float.
# The minimum value is 2.5 and the maximum value is 5.5.


print(f"Random number between 1 and 100: {random.randint(1, 100)}")
# Produce a random number between 1 and 100 inclusive.