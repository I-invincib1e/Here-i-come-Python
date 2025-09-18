# Exercise 5: Count Vowels in a String
# Write a function that counts the number of vowels in a string.
# Example: count_vowels("hello world") should return 3

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test the function
if __name__ == "__main__":
    print(count_vowels("hello world"))  # Expected: 3
