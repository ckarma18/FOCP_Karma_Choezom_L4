"""2. Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).
"""

def find_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

integer_input = int(input("Enter an integer: "))
result_factors = find_factors(integer_input)

print(f"The factors of {integer_input} are: {result_factors}")