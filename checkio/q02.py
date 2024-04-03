"""
https://py.checkio.org/en/mission/replace-all-occurrences/
"""


def replace_all(mainText: str, target: str, repl: str) -> str:
    words = mainText.split()
    for word in words:
        if word == target:
            words[words.index(word)] = repl
    return " ".join(words)


print("Example:")
print(replace_all("hello world", "world", "TypeScript"))
