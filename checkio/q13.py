"""
https://py.checkio.org/en/mission/longest-common-prefix/


"""


def longest_prefix(arr: list[str]) -> str:
    if not arr:
        return ""

    shortest_str = arr[0]

    for palavra in arr:
        if len(palavra) < len(shortest_str):
            shortest_str = palavra

    letra_prefixo = 0

    while True:
        if letra_prefixo >= len(shortest_str):
            break
        letra = shortest_str[letra_prefixo]
        for palavra in arr:
            if letra != palavra[letra_prefixo]:
                return shortest_str[:letra_prefixo]

        letra_prefixo += 1
    return shortest_str


# Example usage
print("Example:")
print(repr(longest_prefix(["flower", "flow", "flight"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
