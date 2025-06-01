MIN_LENGTH = 8

def main():
    password = get_password(MIN_LENGTH)
    print(print_stars(password))

def get_password(MIN_LENGTH):
    """Set the valid password length to be at least 'min_length' characters"""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too easy, please enter at least {MIN_LENGTH} characters.")
        password = input("Enter password: ")
    return password

def print_stars(password):
    print("*" * len(password))

if __name__ == '__main__':
    main()