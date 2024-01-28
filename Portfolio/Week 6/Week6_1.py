"""1. Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!
"""


def integer_to_binary_representation(number):
    if number > 0:
        binary_representation = bin(number)[2:]  # [2:] to remove the '0b' prefix
        return binary_representation
    else:
        return "Invalid input. Please provide a positive integer."

positive_integer = int(input("Enter a positive integer: "))
binary_representation = integer_to_binary_representation(positive_integer)

print(f"The binary representation of {positive_integer} is: {binary_representation}")