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