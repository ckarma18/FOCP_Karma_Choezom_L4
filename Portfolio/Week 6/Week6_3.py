"""3. Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.
"""

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number has a factor, it's not prime

    return True  # If no factors found, it's prime

integer_input = int(input("Enter an integer: "))
is_prime_result = is_prime(integer_input)

if is_prime_result:
    print(f"{integer_input} is a prime number.")
else:
    print(f"{integer_input} is not a prime number.")
