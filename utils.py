import re
from unicodedata import normalize


def remove_diacritics(text):
    """
    Remove diacritics from a text.
    """
    denormalized = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", text), 0, re.I
    )
    return normalize('NFC', denormalized)
