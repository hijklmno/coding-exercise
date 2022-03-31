# Coding Exercise

## Instructions
In this repository, we have three files:
* the main entrypoint file, `main.py`,
* the functions file, `functions.py`, and
* the function validator file, `validator.py`

`functions.py` has a method `validate_word_prefixes`, which its main function is to filter out valid strings 
that have a valid prefix. For various reasons, the function `validate_word_prefixes` has bugs and needs to be fixed.

### Part 1 - Failing test cases
Your goal is to have all the runs in `validator.py` working. You can run the file via `python validator.py`.

Feel free to use any debugging tools or online sources for solutions.

### Part 2 - Using proper python unit tests
Your goal is to use python unit tests to test the function `validate_word_prefixes`. 

You may reuse the test cases in `validator.py`.

### Part 3 - Running locally
Get the Flask app the run locally. We use Pipfile for dependency management. 

You may optionally use virtual environments if needed.

### Part 4 - Surfacing APIs
Your goal is to surface two APIs:
* An API that takes in multiple words and returns the results from `validate_word_prefixes()`
* An API that updates the allowed word prefixes

### Part 5 - Deployment 
Dockerize the app. Don't worry about multi-environments yet.
