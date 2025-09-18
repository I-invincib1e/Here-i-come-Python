# Exercise 2: Check if a Number is Prime
# Write a function that checks if a given number is prime.
# Example: is_prime(7) should return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
if __name__ == "__main__":
    print(is_prime(7))  # Expected: True
    print(is_prime(10))  # Expected: False
