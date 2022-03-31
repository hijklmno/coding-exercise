// set of allowed string prefixes
const ALLOWED_WORD_PREFIXES = new Set([
    '1A',
    '1B',
    '1C',
    '40',
    '4b',
])


export function validate_word_prefixes(words) {
    let valid_words = []
    words.forEach(function (element) {
        if (element.startsWith(ALLOWED_WORD_PREFIXES)) {
            valid_words = element
        }
    });

    return valid_words
}
