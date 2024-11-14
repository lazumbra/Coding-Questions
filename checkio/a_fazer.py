"""

https://py.checkio.org/en/mission/all-permutations/

------------------------------------------------

from collections.abc import Iterable
from itertools import permutations


def string_permutations(s: str) -> Iterable[str]:
    # Generate all permutations
    perm = permutations(s)
    # Convert permutations to strings and sort them
    sorted_perm = sorted("".join(p) for p in perm)
    return sorted_perm


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")

------------------------------------------------

from collections.abc import Iterable


def string_permutations(s: str) -> Iterable[str]:
    if len(s) == 1:
        return [s]

    perms = []
    for i, char in enumerate(s):
        # Remove the character at index i and find permutations of the remaining characters
        remaining = s[:i] + s[i + 1 :]
        for perm in string_permutations(remaining):
            perms.append(char + perm)

    # Sort the permutations alphabetically
    return sorted(perms)


------------------------------------------------


from collections.abc import Iterable

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def string_permutations(s: str) -> Iterable[str]:
    if len(s) == 1:
        return [s]

    perms = []
    for i, char in enumerate(s):
        # Remove the character at index i and find permutations of the remaining characters
        remaining = s[:i] + s[i + 1 :]
        for perm in string_permutations(remaining):
            perms.append(char + perm)

    # Sort the permutations alphabetically using insertion sort
    return insertion_sort(perms)

------------------------------------------------

from collections.abc import Iterable

def heap_permutation(elements):
    length = len(elements)
    counters = [0] * length  # Inicializa o vetor de contadores
    yield ''.join(elements)  # Gera a permutação inicial

    index = 0
    while index < length:
        if counters[index] < index:
            if index % 2 == 0:
                # Troca para index par
                elements[0], elements[index] = elements[index], elements[0]
            else:
                # Troca para index ímpar
                elements[counters[index]], elements[index] = elements[index], elements[counters[index]]
            yield ''.join(elements)  # Gera a nova permutação
            counters[index] += 1
            index = 0
        else:
            counters[index] = 0
            index += 1

def string_permutations(s: str) -> Iterable[str]:
    # Convert string to list of characters
    data = list(s)
    # Generate all permutations using Heap's algorithm
    perms = list(heap_permutation(data))
    # Sort the permutations alphabetically
    return sorted(perms)

------------------------------------------------


from collections.abc import Iterable

def heap_permutation(elements):
    length = len(elements)
    counters = [0] * length  # Inicializa o vetor de contadores
    permutations = [''.join(elements)]  # Armazena a permutação inicial

    index = 0
    while index < length:
        if counters[index] < index:
            if index % 2 == 0:
                # Troca para index par
                elements[0], elements[index] = elements[index], elements[0]
            else:
                # Troca para index ímpar
                elements[counters[index]], elements[index] = elements[index], elements[counters[index]]
            permutations.append(''.join(elements))  # Armazena a nova permutação
            counters[index] += 1
            index = 0
        else:
            counters[index] = 0
            index += 1

    return permutations

def string_permutations(s: str) -> Iterable[str]:
    # Convert string to list of characters
    data = list(s)
    # Generate all permutations using Heap's algorithm
    perms = list(heap_permutation(data))
    # Sort the permutations alphabetically
    return sorted(perms)

------------------------------------------------
"""
