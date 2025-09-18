# Exercise 7: Check if a String is Palindrome
# Write a function that checks if a string is a palindrome.
# Example: is_palindrome("racecar") should return True

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test the function
if __name__ == "__main__":
    print(is_palindrome("racecar"))  # Expected: True
    print(is_palindrome("hello"))  # Expected: False
