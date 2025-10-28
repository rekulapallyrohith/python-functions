"""Module for finding prime factors of a given number.

This module imports utility functions from `math_utils` to determine whether
a number is prime and to compute all factors of a given number. It then uses
these utilities to find and display the prime factors of a user-provided number.
"""

from math_utils import is_prime, factors

num = int(input("Enter the number: "))

def prime_factor(number:int) -> list[int]:
    """Return the list of prime factors of a given number.

    Finds all factors of the provided number and filters them to include
    only the factors that are prime numbers.

    Args:
        number (int): The number for which to find prime factors.

    Returns:
        list[int]: A list containing all prime factors of the given number.
    """
    all_factors = factors(number)
    prime_factor_list = []
    for f in all_factors:
        if is_prime(f):
            prime_factor_list.append(f)
    return prime_factor_list


print(prime_factor(num))
