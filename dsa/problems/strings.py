from __future__ import annotations

from typing import Dict, List


def is_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams (contain same characters with same frequencies).

    Anagrams have identical character counts, just rearranged.
    This solution uses a frequency count array for efficiency.

    Assumes lowercase English letters only (26 characters).

    Args:
        s: First string
        t: Second string

    Returns:
        True if strings are anagrams, False otherwise

    Time: O(n) where n is string length, Space: O(1) - fixed 26-element array
    """
    # Different lengths can't be anagrams
    if len(s) != len(t):
        return False

    # Use array to count character frequencies (26 lowercase letters)
    count = [0] * 26

    # Count characters in both strings simultaneously
    for i in range(len(s)):
        # Increment count for character in s
        count[ord(s[i]) - ord('a')] += 1
        # Decrement count for character in t
        count[ord(t[i]) - ord('a')] -= 1

    # If all counts are zero, strings have identical character frequencies
    return all(c == 0 for c in count)


def first_unique_char(s: str) -> int:
    """Find first non-repeating character index.
    
    Time: O(n), Space: O(1) - limited to 26 characters
    Trick: Two passes - count first, then find first with count=1
    """
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    for i, char in enumerate(s):
        if count[ord(char) - ord('a')] == 1:
            return i
    return -1


def longest_common_prefix(strs: List[str]) -> str:
    """Find longest common prefix among strings.
    
    Time: O(S) where S = sum of all characters, Space: O(1)
    Trick: Compare character by character, stop at first mismatch
    """
    if not strs:
        return ""
    
    # Use first string as reference
    for i, char in enumerate(strs[0]):
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]


def valid_parentheses(s: str) -> bool:
    """Check if parentheses are valid using stack.
    
    Time: O(n), Space: O(n)
    Trick: Use stack to match opening with closing brackets
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # opening bracket
            stack.append(char)
    
    return len(stack) == 0


def reverse_words(s: str) -> str:
    """Reverse words in a string.
    
    Time: O(n), Space: O(n)
    Trick: Split, reverse list, join - or two pointers for O(1) space
    """
    return ' '.join(s.split()[::-1])


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (alphanumeric only).
    
    Time: O(n), Space: O(1)
    Trick: Two pointers from both ends, skip non-alphanumeric
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
