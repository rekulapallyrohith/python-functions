"""
This module provides basic arithmetic operations: addition, subtraction, and multiplication.

Functions:
    add(a, b): Returns the sum of two integers.
    sub(a, b): Returns the difference between two integers.
    mul(a, b): Returns the product of two integers.
"""

def add(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def sub(a: int, b: int) -> int:
    """
    Returns the difference between two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of subtracting b from a.
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Returns the product of two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b

#result = mul(5, 6)
#print(result)
