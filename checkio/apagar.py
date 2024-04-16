def longest_word(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    longest = max(words, key=len)
    return longest
