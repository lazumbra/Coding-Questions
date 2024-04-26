"""
https://py.checkio.org/en/mission/fuzzy-string-matching/

Interessante usar: distância de Levenshtein

Buscar sobre vídeos sobre distância de Levenshtein ou distância de edição

The Levenshtein distance algorithm is also known as the "edit distance"


Um vídeo bom é o seguinte abaixo
AED3 12 08 Casamento aproximado de padrões e a distância de edição


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    if abs(len(str1) - len(str2)) > threshold:
        return False

    if not str1 and not str2:
        return True

    if not str1 or not str2:
        return False

    if threshold == 0:
        return str1 == str2

    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        dp[i][0] = i

    for j in range(len(str2) + 1):
        dp[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[len(str1)][len(str2)] <= threshold

ou

def levenshtein_distance(str1: str, str2: str) -> int:
    if len(str1) < len(str2):
        return levenshtein_distance(str2, str1)

    if len(str2) == 0:
        return len(str1)

    previous_row = range(len(str2) + 1)
    for i, c1 in enumerate(str1):
        current_row = [i + 1]
        for j, c2 in enumerate(str2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    return levenshtein_distance(str1, str2) <= threshold

"""


def fuzzy_string_match_v2(str1: str, str2: str, threshold: int) -> bool:
    if abs(len(str1) - len(str2) > threshold):
        return False

    str1 = str1.ljust(len(str2))
    str2 = str2.ljust(len(str1))

    differences = sum(c1 != c2 for c1, c2 in zip(str1, str2))

    return differences <= threshold


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:

    if abs(len(str1) - len(str2)) > threshold:
        return False

    differences = abs(len(str1) - len(str2))

    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            differences += 1

    if differences > threshold:
        return False

    return True


print("Example:")
print(fuzzy_string_match_v2("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match_v2("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match_v2("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match_v2("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False
assert fuzzy_string_match("fuzzy", "fuzy", 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
