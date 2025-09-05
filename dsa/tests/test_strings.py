import pytest
from dsa.problems.strings import (
    is_anagram, first_unique_char, longest_common_prefix,
    valid_parentheses, reverse_words, is_palindrome
)


class TestIsAnagram:
    def test_simple_anagram(self):
        assert is_anagram("anagram", "nagaram") is True

    def test_not_anagram(self):
        assert is_anagram("rat", "car") is False

    def test_different_lengths(self):
        assert is_anagram("a", "ab") is False

    def test_empty_strings(self):
        assert is_anagram("", "") is True

    def test_single_char(self):
        assert is_anagram("a", "a") is True

    def test_same_word_different_case(self):
        # Note: function assumes lowercase only
        assert is_anagram("listen", "silent") is True

    def test_repeated_characters(self):
        assert is_anagram("aabbcc", "abcabc") is True

    def test_different_frequencies(self):
        assert is_anagram("aabb", "aaab") is False


class TestFirstUniqueChar:
    def test_has_unique(self):
        assert first_unique_char("leetcode") == 0
    
    def test_no_unique(self):
        assert first_unique_char("aabb") == -1
    
    def test_single_char(self):
        assert first_unique_char("a") == 0
    
    def test_empty_string(self):
        assert first_unique_char("") == -1


class TestLongestCommonPrefix:
    def test_common_prefix(self):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    
    def test_no_common_prefix(self):
        assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    
    def test_single_string(self):
        assert longest_common_prefix(["a"]) == "a"
    
    def test_empty_list(self):
        assert longest_common_prefix([]) == ""


class TestValidParentheses:
    def test_valid_parentheses(self):
        assert valid_parentheses("()") is True
        assert valid_parentheses("()[]{}") is True
        assert valid_parentheses("([{}])") is True
    
    def test_invalid_parentheses(self):
        assert valid_parentheses("(]") is False
        assert valid_parentheses("([)]") is False
        assert valid_parentheses("(((") is False
    
    def test_empty_string(self):
        assert valid_parentheses("") is True


class TestReverseWords:
    def test_simple_reverse(self):
        assert reverse_words("the sky is blue") == "blue is sky the"
    
    def test_multiple_spaces(self):
        assert reverse_words("  hello world  ") == "world hello"
    
    def test_single_word(self):
        assert reverse_words("hello") == "hello"


class TestIsPalindrome:
    def test_valid_palindrome(self):
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("race a car") is False
    
    def test_alphanumeric_only(self):
        assert is_palindrome("racecar") is True
        assert is_palindrome("race a car") is False
    
    def test_case_insensitive(self):
        assert is_palindrome("A man a plan a canal Panama") is True
