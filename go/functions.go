package main

import "strings"

var AllowedWordPrefixes = []string{"1A", "1B", "1C", "40", "4b"}

func ValidateWordPrefixes(words []interface{}) []string {
	var validWords []string
	for _, word := range words {
		for _, allowedWord := range AllowedWordPrefixes {
			if strings.HasPrefix(word.(string), allowedWord) {
				validWords = []string{word.(string)}
			}
		}
	}
	return validWords
}