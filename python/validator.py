from functions import validate_word_prefixes

run1 = validate_word_prefixes(['1A'])
print("run1: given ['1A'] should return ['1A']; actual:", run1)

run2 = validate_word_prefixes(['1A', '1A'])
print("run2: given ['1A', '1A'] should return ['1A', '1A']; actual:", run2)

run3 = validate_word_prefixes(['1B', '1C'])
print("run3: given ['1B', '1C'] should return ['1B', '1C']; actual:", run3)

run4 = validate_word_prefixes(['2C', '1C'])
print("run4: given ['2C', '1C'] should return ['1C']; actual:", run4)

run5 = validate_word_prefixes([])
print("run5: given [] should return []; actual:", run5)

run6 = validate_word_prefixes(None)
print("run6: given None should return []; actual:", run6)

run7 = validate_word_prefixes(['1b'])
print("run7: given ['1b'] should return ['1b']; actual:", run7)

run8 = validate_word_prefixes([10, '1C'])
print("run8: given [10, '1C'] should return ['1C']; actual:", run8)

run9 = validate_word_prefixes(['1C123'])
print("run9: given ['1C123'] should return ['1C123']; actual:", run9)

run10 = validate_word_prefixes(['4bABC'])
print("run10: given ['4bABC'] should return ['4bABC']; actual:", run10)

run11 = validate_word_prefixes([404])
print("run11: given [404] should return ['404']; actual:", run11)
