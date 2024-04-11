"""
Count Substring Occurrences
https://py.checkio.org/en/mission/count-substring-occurrences/

v1
def count_occurrences(main_string: str, substring: str) -> int:
    main_string = main_string.lower()
    substring = substring.lower()
    count = start = 0
    while start < len(main_string):
        pos = main_string.find(substring, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

"""


def count_occurrences(main_string: str, substring: str) -> int:
    main_string = main_string.lower()
    substring = substring.lower()
    count = 0
    sub_len = len(substring)

    for i in range(len(main_string) - sub_len + 1):
        if main_string[i : i + sub_len] == substring:
            count += 1

    return count


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1
print("The mission is done! Click 'Check Solution' to earn rewards!")
