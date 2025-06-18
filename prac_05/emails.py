"""
Program to store users' emails and names in a dictionary.
Estimate: 20 minutes
Actual:
"""

def main():
    """Get emails and extract names into a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ["", "y"]:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract name from email."""
    prefix = email.split('@')[0]
    name = ' '.join(part.capitalize() for part in prefix.split('.'))
    return name

main()