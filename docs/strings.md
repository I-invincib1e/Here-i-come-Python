# String Problems

String manipulation problems often involve pattern matching, character counting, and two-pointer techniques.

## Valid Anagram

**Problem**: Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

**Solution Approach**:
- Check if lengths are equal
- Use frequency count array (26 letters)
- Increment for s, decrement for t
- All counts should be zero

**Time Complexity**: O(n)
**Space Complexity**: O(1) (fixed size array)

## First Unique Character

**Problem**: Given a string `s`, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

**Solution Approach**:
- Two-pass algorithm
- First pass: count frequency of each character
- Second pass: find first character with count = 1

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Longest Common Prefix

**Problem**: Write a function to find the longest common prefix string amongst an array of strings.

**Solution Approach**:
- Use first string as reference
- Compare character by character with other strings
- Stop at first mismatch or end of any string

**Time Complexity**: O(S) where S = sum of all characters
**Space Complexity**: O(1)

## Valid Parentheses

**Problem**: Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

**Solution Approach**:
- Use stack to track opening brackets
- For closing bracket, check if matches stack top
- Stack should be empty at end

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Reverse Words

**Problem**: Given an input string `s`, reverse the order of the words.

**Solution Approach**:
- Split string into words
- Reverse the list of words
- Join with spaces

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Valid Palindrome

**Problem**: Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Solution Approach**:
- Use two pointers from start and end
- Skip non-alphanumeric characters
- Compare characters (case-insensitive)

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## String Patterns

### Two Pointers for Strings
- Use for palindrome checks, removing spaces
- Move pointers from both ends
- Skip invalid characters

### Frequency Counting
- Use arrays for limited character sets (ASCII, lowercase)
- Use hash maps for Unicode characters
- Count occurrences for anagrams, duplicates

### String Building
- Use list to build strings (mutable)
- Join at end for efficiency
- Avoid string concatenation in loops

### Substring Problems
- Sliding window for fixed/variable windows
- Two pointers for expanding/contracting
- Hash maps for substring sums

## Practice Tips

1. **Character encoding**: Consider ASCII vs Unicode
2. **Case sensitivity**: Use `.lower()` or `.upper()` consistently
3. **Empty strings**: Handle empty input gracefully
4. **Immutable strings**: Use lists for building, convert to string at end
5. **Boundary checks**: Validate indices before accessing characters
