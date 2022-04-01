# Coding Exercise

## Instructions
In this repository, we have two files:
* the main entrypoint file, `main.go`,
* the functions file, `functions.go`

`functions.go` has a method `ValidateWordPrefixes`, which its main function is to return input strings 
that have a valid prefix. For various reasons, the function `ValidateWordPrefixes` has bugs and needs to be fixed.

### Part 1 - Failing test cases
Your goal is to have all the runs in `main.go` working. You can run the file via `go run .`.

Feel free to use any debugging tools or online sources for solutions.

### Part 2 - Using proper go tests
Your goal is to use go unit tests to test the function `validate_word_prefixes`. 

You may reuse the test cases in `validator.go`.

### Part 3 - Running locally
Get the Go app the run locally. In main.go, set `webEnabled` to `true`.

### Part 4 - Surfacing APIs
Your goal is to surface two APIs:
* An API that takes in multiple words and returns the results from `validate_word_prefixes()`
* An API that updates AllowedWordPrefixes

### Part 5 - Deployment 
Dockerize the app. Don't worry about multi-environments yet.
