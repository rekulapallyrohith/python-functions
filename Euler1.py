from math_utils import is_multiple_of

MAX = 15
result = 0
for number in range(1, MAX):
    if is_multiple_of(number, 3) or is_multiple_of(number, 5):
        result+= number
print(result)