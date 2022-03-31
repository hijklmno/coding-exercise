import {validate_word_prefixes} from './functions.js';

let run1 = validate_word_prefixes(['1A']);
console.log("run1 given ['1A'] expected: ['1A']; actual:", run1);

let run2 = validate_word_prefixes(['1A', '1A']);
console.log("run2 given ['1A', '1A'] expected: ['1A', '1A']; actual:", run2);

let run3 = validate_word_prefixes(['1B', '1C']);
console.log("run3 given ['1B', '1C'] expected: ['1B', '1C']; actual:", run3);

let run4 = validate_word_prefixes(['2C', '1C']);
console.log("run4 given ['2C', '1C'] expected: ['1C']; actual:", run4);

let run5 = validate_word_prefixes([]);
console.log("run5 given [] expected: []; actual:", run5);

let run6 = validate_word_prefixes(null);
console.log("run6 given null expected: []; actual:", run6);

let run7 = validate_word_prefixes(['1b']);
console.log("run7 given ['1b'] expected: ['1b']; actual:", run7);

let run8 = validate_word_prefixes([10, '1C']);
console.log("run8 given [10, '1C'] expected: ['1C']; actual:", run8);

let run9 = validate_word_prefixes(['1C123']);
console.log("run9 given ['1C123'] expected: ['1C123']; actual:", run9);

let run10 = validate_word_prefixes(['4bABC']);
console.log("run10 given ['4bABC'] expected: ['4bABC']; actual:", run10);

let run11 = validate_word_prefixes([404]);
console.log("run11 given [404] expected: ['404']; actual:", run11);
