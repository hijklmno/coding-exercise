from functions import validate_word_prefixes

run1 = validate_word_prefixes(['1A'])  # should return ['1A']
print("run1 expected: ['1A']; actual:", run1)

run2 = validate_word_prefixes(['1A', '1A'])  # should return ['1A', '1A']
print("run2 expected: ['1A', '1A']; actual:", run2)

run3 = validate_word_prefixes(['1B', '1C'])  # should return ['1B', '1C']
print("run3 expected: ['1B', '1C']; actual:", run3)

run4 = validate_word_prefixes(['2C', '1C'])  # should return ['1C']
print("run4 expected: ['1C']; actual:", run4)

run5 = validate_word_prefixes([])  # should return []
print("run5 expected: []; actual:", run5)

run6 = validate_word_prefixes(None)  # should return []
print("run6 expected: []; actual:", run6)

run7 = validate_word_prefixes(['1b'])  # should return ['1B']
print("run7 expected: ['1B']; actual:", run7)

run8 = validate_word_prefixes([10, '1C'])  # should return ['1C']
print("run8 expected: ['1C']; actual:", run8)
