# Exercise 4: Find Maximum in a List
# Write a function that finds the maximum value in a list.
# Example: find_max([1, 3, 2, 5, 4]) should return 5

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# Test the function
if __name__ == "__main__":
    print(find_max([1, 3, 2, 5, 4]))  # Expected: 5
