Roman Numerals Kata
-------------------
# Description
The Roman Numerals kata challenges you to implement the conversion between Roman numerals and modern integers (and vice versa). Roman numerals, used in ancient Rome, are a non-positional numeral system with a fascinating set of rules. This kata is a perfect exercise in algorithmic thinking, test-driven development, and clean coding.
The task involves encoding and decoding Roman numerals while adhering to their historical conventions.
# Objective
Implement functions to:
* Convert integers to Roman numerals.
* Convert Roman numerals back to integers.
The solution should handle all valid Roman numerals up to 3000 (MMM), ensuring correctness and clarity.
# Roman Numerals Basics
## Symbols and Values:
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |    
| L      | 50    |    
| C      | 100   |   
| D      | 500   |   
| M      | 1000  |   
## Rules:
* Symbols are arranged from largest to smallest, with values added together.
  * Example: XVII = 10 + 5 + 1 + 1 = 17
* Smaller symbols placed before larger ones indicate subtraction.
  * Example: IV = 5 - 1 = 4, IX = 10 - 1 = 9
* A symbol may not be repeated more than 3 times in succession.
  * Example: III = 3, but IIII is invalid.
* Only certain subtractions are allowed:
  * I before V or X (e.g., IV, IX)
  * X before L or C (e.g., XL, XC)
  * C before D or M (e.g., CD, CM)
# Requirements
Your solution must:
* Input:
  * An integer (1–3000) for to_roman().
  * A valid Roman numeral string for from_roman().
* Output:
  * A Roman numeral string for to_roman().
  * An integer for from_roman().
* Validate: Reject invalid Roman numeral strings in from_roman().
# Constraints
* Handle numbers between 1 and 3000.
* Ensure Roman numeral formatting adheres to historical rules.
* Focus on correctness and readability for both conversions.
# Bonus points
* Larger Numbers:
  * Extend the range beyond 3000 (e.g., using overlines to represent multiples of 1000).
* Error Handling:
  * Detect and reject malformed Roman numeral strings.
* Custom Symbols:
  * Add support for additional symbols or modified numeral systems.