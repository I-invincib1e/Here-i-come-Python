# Exercise 3: Reverse a String
# Write a function that reverses a given string.
# Example: reverse_string("hello") should return "olleh"

def reverse_string(s):
    return s[::-1]

# Test the function
if __name__ == "__main__":
    print(reverse_string("hello"))  # Expected: olleh
