# Valid Anagram

s = "anagram"
t = "nagaram"


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return count_chars(s) == count_chars(t)


def count_chars(s: str) -> dict:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

