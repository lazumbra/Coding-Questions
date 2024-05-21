"""
https://py.checkio.org/en/mission/bird-language/

"""


def translation(text: str) -> str:
    vogais = "aeiouy"
    i = 0
    nova_palavra = ""

    while i < len(text):
        nova_palavra += text[i]
        if text[i] in vogais:
            i += 3
        elif text[i].isalpha():
            i += 2
        else:
            i += 1

    return nova_palavra


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
