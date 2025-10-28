"""Module providing a function to check if one number is a multiple of another.

This module contains:
    * is_multiple_of: Checks whether a given number is a multiple of another.
"""


def is_multiple_of(number: int, multiple: int) -> bool:
    """
    Check if a number is a multiple of another number.

    Args:
        number (int): The number to check.
        multiple (int): The number to check divisibility against.
    Returns:
        bool: True if `number` is a multiple of `multiple`, otherwise False.
    """
    return number % multiple == 0

def fibonacci_sequence(first: int = 1, second: int = 2, limit: int = 10) -> list[int]:
    """
    Generate a Fibonacci-like sequence up to a given limit.

    The sequence starts with the provided `first` and `second` numbers and continues
    by adding the two previous numbers until the next number would be equal to or
    exceed the specified limit.

    Args:
        first (int, optional): The first number in the sequence. Defaults to 1.
        second (int, optional): The second number in the sequence. Defaults to 2.
        limit (int, optional):The upper limit;sequence generation stops before exceeding this value.
        Defaults to 10.

    Returns:
        list[int]: A list containing the generated Fibonacci-like sequence.
    """
    sequence = []
    sequence.append(first)
    sequence.append(second)
    while first + second < limit:
        next_in_sequence = first + second
        sequence.append(next_in_sequence)
        first = second
        second = next_in_sequence
    return sequence

def is_even(number: int) -> bool:
    """
    Check whether a given number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, otherwise False.
    """
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """Check if a number is a prime number.

    A prime number is a number greater than 1 that has no positive divisors 
    other than 1 and itself.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def factors(number: int) -> list[int]:
    """Return all factors of a given number.

    A factor is a number that divides the given number exactly 
    (without leaving a remainder).

    Args:
        number (int): The number for which to find factors.

    Returns:
        list[int]: A list of all factors of the number.
    """
    result = []
    for index in range(1, number + 1):
        if number % index == 0:
            result.append(index)
    return result

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
