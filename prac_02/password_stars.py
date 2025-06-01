MIN_LENGTH = 8

def get_password(MIN_LENGTH):
    """Set the valid password length to be at least 'min_length' characters"""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too easy, please enter at least {MIN_LENGTH} characters.")
    return password

def print_stars(password):
    print("*" * len(password))