# tuple of allowed string prefixes
ALLOWED_WORD_PREFIXES = (
    '1A',
    '1B',
    '1C',
)


def validate_word_prefixes(words):
    valid_words = []
    for word in words:
        if word.startswith(ALLOWED_WORD_PREFIXES):
            valid_words = word
    return valid_words
