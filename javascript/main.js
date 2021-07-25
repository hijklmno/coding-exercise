import {validate_word_prefixes} from './functions.js';

let run1 = validate_word_prefixes(['1A']);  // should return ['1A']
console.log("run1 expected: ['1A']; actual:", run1);

let run2 = validate_word_prefixes(['1A', '1A']);  // should return ['1A', '1A']
console.log("run2 expected: ['1A', '1A']; actual:", run2);

let run3 = validate_word_prefixes(['1B', '1C']);  // should return ['1B', '1C']
console.log("run3 expected: ['1B', '1C']; actual:", run3);

let run4 = validate_word_prefixes(['2C', '1C']);  // should return ['1C']
console.log("run4 expected: ['1C']; actual:", run4);

let run5 = validate_word_prefixes([]);  // should return []
console.log("run5 expected: []; actual:", run5);

let run6 = validate_word_prefixes(null);  // should return []
console.log("run6 expected: []; actual:", run6);

let run7 = validate_word_prefixes(['1b']);  // should return ['1B']
console.log("run7 expected: ['1B']; actual:", run7);

let run8 = validate_word_prefixes([10, '1C']);  // should return ['1C']
console.log("run8 expected: ['1C']; actual:", run8);
