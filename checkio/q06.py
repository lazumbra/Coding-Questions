"""
https://py.checkio.org/en/mission/the-longest-word/

def longest_word(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    longest = max(words, key=len)
    return longest

and


"""


def longest_word(sentence: str) -> str:
    sentences = sentence.split(" ")
    if not sentences:
        return ""
    biggest = sentences[0]
    for word in sentences[1:]:
        if len(word) > len(biggest):
            biggest = word
    return biggest


def longest_word_v2(sentence: str) -> str:
    sentences = sentence.split(" ")
    if not sentences:
        return ""
    return max(sentences, key=len)


print("Example:")
print(longest_word("hello world"))


# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word_v2("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word_v2("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word_v2("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
