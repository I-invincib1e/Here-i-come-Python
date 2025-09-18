# Exercise 1: Calculate Factorial
# Write a function that calculates the factorial of a given number.
# Example: factorial(5) should return 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
if __name__ == "__main__":
    print(factorial(5))  # Expected: 120
