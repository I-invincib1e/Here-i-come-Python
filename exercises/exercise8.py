# Exercise 8: Sum of List Elements
# Write a function that calculates the sum of all elements in a list.
# Example: sum_list([1, 2, 3, 4]) should return 10

def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4]))  # Expected: 10
