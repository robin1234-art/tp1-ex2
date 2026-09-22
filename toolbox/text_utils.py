import re

def is_palindrome(s: str) -> bool:
    """Renvoie True si s est un palindrome (insensible à la casse et aux espaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_frequency(text: str) -> dict:
    """Renvoie {mot: nombre d'occurrences}, insensible à la casse et à la ponctuation."""
    words = re.findall(r'[a-zA-Z]+', text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
