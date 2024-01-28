"""Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    password2 = input("Confirm your password: ")

    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
        break
    else:
        print("Passwords do not match, do not meet length criteria, or are in the list of bad passwords. Please try again.")