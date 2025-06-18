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
        email_to_name[email] = ""
        email = input("Email: ")

def extract_name(email):
    """Extract name from email."""
    prefix = email.split('@')[0]
    name = ' '.join(part.capitalize() for part in prefix.split('.'))
    return name