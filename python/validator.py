from functions import validate_word_prefixes

run1 = validate_word_prefixes(['1A'])  # should return ['1A']
print("should return ['1A']; actual:", run1)

run2 = validate_word_prefixes(['1A', '1A'])  # should return ['1A', '1A']
print("should return ['1A', '1A']; actual:", run2)

run3 = validate_word_prefixes(['1B', '1C'])  # should return ['1B', '1C']
print("should return ['1B', '1C']; actual:", run3)

run4 = validate_word_prefixes(['2C', '1C'])  # should return ['1C']
print("should return ['1C']; actual:", run4)

run5 = validate_word_prefixes([])  # should return []
print("should return []; actual:", run5)

run6 = validate_word_prefixes(None)  # should return []
print("should return []; actual:", run6)

run7 = validate_word_prefixes(['1b'])  # should return ['1b']
print("should return ['1B']; actual:", run7)

run8 = validate_word_prefixes([10, '1C'])  # should return ['1C']
print("should return ['1C']; actual:", run8)

run9 = validate_word_prefixes(['1C123'])  # should return ['1C123']
print("should return ['1C123']; actual:", run9)

run10 = validate_word_prefixes(['4bABC'])  # should return ['4bABC']
print("should return ['4bABC']; actual:", run10)

run11 = validate_word_prefixes([404])  # should return ['404']
print("should return ['404']; actual:", run11)
