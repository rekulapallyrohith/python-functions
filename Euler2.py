from math_utils import fibonacci_sequence,is_even

sequence = fibonacci_sequence(first = 1, second = 2, limit = 100)
result = 0
for number in sequence:
    if is_even(number):
        result += number
print(result)