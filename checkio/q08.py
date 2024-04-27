"""

https://py.checkio.org/en/mission/replace-all-occurrences/

IMPORTANTE: Rresolver de forma mais explicita

def replace_all(mainText: str, target: str, repl: str) -> str:
    return mainText.replace(target, repl)

def replace_all(mainText: str, target: str, repl: str) -> str:
    words = mainText.split(target)
    return repl.join(words)


"""


def replace_all(mainText: str, target: str, repl: str) -> str:
    nova_palavra = ""
    i = 0
    while i < len(mainText):
        if mainText[i : i + len(target)] == target:
            nova_palavra += repl
            i = i + len(target)
        else:
            nova_palavra += mainText[i]
            i += 1
    return nova_palavra


print("Example:")
print(replace_all("hello worldp", "world", "TypeScript"))

# These "asserts" are used for self-checking
assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
assert (
    replace_all("hello world world", "world", "TypeScript")
    == "hello TypeScript TypeScript"
)
assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
assert replace_all("aaa", "a", "b") == "bbb"
assert replace_all("replace all the all", "all", "some") == "replace some the some"
assert replace_all("nothing to replace", "something", "nothing") == "nothing to replace"
assert replace_all("same same same", "same", "same") == "same same same"
assert replace_all("123 123", "123", "321") == "321 321"
assert replace_all("OpenAI", "AI", "Source") == "OpenSource"
assert replace_all("", "anything", "nothing") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
