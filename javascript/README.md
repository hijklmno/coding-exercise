# Coding Exercise

## Instructions
In this repository, we have three files:
* the main entrypoint file, `main.js`,
* the functions file, `functions.js`, and
* the function validator file, `validator.js`

`functions.js` has a method `validate_word_prefixes`, which its main function is to filter out valid strings that have 
a valid prefix. For various reasons, the function `validate_word_prefixes` has bugs and needs to be fixed.

### Part 1 - Failing test cases
Your goal is to have all the run cases in `validator.js` working. You can run the `validator.js` via 
`npm run validator` or via `node validator.js`.

Feel free to use any debugging tools or online sources for solutions.

### Part 2 - Using proper unit tests
Your goal is to use a unit test framework to test the function `validate_word_prefixes`. 

You may reuse the test cases in `validator.js`.

### Part 3 - Running locally
Get the node app the run locally. 

### Part 4 - Surfacing APIs
Your goal is to surface two APIs:
An API that takes in multiple words and returns the results from validate_word_prefixes()
An API that updates the current filter conditions

You may replace express with another framework if you prefer.

### Part 5 - Deployment 
Dockerize the app. Don't worry about multi-environments yet.
