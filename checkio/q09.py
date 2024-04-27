"""
https://py.checkio.org/en/mission/find-remainder/
"""


def find_remainder(dividend: int, divisor: int) -> int:
    resultado = dividend // divisor
    return abs(resultado * divisor - dividend)


def find_remainder_v2(dividend: int, divisor: int) -> int:
    return dividend % divisor


print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder_v2(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder_v2(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
