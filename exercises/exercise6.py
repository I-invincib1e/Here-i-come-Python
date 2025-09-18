# Exercise 6: Generate Fibonacci Sequence
# Write a function that generates the first n Fibonacci numbers.
# Example: fibonacci(5) should return [0, 1, 1, 2, 3]

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Test the function
if __name__ == "__main__":
    print(fibonacci(5))  # Expected: [0, 1, 1, 2, 3]
