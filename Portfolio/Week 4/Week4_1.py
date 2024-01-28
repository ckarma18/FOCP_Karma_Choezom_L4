"""Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function"""

def validate_input(number):
    return 0 <= number <= 100

user_input = int(input("Enter an integer: "))

if validate_input(user_input):
    print("Valid input!")
else:
    print("Input is outside the range 0 to 100.")