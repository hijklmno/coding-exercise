package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	runFunctionValidator()

	webEnabled := false
	if webEnabled {
		http.HandleFunc("/validate", func(w http.ResponseWriter, _ *http.Request) {
			io.WriteString(w, "TODO run validate word prefixes function")
		})

		log.Fatal(http.ListenAndServe(":8080", nil))
	}
}

func runFunctionValidator() {
	run1 := ValidateWordPrefixes([]interface{}{"1A"})
	log.Printf("run1: given ['1A'] should return ['1A']; actual: %s", run1)

	run2 := ValidateWordPrefixes([]interface{}{"1A", "1A"})
	log.Printf("run2: given ['1A', '1A'] should return ['1A', '1A']; actual: %s", run2)

	run3 := ValidateWordPrefixes([]interface{}{"1B", "1C"})
	log.Printf("run3: given ['1B', '1C'] should return ['1B', '1C']; actual: %s", run3)

	run4 := ValidateWordPrefixes([]interface{}{"2C", "1C"})
	log.Printf("run4: given ['2C', '1C'] should return ['1C']; actual: %s", run4)

	run5 := ValidateWordPrefixes([]interface{}{})
	log.Printf("run5: given [] should return []; actual: %s", run5)

	run6 := ValidateWordPrefixes(nil)
	log.Printf("run6: given nil should return []; actual: %s", run6)

	run7 := ValidateWordPrefixes([]interface{}{"1b"})
	log.Printf("run7: given ['1b'] should return ['1b']; actual: %s", run7)

	run8 := ValidateWordPrefixes([]interface{}{"1C123"})
	log.Printf("run8: given ['1C123'] should return ['1C123']; actual: %s", run8)

	run9 := ValidateWordPrefixes([]interface{}{"4bABC"})
	log.Printf("run9: given ['4bABC'] should return ['4bABC']; actual: %s", run9)

	run10 := ValidateWordPrefixes([]interface{}{404})
	log.Printf("run10: given [404] should return ['404']; actual: %s", run10)

	run11 := ValidateWordPrefixes([]interface{}{10, "1C", 'Z'})
	log.Printf("run11: given [10, '1C', 'Z'] should return ['1C']; actual: %s", run11)
}